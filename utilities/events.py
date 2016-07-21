import re
import json
import db
import datetime
from dateutil.parser import parse

section_items = []
pattern_text_file = re.compile("(~~~~*)")
pattern_split_lines = re.compile("\n")
def process_text_file(events_file):
    with open(events_file) as txt_file:
        my_file = txt_file.read()
        sections = pattern_text_file.split(my_file)
        for section in sections:

            if not pattern_text_file.search(section):
                section_items.append(section.strip())

def create_individual_items(section):
    items = []
    result = pattern_split_lines.split(section)
    if result:
        [items.append(result_item) for result_item in result]
    return result



    # [print(record,"==") for record in db_record]

def create_dict_record(section):
    record = {}
    has_ticket = False
    record['title']         = section[0]
    record['photo']         = section[1]
    record['time']          = section[2]
    record['date']          = section[3]
    record['parsed_date']   = parse(record['date'])
    record['venue']         = section[4]
    record['address']       = section[5]
    record['url']           = section[6]
    record['description']   = section[7]
    record['tickets']       = "none"
    if len(section) == 9:
        record['tickets']   = process_ticket_group(section[8])

    record['created'] = datetime.datetime.now()
    record['updated'] = datetime.datetime.now()
    record['photo'] = re.search("\s.*",record['photo']).group().strip()
    record['url'] = re.search("(http://|https://)(.*)",record['url']).group(2).strip()

    record = process_venue_url_info(record)

    return record

split_string_regex = re.compile("#")

def process_venue_url_info(record):
    original_record = record
    split = split_string_regex.split(record['venue'])
    if len(split) == 2:
        record['venue'] = split[0]
        record['venue_url'] = split[1]
    else:
        record['venue_url'] = "none"
    return record

def process_ticket_group(ticket):
    result = ticket
    match = re.search("http.?://.*$", ticket)
    if match:
        result = match.group()
    print("result:", result )
    return result


def insert_into_database(db_record):
    events = db.events
    db.events.drop()
    result =events.insert_many(db_record)
    print(result.inserted_ids)
    cursor = events.find().sort("date")


def list_events():
    events = db.events
    cursor = events.find().sort("date")
    for cursor_item in cursor:
        for (k,v) in cursor_item.items():
            print(k,":",v)
        print("++")

def update_events_database(events_file):
    db_record = []
    process_text_file(events_file)
    for section in section_items:
        result = create_individual_items(section)
        db_record.append(create_dict_record(result))

    insert_into_database(db_record)

def main(events_file):
    update_events_database(events_file)
    list_events()
