import argparse
import yaml
import re
import os

def getExistYear(metadata):
    # get start year
    
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
        yearStart = int(metadata.get("born"))
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
    
    if yearStart is None: 
        if yearEnd is None: 
            return "unknown age"
        else:
            if yearEnd < currentYear: return endPrefix + " " + str(yearEnd) + ", " + endStatus + " at unknown age"
            return "unknown age"
    else:
        if yearEnd is None:
            if yearStart > currentYear: return preExistError
            age = currentYear - yearStart
            return startPrefix + " " + str(yearStart) + " (" + str(age) + " years old)"
        else:
            if yearStart > yearEnd: return "**(timetraveler, check your YAML)**"
            if yearStart > currentYear: return preExistError
            if yearEnd < currentYear:
                return startPrefix + " " + str(yearStart) + " - " + endPrefix + " " + str(yearEnd) +  ", " + endStatus + " at " + str(yearEnd-yearStart) + " years old"
            return startPrefix + " " + str(yearStart) + " (" + str(currentYear-yearStart) + " years old)"


def process_string(s, metadata):
    def callback(match):
        function_name = match.group(1).split(",", maxsplit=1)[0].strip('\"').split("/")[-1]

        if (function_name == "get_PageDatedValue"):
            return_value = get_PageDatedValue(metadata)
        elif (function_name == "get_RegnalValue"):
            return_value = get_RegnalValue(metadata)
        else:
            print("Function name " + function_name + " not found! Returning ...")
            return_value = "..."
        
        return return_value

    pattern = "\`\$\=dv\.view\((.*)\`"
    return re.sub(pattern, callback, s)

parser = argparse.ArgumentParser()
parser.add_argument('--date', required=True)
parser.add_argument('--dir', required=True)
parser.add_argument('--campaign', required=True)
args = parser.parse_args()

# Get the date, campaign, and directory name from the command line arguments
parse_date = args.date
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

    metadata["curYear"] = parse_date
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
            match = re.search(r'%%\^Date:\s*(\w+)\s*%%', line)
            ## currently we assume that Date and --date arguments are both just plain years
            if match:
                year = match.group(1)
                if int(year) >= int(parse_date):
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
 