import csv
import db
import re
from json import dumps
import datetime

store_data = []

labels = ["county","city","venue","street","city","state","zip","url"]

def process_street(store_record):
    pattern = re.compile("(\w*)")
    updated_record = [re.sub("\s\s"," ", item) for item in store_record]
    new_record = [item.strip() for item in updated_record]
    return new_record

def process_stores_records(file_name):
    with open(file_name) as csvfile:
         reader = csv.reader(csvfile, delimiter=",")
         for row in reader:
            new_row = process_street(row)
            record_row = dict(zip(labels,new_row))
            record_row['created'] = datetime.datetime.now()
            record_row['updated'] = datetime.datetime.now()
            store_data.append( record_row )
    return store_data

def update_database(file_name):
    store_data = process_stores_records(file_name)
    stores = db.stores
    db.stores.drop()
    result = stores.insert_many(store_data)
    print(result.inserted_ids)
    cursor = stores.find().sort("county")
    for item in cursor:
        print(item)
