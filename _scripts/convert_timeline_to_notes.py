import csv
import os
from pathlib import Path
import argparse
import datetime

MONTHNUM = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06", "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12" }

parser = argparse.ArgumentParser()
parser.add_argument('--csv', required=True)
parser.add_argument('--dir', required=True)
args = parser.parse_args()

## make output dir
Path(args.dir).mkdir(parents=True, exist_ok=True)

## currently not flexible - assumes a specific set of columns

headers = ['Date', 'Dunmari Frontier', 'Great Library', 'Other Campaigns', 'Rumors and News', 'Secrets']

## read each row

with open(args.csv, 'r', encoding='utf-8-sig', newline='') as tl:
    timeline = csv.reader(tl, dialect='excel')
    for day in timeline:
        # skip header row
        if day[0] == "Date":
            continue

        # parse the date assumes day month year format, with month a text string

        date_parts = day[0].split()
        print("Parsing date: " + "-".join(date_parts))
        event_date = date_parts[2] + "-" + MONTHNUM[date_parts[1][0:3]] + "-" + date_parts[0].zfill(2)
        event_file = args.dir + "/" + event_date + ".md"

        # open a file with the correct name
        with open(event_file, "w") as ef:
            
            #print yaml frontmatter

            print("---", file=ef)
            print("fc-calendar: Taelgar", file=ef)
            print("fc-category: Campaign Timeline", file=ef)
            print("fc-date: " + event_date, file=ef)
            print("tags: [timeline, unified-events]", file=ef)
            print("---\n", file=ef)

            # go through each column and print appropriate information

            for idx, day_event in enumerate(day):
                try:
                    header = headers[idx]
                except IndexError:
                    header = "Other Events"
               
                if header == "Secrets" and day_event:
                    print("%%SECRET", file=ef)
                if day_event:
                    print("## " + header, file=ef)
                    print(day_event + "\n", file=ef)
                if header == "Secrets" and day_event:
                    print("%%", file=ef)





