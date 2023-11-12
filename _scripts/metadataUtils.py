from datetime import datetime, date
import os
from pathlib import Path
import urllib.parse 
import json
import sys
import re

def loc_join(l):
    if not l:
        return ""
    
    if isinstance(l, str):
        return l

    # Check if the input is a list
    if isinstance(l, list):
        # Process each element in the list
        processed_list = [item if isinstance(item, str) else str(list(item.values())[0]) for item in l if item is not None and item != ""]

        if len(processed_list) == 1:
            return processed_list[0]
        else:
            return ', '.join(processed_list)

    # Return an empty string for other types
    return ""

def get_valid_types(): 
    return(["Ruler", "PC", "NPC", "Item", "Place", "Building", "Event", "Organization", "Session Note"])

def get_tags_to_output():
    return(["sessionStartTime", "sessionEndDate", "sessionEndTime", "summary"])

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
    if (date is None) or (date == ""):
        return None

    if (full):
        return date.strftime("%b %d, %Y")
    else:
        return cr + " " + date.strftime("%Y")

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
    died_date = clean_date(metadata["died"]) if "died" in metadata else None
    if died_date is not None:
        target_date = died_date

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

    """
    # if you are dead, current location should never be output
    if died_date is not None and target_date > died_date:
        locations["current"]["output"] = False
    
    """


    if debug:
        print(metadata["name"], locations, file=sys.stderr)

    return locations

def define_metadata(type): 

    ## creates a blank metadata dictionary with all valid fields

    valid_types = get_valid_types()

    metadata_core = {
        'type' : None, 
        'name' : None,
        'pronouciation' : None, 
        'aliases' : [],
        'tags' : [],
        'pageTargetDate' : None,
        'endStatus' : None,
        'endPrefix' : None,
        'startStatus': None,
        'startPrefix' : None,
        'preExistError': None
    }

    metadata_people = {
        'title' : None,
        'born' : None,
        'ka' : None,
        'died' : None,
        'gender' : None,
        'pronouns' : None,
        'ancestry' : None,
        'species' : None,
        'affiliations' : [],
        'family' : None,
        'whereabouts' : [],
        'lastSeenByParty' : []
    }

    metadata_ruler = {
        'reignStart' : None,
        'reignEnd' : None
    }

    metadata_pc = {
        'player' : None,
        'ddbLink' : None
    }

    metadata_place = {
        'created' : None,
        'destroyed' : None,
        'location' : None,
        'population' : None,
        'politicalUnit' : None
    }

    metadata_item = {
        'created' : None,
        'destroyed' : None,
        'magical' : None,
        'maker' : None,
        'owner' : None,
        'ddbLink' : None
    }

    metadata_building = {
        'created' : None,
        'destroyed' : None,
        'owner' : None,
        'place' : None
    }

    metadata_dates = {
        'DR' : None,
        'DR_end' : None,
        'fc-date' : None,
        'fc-end' : None,
        'fc-display-name' : None
    }

    metadata_session = {
        'sessionNumber' : None,
        'realWorldDate' : None,
        'players' : [],
        'campaign' : None
    }

    metadata_other = {
        'speciesDescriptor' : None,
        'cultureDescriptor' : None
    }

    metadata_organization = {
        'created' : None,
        'destroyed' : None
    }

    # construct metadata by type

    # ["Ruler", "PC", "NPC", "Item", "Place", "Building", "Event", "Organization", "Session Note"]
    if type in valid_types:
        if type == "Ruler":
            metadata = {**metadata_core, **metadata_people, **metadata_ruler}
        elif type=="PC":
            metadata = {**metadata_core, **metadata_people, **metadata_pc}
        elif type=="NPC":
            metadata = {**metadata_core, **metadata_people}
        elif type=="Item":
            metadata = {**metadata_core, **metadata_item}
        elif type=="Place":
            metadata = {**metadata_core, **metadata_place}
        elif type=="Building":
            metadata = {**metadata_core, **metadata_building}
        elif type=="Event":
            metadata = {**metadata_core, **metadata_dates}
        elif type=="Organization":
            metadata = {**metadata_core, **metadata_organization}
        elif type=="Session Note":
            metadata = {**metadata_core, **metadata_session, **metadata_dates}
    else:
        metadata = {**metadata_core, **metadata_dates, **metadata_other}
    
    ## sets default values for metadata fields based on type

    if type in valid_types:
        if type == "Ruler" or type == "PC" or type == "NPC":
            metadata["endStatus"] = "died"
            metadata["endPrefix"] = "d."
            metadata["startStatus"] = "born"
            metadata["startPrefix"] = "b."
            metadata["preExistError"] = "**(not yet born)**"
        elif type=="Organization":
            metadata["endStatus"] = "disbanded"
            metadata["endPrefix"] = "d."
            metadata["startStatus"] = "founded"
            metadata["startPrefix"] = "f."
            metadata["preExistError"] = "**(not yet founded)**"
        elif type=="Item":
            metadata["endStatus"] = "destroyed"
            metadata["endPrefix"] = "d."
            metadata["startStatus"] = "created"
            metadata["startPrefix"] = "c."
            metadata["preExistError"] = "**(not yet created)**"
        elif type=="Place":
            metadata["endStatus"] = "destroyed"
            metadata["endPrefix"] = "d."
            metadata["startStatus"] = "founded"
            metadata["startPrefix"] = "f."
            metadata["preExistError"] = "**(not yet created)**"
        elif type=="Building":
            metadata["endStatus"] = "destroyed"
            metadata["endPrefix"] = "d."
            metadata["startStatus"] = "built"
            metadata["startPrefix"] = "b."
            metadata["preExistError"] = "**(not yet created)**"
        elif type=="Event":
            metadata["endStatus"] = "ended"
            metadata["endPrefix"] = ""
            metadata["startStatus"] = "started"
            metadata["startPrefix"] = ""
            metadata["preExistError"] = "**(has not happened)**"
        elif type=="Session Note":
            metadata["endStatus"] = "ended"
            metadata["endPrefix"] = ""
            metadata["startStatus"] = "started"
            metadata["startPrefix"] = ""
            metadata["preExistError"] = "**(has not happened)**"
    else:
            metadata["endStatus"] = "ended"
            metadata["endPrefix"] = ""
            metadata["startStatus"] = "started"
            metadata["startPrefix"] = ""
            metadata["preExistError"] = "**(doesn't exist)**"
    
    # return blank metadata

    return metadata

def guess_type(file):
    # NOT IMPLEMENTED
    return None

def update_metadata(metadata, metadata_orig, guess_type=False):

    # takes as input an metadata dictionary, and returns an updated metadata dictionary according to the speck
    # if guess_type is true, attempts to guess the type based on path

    type = metadata["type"] if "type" in metadata else None
    valid_types = get_valid_types()

    if guess_type and type is None:
        type = guess_type(metadata["file"])
    
    type = "" if type is None else type
    
    metadata_default = define_metadata(type)

    if type not in valid_types:
        return(metadata_orig)

    # for each key in metadata_default, check to see if key exists in metadata. if yes, take value. else, use default or leave blank

    metadata_fixed = dict()

    for key in metadata_default:
        if key in metadata and metadata[key] is not None:
            metadata_fixed[key] = metadata[key]
        else:
            metadata_fixed[key] = metadata_default[key]
    
    # special cleanup for whereabouts

    ## if we have old home, origin, location tags, convert those to whereabouts; location tags get current date
    ## if we have whereabouts, check each entry and fix up, but return in same order

    ## procedure is: first check for whereabouts in fixed, and clean up
    ## then add additional whereabouts lines as needed from home, origin, location, tags
    
    if "whereabouts" in metadata_fixed:
        #we have whereabouts
        #get born date to remove from start if needed
        born = clean_date(metadata_fixed["born"]) if "born" in metadata_fixed else None
        metadata_fixed["whereabouts"] = clean_whereabouts(metadata_fixed["whereabouts"],born)
    
    if ("origin" in metadata and metadata["origin"]) or ("originRegion" in metadata and metadata["originRegion"]): 
        place = metadata["origin"] if "origin" in metadata else None
        region = metadata["originRegion"] if "originRegion" in metadata else None
        new_home = {'type': "home", 'start': "", 'end': "", 'location': loc_join([place,region])}
        metadata_fixed["whereabouts"].append(new_home)

    if ("home" in metadata and metadata["home"]) or ("homeRegion" in metadata and metadata["homeRegion"]): 
        place = metadata["home"] if "home" in metadata else None
        region = metadata["homeRegion"] if "homeRegion" in metadata else None
        new_home = {'type': "home", 'start': "", 'end': "", 'location': loc_join([place,region])}
        metadata_fixed["whereabouts"].append(new_home)
    
    if ("location" in metadata and metadata["location"]) or ("locationRegion" in metadata and metadata["locationRegion"]): 
        place = metadata["location"] if "location" in metadata else None
        region = metadata["locationRegion"] if "locationRegion" in metadata else None
        date=display_date(get_current_date(metadata))
        new_loc = {'type': "away", 'start': date, 'end': "", 'location': loc_join([place,region])}
        metadata_fixed["whereabouts"].append(new_loc)

    ## update obselete tags

    # yearOverride - replaced by pageTargetDate

    metadata_fixed["pageTargetDate"] = metadata["yearOverride"] if "yearOverride" in metadata else metadata_fixed["pageTargetDate"]
    
    # campaign - replaced by affiliations
    # Assuming 'type' is a variable you've defined earlier
    if type == "PC" and "campaign" in metadata:
        # Initialize metadata_fixed["affiliations"] as a list if it doesn't exist or is None
        if "affiliations" not in metadata_fixed or metadata_fixed["affiliations"] is None:
            metadata_fixed["affiliations"] = []

        # Now safely append to metadata_fixed["affiliations"]
        metadata_fixed["affiliations"].append(metadata["campaign"])
    
    # home, homeRegion, location, locationRegion, origin, originRegion - replaced by whereabouts, seea bove

    # realDate: replaced with realWorldDate
    if "realWorldDate" in metadata_fixed:
        metadata_fixed["realWorldDate"] = metadata["realDate"] if "realDate" in metadata else metadata_fixed["realWorldDate"]
    
    # taelgar-date: replaced with DR
    # taelgar-date-end: replaced with DR_end
    # DR-end replaced with DR_end

    if "DR" in metadata_fixed:
        metadata_fixed["DR"] = metadata["taelgar-date"] if "taelgar-date" in metadata else metadata_fixed["DR"]
    if "DR_end" in metadata_fixed:
        metadata_fixed["DR_end"] = metadata["taelgar-date-end"] if "taelgar-date-end" in metadata else metadata_fixed["DR_end"]
        metadata_fixed["DR_end"] = metadata["DR-end"] if "DR-end" in metadata else metadata_fixed["DR_end"]

    # currentOwner: replaced with owner

    if "owner" in metadata_fixed:
        metadata_fixed["owner"] = metadata["currentOwner"] if "currentOwner" in metadata else metadata_fixed["owner"]
    
    # dbbLink: replace with ddbLink (d d beyond link)
    if "ddbLink" in metadata_fixed:
        metadata_fixed["ddbLink"] = metadata["dbbLink"] if "dbbLink" in metadata else metadata_fixed["ddbLink"]

    # tag: typo for tags; replace with tags
    if "tag" in metadata:
        metadata_fixed["tags"].append(metadata["tag"])

    if "created" in metadata_fixed:
        metadata_fixed["created"] = metadata["built"] if "built" in metadata else metadata_fixed["created"]

    return(metadata_fixed)

def clean_whereabouts(whereabouts, born):

    whereabouts_clean = []

    for loc in whereabouts:
        if "start" in loc:
            start = loc["start"]
        elif "date" in loc:
            start = loc["date"]
        else:
            start = ""

        if "end" in loc:
            end = loc["end"]
        else:
            end = ""
        
        if "location" in loc:
            location = loc["location"]
        elif "place" in loc or "region" in loc:
            place = loc["place"] if "place" in loc else None
            region = loc["region"] if "region" in loc else None
            location = loc_join([place, region])
        else:
            location = ""
        
        if "type" in loc:
            type = loc["type"]
            if type == "home" or type == "origin":
                type = "home"
            else:
                type = "away"
        else:
            type = "away"
    
        #check start date
        if display_date(clean_date(start),full=True) == display_date(clean_date(born),full=True):
            start = ""

        new_loc = {"type": type, "start": start, "end": end, "location": location}
        whereabouts_clean.append(new_loc)

    return whereabouts_clean
