import argparse
import yaml
import re
import os
import sys
import json
from pathlib import Path
import datetime
import urllib.parse 

def get_links_dict(files):
    links = {}
    for file in files:
        filepath = Path(file)
        links[filepath.stem] = filepath
    return links

def get_link(string, file, links):
    if string in links:
        dest = links[string]
        orig = links[Path(file).stem].parent
        linkpath = os.path.relpath(dest,orig)
        return "[" + string + "](" + urllib.parse.quote(linkpath) + ")"
    else:
        return string

def get_currentFantasyDate(directory):    
    with open(os.path.join(directory, 'plugins', 'fantasy-calendar', 'data.json'), 'r', 2048, "utf-8") as f:
        data = json.load(f)
        return data['calendars'][0]['current']['year']

def get_Existence(metadata):
    # get start year
    
    yearStart = None

    if metadata.get("type") == "NPC":
        yearStart = metadata.get("born")
    elif metadata.get("type") == "Ruler":
        yearStart = metadata.get("born")
    elif metadata.get("type") == "Building":
        yearStart = metadata.get("built")
    elif metadata.get("type") == "Item":
        yearStart = metadata.get("created")

    if yearStart and (yearStart > int(metadata["curYear"])):
        return False
    else:
        return True

def get_md_files(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        markdown_files += [os.path.join(root, file) for file in files if file.endswith('.md')]
    return markdown_files

def get_RegnalValue(metadata):
    
    currentYear = int(metadata["curYear"])

    yearStart = metadata.get("reignStart")
    yearEnd = metadata.get("reignEnd")
    
    if yearEnd == None: yearEnd = metadata.get("died")
    
    if yearStart is None: 
        return ""
    else:
        if (yearEnd is None) or (yearEnd is not None and yearEnd >= currentYear):
            reignLength = currentYear - yearStart
            return "reigning since " + str(yearStart) + " (" + str(reignLength) + " years)"
        else:
            if yearStart and yearEnd and yearStart > yearEnd: return "**(timetraveler, check your YAML)**"
            if yearStart > currentYear: return ""
    
    return "reigned " + str(yearStart) + " - " + str(yearEnd) + " (" + str(yearEnd-yearStart) + " years)"

def get_PageDatedValue(metadata):

    currentYear = int(metadata["curYear"])

    if metadata.get("type") == "NPC":
        yearStart = metadata.get("born")
        yearEnd = metadata.get("died")
        preExistError = metadata.get("preExistError", "**(not yet born)**")
        startPrefix = metadata.get("startPrefix", "b.")
        endPrefix = metadata.get("endPrefix", "d.")
        endStatus = metadata.get("endStatus", "died")
    elif metadata.get("type") == "Ruler":
        yearStart = metadata.get("born")
        yearEnd = metadata.get("died")
        preExistError = metadata.get("preExistError", "**(not yet born)**")
        startPrefix = metadata.get("startPrefix", "b.")
        endPrefix = metadata.get("endPrefix", "d.")
        endStatus = metadata.get("endStatus", "died")
    elif metadata.get("type") == "Building":
        yearStart = metadata.get("built")
        yearEnd = metadata.get("destroyed")
        preExistError = metadata.get("preExistError", "**(not yet built)**")
        startPrefix = metadata.get("startPrefix", "built")
        endPrefix = metadata.get("endPrefix", "destroyed")
        endStatus = metadata.get("endStatus", "destroyed")
    elif metadata.get("type") == "Item":
        yearStart = metadata.get("created")
        yearEnd = metadata.get("destroyed")
        preExistError = metadata.get("preExistError", "**(not yet created)**")
        startPrefix = metadata.get("startPrefix", "created")
        endPrefix = metadata.get("endPrefix", "destroyed")
        endStatus = metadata.get("endStatus", "destroyed")
    else: 
        yearStart = None
        yearEnd = None
    
    if yearStart is None: 
        if yearEnd is None: 
            return "unknown age"
        else:
            if yearEnd <= currentYear: return endPrefix + " " + str(yearEnd) + ", " + endStatus + " at unknown age"
            return "unknown age"
    else:
        if yearEnd is None:
            if yearStart > currentYear: return preExistError
            age = currentYear - yearStart
            return startPrefix + " " + str(yearStart) + " (" + str(age) + " years old)"
        else:
            if yearStart > yearEnd: return "**(timetraveler, check your YAML)**"
            if yearStart > currentYear: return preExistError
            if yearEnd <= currentYear:
                return startPrefix + " " + str(yearStart) + " - " + endPrefix + " " + str(yearEnd) +  ", " + endStatus + " at " + str(yearEnd-yearStart) + " years old"
            return startPrefix + " " + str(yearStart) + " (" + str(currentYear-yearStart) + " years old)"

def get_HomeWhereabouts(metadata,file_name,links):
    cur_year = datetime.date(int(metadata["curYear"]),1,1)
    
    if "whereabouts" not in metadata:
        return ""
    
    home_whereabouts = [w for w in metadata["whereabouts"] if w["type"] == "home" and w.get("date",datetime.date(1,1,1)) <= cur_year]
    if home_whereabouts:
        most_recent_home = max(home_whereabouts, key=lambda x: x.get("date",datetime.date(1,1,1)))
        home =  most_recent_home["place"] + ","  + most_recent_home["region"]
        home_parts =  [x.strip() for x in home.split(',')]
        home_text = [get_link(x,file_name,links) for x in home_parts]
        return "Based in: " + ", ".join(home_text)
    else:
        return ""


def process_string(s, metadata, file_name, links):
    def callback(match):
        function_name = match.group(1).split(",", maxsplit=1)[0].strip('\"').split("/")[-1]

        if (function_name == "get_PageDatedValue"):
            return_value = get_PageDatedValue(metadata)
        elif (function_name == "get_HomeWhereabouts"):
            return_value = get_HomeWhereabouts(metadata, file_name, links)
        elif (function_name == "get_RegnalValue"):
            return_value = get_RegnalValue(metadata)
        elif (function_name == "get_CurrentWhereabouts"):
            return_value = ""     
        elif (function_name == "get_Whereabouts"):
            return_value = ""             
        else:
            print("Function name " + function_name + " not found in " + file_name, file=sys.stderr)
            return_value = ""
        
        return return_value

    pattern = "\`\$\=dv\.view\((.*)\)\`"
    return re.sub(pattern, callback, s)

parser = argparse.ArgumentParser()
parser.add_argument('--date', required=False)
parser.add_argument('--dir', required=True)
parser.add_argument('--campaign', required=False)
parser.add_argument('--configDir', required=False)
args = parser.parse_args()

# Get the date, campaign, and directory name from the command line arguments
if (args.date):
    input_date = args.date.split("-")[0]
elif (args.configDir):
    input_date = get_currentFantasyDate(args.configDir)
else:
    print("Error: Requires either a configDir or an input date")
    exit

dir_name = args.dir
input_campaign = args.campaign
md_file_list = get_md_files(dir_name)
links = get_links_dict(md_file_list)

print("Using year:", input_date)

for file_name in md_file_list:
    # Open the input file
    with open(file_name, 'r', 2048, "utf-8") as input_file:
        lines = input_file.readlines()

    # if file is blank, move on
    if len(lines) == 0:
        continue

    # Check if the file starts with a metadata block
    metadata = dict()
    if lines[0].strip() == '---':
        metadata_block = []
        start_metadata = True
        for line in lines[1:]:
            if start_metadata and line.strip() == '---':
                start_metadata = False
            elif start_metadata:
                metadata_block.append(line)
            else:
                break
        if metadata_block:
            metadata = yaml.safe_load(''.join(metadata_block))

    metadata["curYear"] = input_date if "yearOverride" not in metadata or metadata["yearOverride"] is None else metadata["yearOverride"]
    metadata["campaign"] = input_campaign
    thing_exist = get_Existence(metadata)

    #Process the rest of the file with access to the metadata information
    filter_start = False
    filter_end = False
    filter_block = False
    newlines = []
    for line in lines:
        filter_start = line.startswith(("%%^", ">%%^", ">>%%^", ">>>%%^"))
        line_start = ""
        filter_end = line.endswith(("%%^End%%\n","%%^End%%"))

        # check if line is just %%^End%%
        if line.startswith("%%^End"):
            filter_start = False

        # get filter type if filter start
        if filter_start:
            match = re.search(r'^(.*?)%%\^([A-Za-z]+):\s*(\w+).*?\s*%%', line)
            if match:
                if match.group(2) == "Date":
                    # we have a date filter
                    filter_block = True if int(metadata["curYear"]) < int(match.group(3)) else filter_block
                elif match.group(2) == "Campaign":
                    # we have a campaign filter
                    filter_block = True if metadata["campaign"] != match.group(3) else filter_block
                else:    
                    # filter we don't know
                    print("Found unknown filter in file " + file_name + ": " + match.group(2), file=sys.stderr)
                line_start = match.group(1)
            else:
                print("In file " + file_name + ", couldn't parse filter at line: " + line, end="", file=sys.stderr)
        
        if not filter_block:
            # if filter block is False, we should print the line
            newline = process_string(line,metadata,file_name,links)
            newlines.append(newline)
        
        # now need to check filter_end and reset filter_block if we are at the end

        if filter_end:
            filter_block = False

    # Write the updated lines to a new file
    with open(file_name, 'w', 2048, "utf-8") as output_file:
        if not thing_exist:
            newlines = metadata_block
            newlines.append("# " + metadata.get("name", "unnamed entity") + "\n")
            newlines.append("**This does not exist yet!**\n")

        output_file.writelines(newlines)
 