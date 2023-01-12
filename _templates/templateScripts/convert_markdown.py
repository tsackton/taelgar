import argparse
import yaml
import re
import warnings
import json
import os

def getExistYear(metadata):
    # get start year
    
    if "born" in metadata:
        year_start = int(metadata["born"])
    elif "built" in metadata:
        year_start = int(metadata["built"])
    elif "created" in metadata:
        year_start = int(metadata["created"])
    else:
        year_start = None

    if year_start and (year_start > int(metadata["curYear"])):
        return False
    else:
        return True

def get_md_files(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        markdown_files += [os.path.join(root, file) for file in files if file.endswith('.md')]
    return markdown_files

def getAgeBasedValue(metadata, strings):

    ## get strings

    if strings is None:
        pre_exist_error = "(not yet born)"
        start_prefix = "b."
        end_prefix = "d."
    else:
        strings = json.loads(strings)
        pre_exist_error = strings.get("preExistError", "(not yet born)")
        start_prefix = strings.get("startPrefix", "b.")
        end_prefix = strings.get("endPrefix", "d.")
    
    # get start year
    if "born" in metadata:
        year_start = metadata["born"]
    elif "built" in metadata:
        year_start = metadata["built"]
    elif "created" in metadata:
        year_start = metadata["created"]
    else:
        year_start = None
    
    # get end year
    if "died" in metadata:
        year_end = metadata["died"]
    elif "destroyed" in metadata:
        year_end = metadata["destroyed"]
    else:
        year_end = None
    
    # get current year
    current_year = metadata.get("yearOverride", None)
    if current_year is None:
        current_year = int(metadata["curYear"])
    
    # process
    if not year_start and not year_end:
        return ""
    if year_start and year_end and year_start > year_end:
        return "(timetraveler, check your YAML)"
    if year_start and not year_end:
        if year_start > current_year:
            return pre_exist_error
        age = current_year - year_start
        return start_prefix + " " + str(year_start) + " (" + str(age) + " years old)"
    if year_end and not year_start:
        if year_end < current_year:
            return end_prefix + " " + str(year_end)
        return ""
    if year_start > current_year:
        return pre_exist_error
    if year_end < current_year:
        return (
            start_prefix
            + " "
            + str(year_start)
            + " - "
            + end_prefix
            + " "
            + str(year_end)
            + " at age "
            + str(year_end - year_start)
        )
    return start_prefix + " " + str(year_start) + " (" + str(current_year - year_start) + " years old)"

def getCampaignBasedValue(metadata, frontmatterItem):
    
    keyToGet = frontmatterItem.replace('"', '')
    campaignValue = metadata["campaign"]
    campaignKey = keyToGet.strip() + "_" + campaignValue
    if campaignKey in metadata:
        return str(metadata[campaignKey])
    else:
        return str(metadata[keyToGet.strip()])

def getRegnalValue(metadata):
        
    yearStart = metadata.get("reignStart", None)
    if "reignEnd" in metadata:
        yearEnd = metadata["reignEnd"]
    elif "died" in metadata:
        yearEnd = metadata["died"]
    else:
        yearEnd = None
   
    # get current year
    currentYear = metadata.get("yearOverride", None)
    if currentYear is None:
        currentYear = int(metadata["curYear"])
    
    if not yearStart:
        return ""

    if yearStart and yearEnd and (yearStart > yearEnd):
        return "(timetraveler, check your YAML)"

    if yearStart > currentYear:
        return ""
        
    if not yearEnd or (yearEnd >= currentYear):              
        reignLength = currentYear - yearStart
        return "reigning since " + str(yearStart) + " (" + str(reignLength) + " years)"

    return "reigned " + str(yearStart) + " - " + str(yearEnd) + " (" + str(yearEnd-yearStart) + " years)"

def process_string(s, metadata):
    def callback(match):
        function_name = match.group(1)
        arguments = match.group(2).split(",", maxsplit=1)

        if (function_name == "getAgeBasedValue"):
            if len(arguments) > 1:
                argValue = arguments[1]
            else:
                argValue = None
            return_value = getAgeBasedValue(metadata, argValue)
        elif (function_name == "getCampaignBasedValue"):
            return_value = getCampaignBasedValue(metadata, arguments[1])
        elif (function_name == "getRegnalValue"):
            return_value = getRegnalValue(metadata)
        else:
            warnings.warn("Function name " + function_name + " not found! Returning unmodified text")
            return_value = "<%+ tp.user." + function_name + "(" + ",".join(arguments) + ") %>"
        
        return return_value

    pattern = "<\%\+\s+tp\.user\.([A-Za-z]*)\((.*)\)\s+\%>"
    return re.sub(pattern, callback, s)

parser = argparse.ArgumentParser()
parser.add_argument('--date', required=True)
parser.add_argument('--dir', required=True)
parser.add_argument('--campaign', required=True)
args = parser.parse_args()

# Get the date, campaign, and file name from the command line arguments
date = args.date
dir_name = args.dir
campaign = args.campaign

for file_name in get_md_files(dir_name):
    # Open the input file
    with open(file_name, 'r') as input_file:
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

    metadata["curYear"] = date
    metadata["campaign"] = campaign
    existYear = getExistYear(metadata)

    #Process the rest of the file with access to the metadata information
    date_block = False
    newlines = []
    for line in lines:
        if date_block:
            if "%%^End%%" in line:
                date_block = False
            continue
        elif line.startswith("%%^Date:"):
            date_block = True
            match = re.search(r'%%\^Date:(\S+)%%', line)
            ## currently we assume that Date and --date arguments are both just plain years
            if match:
                year = match.group(1)
                if int(year) >= int(date):
                    continue
        
        # find templater functions
        # we don't care about templater functions in date blocks
        newline = process_string(line,metadata)
        newlines.append(newline)

    # Write the updated lines to a new file
    with open(file_name, 'w') as output_file:
        if not existYear:
            newlines = metadata_block
            newlines.append("# " + metadata.get("name", "unnamed entity") + "\n")
            newlines.append("**This does not exist yet!**\n")

        output_file.writelines(newlines)
 