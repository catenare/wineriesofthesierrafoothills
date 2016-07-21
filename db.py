from pymongo import MongoClient

client = MongoClient()

db = client.winebook

stores = db.stores
events = db.events
