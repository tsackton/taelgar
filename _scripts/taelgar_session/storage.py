"""Bundle-safe paths, byte fingerprints, atomic writes, and cross-platform locks."""
import contextlib
import hashlib
import os
from pathlib import Path
import sys
import uuid

if sys.platform != 'win32':
    import fcntl

_held_windows_locks = set()


class PipelineError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise PipelineError(message)


def sha(value):
    return hashlib.sha256(value if isinstance(value, bytes) else value.encode()).hexdigest()


def safe(root, relative):
    root = Path(root).resolve()
    require(not Path(relative).is_absolute(), f'Managed path must be relative: {relative}')
    candidate = root / relative
    resolved = candidate.resolve()
    require(resolved.is_relative_to(root) and resolved != root, f'Path escapes session bundle: {relative}')
    for part in [candidate, *candidate.parents]:
        if part == root:
            break
        require(not part.is_symlink(), f'Managed path is a symlink: {relative}')
    return candidate


def open_no_follow(path, flags, mode=0o644):
    """Open a draft without following reparse points, on either platform."""
    if sys.platform != 'win32':
        return os.open(path, flags | os.O_NOFOLLOW, mode)
    import ctypes
    from ctypes import wintypes
    import msvcrt
    api = ctypes.WinDLL('kernel32', use_last_error=True)
    api.CreateFileW.argtypes = [wintypes.LPCWSTR, wintypes.DWORD, wintypes.DWORD,
                               ctypes.c_void_p, wintypes.DWORD, wintypes.DWORD, wintypes.HANDLE]
    api.CreateFileW.restype = wintypes.HANDLE
    api.CloseHandle.argtypes = [wintypes.HANDLE]
    access = 0xC0000000 if flags & os.O_RDWR else 0x40000000
    # Exclusive handle, CREATE_NEW or OPEN_EXISTING, OPEN_REPARSE_POINT.
    handle = api.CreateFileW(str(path), access, 0, None, 1 if flags & os.O_EXCL else 3, 0x00200000, None)
    if handle == wintypes.HANDLE(-1).value:
        raise ctypes.WinError(ctypes.get_last_error())
    try:
        fd = msvcrt.open_osfhandle(handle, (os.O_RDWR if flags & os.O_RDWR else os.O_WRONLY) | os.O_BINARY)
    except BaseException:
        api.CloseHandle(handle)
        raise
    try:
        require(not (getattr(os.fstat(fd), 'st_file_attributes', 0) & 0x400), 'Draft must not be a reparse point')
    except BaseException:
        os.close(fd)
        raise
    return fd


def atomic(root, relative, data):
    path = safe(root, relative)
    path.parent.mkdir(parents=True, exist_ok=True)
    temp = path.with_name(path.name + '.' + uuid.uuid4().hex + '.tmp')
    try:
        with temp.open('xb') as out:
            out.write(data)
            out.flush()
            os.fsync(out.fileno())
        os.replace(temp, path)
    finally:
        if temp.exists():
            temp.unlink()


@contextlib.contextmanager
def lock(root):
    # Windows cannot flock a directory. A kernel mutex gives the same
    # process-crash release and no-sidecar contract for all session helpers.
    if sys.platform == 'win32':
        import ctypes
        from ctypes import wintypes
        api = ctypes.WinDLL('kernel32', use_last_error=True)
        api.CreateMutexW.argtypes = [ctypes.c_void_p, wintypes.BOOL, wintypes.LPCWSTR]
        api.CreateMutexW.restype = wintypes.HANDLE
        api.WaitForSingleObject.argtypes = [wintypes.HANDLE, wintypes.DWORD]
        api.WaitForSingleObject.restype = wintypes.DWORD
        api.ReleaseMutex.argtypes = [wintypes.HANDLE]
        api.CloseHandle.argtypes = [wintypes.HANDLE]
        name = 'Local\\TaelgarSession-' + sha(os.path.normcase(str(Path(root).resolve())))
        handle = api.CreateMutexW(None, False, name)
        if not handle:
            raise ctypes.WinError(ctypes.get_last_error())
        acquired = False
        try:
            result = api.WaitForSingleObject(handle, 0)
            # WAIT_ABANDONED also grants ownership after a crashed writer.
            require(result in (0, 0x80), 'Another writer is working in this session bundle.')
            acquired = True
            require(name not in _held_windows_locks, 'Another writer is working in this session bundle.')
            _held_windows_locks.add(name)
            try:
                yield
            finally:
                _held_windows_locks.remove(name)
        finally:
            if acquired:
                api.ReleaseMutex(handle)
            api.CloseHandle(handle)
        return
    # The bundle directory survives finalization; never delete a lock inode.
    handle = os.open(root, os.O_RDONLY)
    try:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise PipelineError('Another writer is working in this session bundle.') from exc
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)
    finally:
        os.close(handle)
