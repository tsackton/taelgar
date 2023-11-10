from datetime import datetime
import os
from pathlib import Path
import urllib.parse 
import json
import re

def get_link(string, metadata):
    links = metadata["links"]
    file = metadata["file"]
    if string in links:
        dest = links[string]
        orig = links[Path(file).stem].parent
        linkpath = os.path.relpath(dest,orig)
        return "[" + string + "](" + urllib.parse.quote(linkpath) + ")"
    else:
        return string

def get_current_date(metadata):
    directory = metadata["configDir"]
    if metadata["pageTargetDate"] is not None:
        return clean_date(metadata["pageTargetDate"])
    if metadata["override_year"] is not None:
        return clean_date(metadata["override_year"])
    with open(os.path.join(directory, 'plugins', 'fantasy-calendar', 'data.json'), 'r', 2048, "utf-8") as f:
        data = json.load(f)
        current_data_string = data['calendars'][0]['current']['year'] + "-" + data['calendars'][0]['current']['month'] + "-" + data['calendars'][0]['current']['day']
        return clean_date(current_data_string)

def clean_date(value, end = False):
    # If the value is already a datetime object, return it as is
    if isinstance(value, datetime):
        return value

    if isinstance(value, int):
        # Assuming the integer is a year
        if (end):
            return datetime(value, 12, 31)
        else:
            return datetime(value, 1, 1)

    if isinstance(value, str):

        def sanitize(input_string):
            return re.sub(r'\D', '', input_string)

        parts = value.split('-')

        year = int(sanitize(parts[0]))
        if len(parts) == 1: 
            if (end):
                return datetime(year, 12, 31)
            else:
                return datetime(year, 1, 1)
        elif len(parts) == 2:
            if (end): 
                return datetime(year, int(sanitize(parts[1])), 31)
            else:
                return datetime(year, int(sanitize(parts[1])), 1)
        elif len(parts) == 3:
            return datetime(year, int(sanitize(parts[1])), int(sanitize(parts[2])))
        else:
            raise ValueError("Input must be a datetime object, an integer, or a string in YYYY, YYYY-MM, or YYYY-MM-DD format.")
        
    raise ValueError("Input must be a datetime object, an integer, or a string in YYYY, YYYY-MM, or YYYY-MM-DD format.")

def display_date(date, full = True, cr = "DR"):
    if (full):
        return date.strftime("%b %d, %Y")
    else:
        return cr + date.strftime("%Y")

def get_Age(younger, older):
    younger = clean_date(younger)
    older = clean_date(older)
    return younger.year - older.year - ((younger.month, younger.day) < (older.month, older.day))


def parse_loc_string(string, metadata):
    pieces = string.split(",")
    for piece in pieces:
        piece = piece.strip()
        piece = get_link(piece, metadata)
    return ", ".join(pieces)
