import argparse
import yaml
import re
import os
import sys
from pathlib import Path
from metadataUtils import *
import importlib.util

## import dview_functions.py as module
dview_file_name = "dview_functions.py"
dview_functions = importlib.import_module(dview_file_name)

def is_function(module, attribute):
    attr = getattr(module, attribute)
    return callable(attr)

def get_links_dict(files):
    links = {}
    for file in files:
        filepath = Path(file)
        links[filepath.stem] = filepath
    return links

def get_md_files(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        markdown_files += [os.path.join(root, file) for file in files if file.endswith('.md')]
    return markdown_files

def process_string(s, metadata):
    def callback(match):
        function_name = match.group(1).split(",", maxsplit=1)[0].strip('\"').split("/")[-1]

        # Check if the function exists in the module and is a callable
        if function_name in dir(dview_functions) and is_function(dview_functions, function_name):
            dview_call = getattr(dview_functions, function_name)
            # Now you can call the function
            result = dview_call(metadata)
        else:
            result = print(f"Function {function_name} not implemented in conversion code.", file=sys.stderr)
            result = ""
        return result

    pattern = "\`\$\=dv\.view\((.*)\)\`"
    return re.sub(pattern, callback, s)

parser = argparse.ArgumentParser()
parser.add_argument('--date', required=False)
parser.add_argument('--dir', required=True)
parser.add_argument('--campaign', required=False)
parser.add_argument('--configDir', required=True)
args = parser.parse_args()

# Get the date, campaign, and directory name from the command line arguments
dir_name = args.dir
input_campaign = args.campaign
md_file_list = get_md_files(dir_name)
links = get_links_dict(md_file_list)
override_year = clean_date(args.date) if args.date else None

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

    metadata["campaign"] = input_campaign
    metadata["override_year"] = override_year
    metadata["directory"] = args.configDir
    metadata["links"] = links
    metadata["file"] = file_name

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
        '''
        Would replace text with this if we wanted to add a note that the thing doesn't exist yet
        if not thing_exist:
            newlines = metadata_block
            newlines.append("# " + metadata.get("name", "unnamed entity") + "\n")
            newlines.append("**This does not exist yet!**\n")
        '''
        output_file.writelines(newlines)
 