from datetime import datetime, date
import os
from pathlib import Path
import urllib.parse 
import json
import sys
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
    directory = metadata["directory"]
    target_date = metadata.get("pageTargetDate", None)
    if target_date is not None:
        return clean_date(metadata["pageTargetDate"])
    if metadata["override_year"] is not None:
        return clean_date(metadata["override_year"])
    with open(os.path.join(directory, 'plugins', 'fantasy-calendar', 'data.json'), 'r', 2048, "utf-8") as f:
        data = json.load(f)
        current_data_string = str(data['calendars'][0]['current']['year']) + "-" + str(data['calendars'][0]['current']['month']+1) + "-" + str(data['calendars'][0]['current']['day'])
        return clean_date(current_data_string)

def clean_date(value, end = False, debug = False):

    def sanitize(input_string):
        return re.sub(r'\D', '', input_string)

    if debug:
        print(value, type(value), file=sys.stderr)

    # If value is None, return None
    if value is None or not value:
        return None

    if isinstance(value, datetime):
        return date(value.year, value.month, value.day)
    
    # If the value is already a datetime object, return it as is
    if isinstance(value, date):
        return value

    if isinstance(value, int):
        # Assuming the integer is a year
        if (end):
            return date(value, 12, 31)
        else:
            return date(value, 1, 1)

    if isinstance(value, str):

        parts = value.split('-')

        year = int(sanitize(parts[0]))
        if len(parts) == 1: 
            if (end):
                return date(year, 12, 31)
            else:
                return date(year, 1, 1)
        elif len(parts) == 2:
            if (end): 
                return date(year, int(sanitize(parts[1])), 31)
            else:
                return date(year, int(sanitize(parts[1])), 1)
        elif len(parts) == 3:
            return date(year, int(sanitize(parts[1])), int(sanitize(parts[2])))
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

def get_page_start_date(metadata):
    pageStartDate = clean_date(metadata["created"]) if "created" in metadata else None
    if "type" in metadata and metadata["type"] in ["NPC", "PC", "Ruler"]:
        pageStartDate = clean_date(metadata["born"]) if "born" in metadata else pageStartDate
    return pageStartDate

def get_page_end_date(metadata):
    pageEndDate = clean_date(metadata["destroyed"], end=True) if "destroyed" in metadata else None
    if "type" in metadata and metadata["type"] in ["NPC", "PC", "Ruler"]:
        pageEndDate = clean_date(metadata["died"], end=True) if "died" in metadata else pageEndDate
    return pageEndDate

def parse_whereabouts(metadata, debug = False):

    whereabouts = metadata["whereabouts"]
    target_date = get_current_date(metadata)
    locations = {"exact": {}, "home": {}, "origin": {}, "last": {}, "current": {}}

    locations["exact"]["value"] = None
    locations["exact"]["output"] = False
    locations["exact"]["date"] = None
    locations["exact"]["duration"] = None
    locations["home"]["value"] = None
    locations["home"]["output"] = False
    locations["home"]["date"] = None
    locations["home"]["duration"] = None
    locations["origin"]["value"] = None
    locations["origin"]["output"] = False
    locations["origin"]["date"] = None
    locations["origin"]["duration"] = None
    locations["last"]["value"] = None
    locations["last"]["output"] = False
    locations["last"]["date"] = None
    locations["last"]["duration"] = None
    locations["last"]["end"] = None
    locations["current"]["value"] = None
    locations["current"]["output"] = False
    locations["current"]["date"] = None
    locations["current"]["duration"] = None

    home_count = 0 

    for whereabout in whereabouts:
        ## define variables ##

        # a logical end date is the start date if the end date is undefined, otherwise the start date
        start = clean_date(whereabout["start"]) if "start" in whereabout else None
        end = clean_date(whereabout["end"], end=True) if "end" in whereabout else None
        logical_end = end if end is not None else start
        type = whereabout["type"] if whereabout["type"] is not None else None
        if type is None:
            raise ValueError("Whereabouts must have a type")
        elif type == "away" and start is None:
            raise ValueError("Away whereabouts must have a start date")
        
        type = "home" if type == "origin" else type #clean up old origin type, which is now home

        # a location is constructed from the location , place, and region fields
        # location field is preferred if multiple fields exist
        location = whereabout["location"] if "location" in whereabout else None
        place = whereabout["place"] if "place" in whereabout else None
        region = whereabout["region"] if "region" in whereabout else None
        value = location if location is not None else ",".join([place, region])
        if value is None:
            value = "Unknown"
        
        home_count = home_count + 1 if type == "home" else home_count
        
        # Find the "exact known whereabouts".
        # Candidate set = Take all of the whereabouts with type = away
        # Start is defined and before or equal to target date
        # Logical end is after or equal to target date
        # If there are multiple items in the candidate set, select the one with the smallest duration between the logic end date and the start date
        # If there are no items, the "exact known whereabouts" is undefined

        if type == "away" and start is not None and start <= target_date and (logical_end >= target_date):
            if locations["exact"]["value"] is None or (logical_end - start) < locations["exact"]["duration"]:
                locations["exact"]["value"] = value
                locations["exact"]["date"] = target_date
                locations["exact"]["duration"] = logical_end - start
                locations["exact"]["output"] = True
    
        # Find the "home whereabouts".
        # Candidate set = Take all of the whereabouts with type = home
        # Start is unset or before or equal to target date and end (not logical end) is after or equal to target date
        # Start is unset or before or equal to target date and end is unset
        # If there are multiples reduce the set to all of the items with the latest start date that is before the target date. 
        # An unset start date should be treated as the earliest possible date
        # If there are still multiples (because multiple items have the same or blank start date), take the one that is lexically last in the yaml
        # If there are no items, the "home whereabouts" is undefined

        if type == "home" and ((start is None or start <= target_date) and (end is None or end >= target_date)):
            home_implied_start = start if start is not None else clean_date(int(1))
            # if we don't have a home, set one
            if locations["home"]["value"] is None:
                locations["home"]["value"] = value
                locations["home"]["date"] = home_implied_start
                locations["home"]["output"] = True
            # if we have a home, skip if the start is earlier than the current home
            elif home_implied_start < locations["home"]["date"]:
                continue
            # we have a home, but we've encountered a new home listed later in the yaml
            # or a new home with a later date
            # replace old home with new home
            else: 
                locations["home"]["value"] = value
                locations["home"]["date"] = home_implied_start
                locations["home"]["output"] = True
        
        # Find the "last known whereabout"
        # Candidate set = Take all of the whereabouts where type = away
        # Start is before or equal to target
        # If there are multiples, take start date that is closest to the target date

        if type == "away" and start is not None and start <= target_date:
            if locations["last"]["value"] is None or start > locations["last"]["date"]:
                locations["last"]["value"] = value
                locations["last"]["date"] = start
                locations["last"]["output"] = True
                locations["last"]["end"] = end
        
        # Find the "origin whereabout"
        # Candidate set = Take all of the whereabouts where type = home and start = undefined
        # If there are multiples, select the lexically first one in the yaml
        if type == "home" and start is None:
            if locations["origin"]["value"] is None:
                locations["origin"]["value"] = value
                locations["origin"]["output"] = True
    
    # clean up output flags
    # An origin location is defined as
    # Value: the origin whereabout
    # Output: origin whereabout is defined and whereabouts with type home > 1 or the origin whereabout is defined and there is no home whereabout

    # if home_count == 1:
    # home = True and origin = False if home value is defined, otherwise origin = True and home = False
    # logic is if home_count == 1, should always just output home unless home has an end date, implying no current home
    # by definition if home_count == 1, origin and home must have the same value if both defined, so don't need to check
    # if home_count > 1, we need to check if home and origin have the same value. 
    # if they have the same value, that means the only valid home is the origin, so we output origin True and home True but set home value to "Unknown"

    if home_count == 0:
        locations["origin"]["output"] = False
        locations["home"]["output"] = False
    elif home_count == 1:
        locations["origin"]["output"] = False
        locations["home"]["output"] = True
        if locations["home"]["value"] is None or locations["home"]["value"] == "Unknown":
            locations["home"]["output"] = False
            locations["origin"]["output"] = True
    else:
        locations["home"]["output"] = True
        locations["origin"]["output"] = True
        if locations["home"]["value"] == locations["origin"]["value"]:
            locations["home"]["value"] = "Unknown"
            locations["home"]["output"] = False

    # A current location is defined as
    # Value:
    # If there is an exact known whereabouts, use that and set the output flag to true
    # Otherwise, if there is both a home and last known whereabouts where
    # The last known whereabouts has a defined end and
    # The last known whereabouts end date is in the past compared to the target date
    # Then use the home whereabout as the current location and set the output flag to false
    # Otherwise, the current location is Unknown and set the output flag to true
    # Output: See algorithm above

    if locations["exact"]["value"] is not None:
        locations["current"]["value"] = locations["exact"]["value"]
        locations["current"]["output"] = True
    elif locations["home"]["value"] is not None:
        if locations["last"]["end"] is not None and locations["last"]["end"] < target_date:
            locations["current"]["value"] = locations["home"]["value"]
            locations["current"]["output"] = False
        elif locations["last"]["value"] is None:
            locations["current"]["value"] = locations["home"]["value"]
            locations["current"]["output"] = False
        else:
            locations["current"]["value"] = "Unknown"
            locations["current"]["output"] = True
    else:
        locations["current"]["value"] = "Unknown"
        locations["current"]["output"] = True

    # a last known location is defined as
    # Value: the last known whereabouts
    # Output: the last known whereabouts is defined and the current location is Unknown
    # Date: the last known whereabouts date
    if locations["current"]["value"] == "Unknown" and locations["last"]["value"] is not None:
        locations["last"]["output"] = True
    else:
        locations["last"]["output"] = False

    if debug:
        print(metadata["name"], locations, file=sys.stderr)

    return locations

