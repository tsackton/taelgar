#!/usr/bin/env python3
import re
import sys
from datetime import datetime

def parse_chat(lines):
    messages = []
    current_user = None
    current_date = None      # holds "MM/DD/YYYY" from the last date-header
    next_timestamp = None    # tuple (date_str, time_str)
    expecting_content = False

    user_header_re = re.compile(r'^\*\*(.+?)\*\*$')
    date_header_re = re.compile(
        r'^(\d{1,2}/\d{1,2}/\d{4}) at (\d{1,2}:\d{2} (?:AM|PM))(?: [A-Z]+)?$'
    )
    time_only_re = re.compile(r'^(\d{1,2}:\d{2} (?:AM|PM))$')

    for raw in lines:
        line = raw.strip()
        if not line:
            continue

        # 1) New user block
        m = user_header_re.match(line)
        if m:
            current_user = m.group(1)
            expecting_content = False
            continue

        # 2) Full date header => sets our date+time for the very next message
        m = date_header_re.match(line)
        if m:
            current_date = m.group(1)
            time_str = m.group(2)
            next_timestamp = (current_date, time_str)
            expecting_content = True
            continue

        # 3) “Time only” header => same date, but new time
        m = time_only_re.match(line)
        if m and current_date:
            time_str = m.group(1)
            next_timestamp = (current_date, time_str)
            expecting_content = True
            continue

        # 4) Content line for the pending timestamp
        if expecting_content and current_user and next_timestamp:
            date_str, time_str = next_timestamp
            dt = datetime.strptime(f"{date_str} {time_str}", "%m/%d/%Y %I:%M %p")
            messages.append((dt, current_user, line))
            expecting_content = False
            continue

        # (All other lines are ignored; if you have truly multi-line messages,
        # you could extend this to append to the last message if you'd like.)

    return messages

def reformat_chat_file(path):
    with open(path, encoding='utf-8') as f:
        lines = f.readlines()

    msgs = parse_chat(lines)
    msgs.sort(key=lambda x: x[0])  # oldest first

    for dt, user, content in msgs:
        # Build “M/D/YYYY” with no leading zeros, and “H:MM AM/PM”
        date_part = f"{dt.month}/{dt.day}/{dt.year}"
        time_part = dt.strftime("%I:%M %p").lstrip("0")
        print(f"[{date_part} {time_part}] {user}")
        print(content)
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python reformat_chat.py <input_file>")
        sys.exit(1)
    reformat_chat_file(sys.argv[1])
