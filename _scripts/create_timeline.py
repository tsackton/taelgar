import argparse
import json
import yaml
import os
import sys
import datetime

def get_md_files(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        markdown_files += [os.path.join(root, file) for file in files if file.endswith('.md')]
    return markdown_files

def parse_daily_notes(text, metadata, file_name):
    # split text by '---' and parse each event separately
    events = text.split("---")
    events_array = []

    for event in events:
        if event == "" or event == "\n":
            continue

        event_lines = [i for i in event.split("\n") if i]
        event_metadata = json.loads(event_lines[1])
        event_metadata["header"] = event_lines[0]
        event_text = ''.join(event_lines[2:])

        events_array.append({ "text" : event_text, "metadata" : event_metadata })

    return events_array

parser = argparse.ArgumentParser()
parser.add_argument('--dir', required=True, nargs="*")
args = parser.parse_args()

md_file_list = []
for dir in args.dir:
    md_file_list += get_md_files(dir)

all_events = {}

## copied from convert_markdown, should abstract to a function

for file_name in md_file_list:
    # Open the input file
    with open(file_name, 'r', 2048, "utf-8") as input_file:
        lines = input_file.readlines()

    # if file is blank, move on
    if len(lines) == 0:
        continue

    # Check if the file starts with a metadata block
    metadata = dict()
    text_start = 0
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
            text_start = len(metadata_block) + 1
    
    file_text = ""
    if metadata and metadata.get("type") == "Event":
        file_text = ''.join(lines[text_start:]) 
        file_date = metadata["taelgar-date"]
        if type(file_date) == int:
            file_date = datetime.date(file_date, 1, 1)

        if metadata.get("subtype") == "Daily Note":
            events = parse_daily_notes(file_text, metadata, file_name)
        else:
            events = [ { "text": file_text, "metadata": metadata } ]
    
        if file_date in all_events:
            all_events[file_date].append(events)
        else:
            all_events[file_date] = events

# at this point should have a big dictionary of all events
# for testing, let's write them out to stdout

for date in sorted(all_events.keys()):
    datestring = date.strftime("%d %b %Y")
    print("## " + datestring)
    for date_event in all_events[date]:
        print(date_event["text"])
        print("\n---\n")
