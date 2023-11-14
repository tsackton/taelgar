from metadataUtils import *

def filter_whereabouts(whereabouts, target_date, type=None, allow_past=False):
    """
    Takes a whereabouts list of dicts, a target date, and optionally a type
    Returns all valid whereabouts for the specified type on the target date
    """

    target_date = clean_date(target_date)

    valid_whereabouts = []

    for entry in whereabouts:
        if type is not None and entry['type'] != type:
            continue
        else:
            #valid type, or no type specified
            start_date = clean_date(entry['start']) if "start" in entry else date.min
            end_date = clean_date(entry['end'], end=True) if "end" in entry else date.max
            entry["recency"] = (target_date - start_date).days
            entry["duration"] = (end_date - start_date).days
            if allow_past and start_date <= target_date:
                valid_whereabouts.append(entry)
            elif start_date <= target_date and end_date >= target_date:
                valid_whereabouts.append(entry)


    return valid_whereabouts

def get_whereabouts(metadata, target_date):
    """
    Takes a metadata dict and a target date
    Returns a list of whereabouts dicts for the target date
    """

    # Get whereabouts from metadata
    whereabouts = metadata.get('whereabouts', [])

    # Get valid locations for each type
    valid_homes = filter_whereabouts(whereabouts, target_date, type='home', allow_past=False)
    valid_origins = filter_whereabouts(whereabouts, target_date, type='home', allow_past=True)
    valid_current = filter_whereabouts(whereabouts, target_date, allow_past=False)
    valid_known = filter_whereabouts(whereabouts, target_date, allow_past=True)

    # Get current home as the most recent valid home, or if there are multiple equally recent homes, the last one
    current_home = None
    if len(valid_homes) > 0:
        for home in valid_homes:
            if current_home is None or clean_date(home['start']) > clean_date(current_home['start']):
                current_home = home

