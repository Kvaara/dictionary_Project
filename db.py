import pymongo
from pymongo import MongoClient
import json

# Establishing a connection to the default host (localhost) and the default port (27017)
client = MongoClient()

# Name of the database that we want to create to the localhost database
db = client.dictionary

# Name of the collection that we want to add into the just created database
collection = db.english

collectionCount = collection.count_documents({})

if (collectionCount == 0):
    # Loading in the dictionary data and assigning it to a variable data
    data = json.load(
        open("./Interactive English Dictionary/dictionaryData.json"))
    # The below is for inserting a collection named english with all of the dictionary data inside a database named dictionary
    print("Adding data to the database collection...")
    for key in data:
        array = {}
        if (len(data[key]) > 1):
            array[key] = data[key]
        else:
            array[key] = "".join(data[key])

        collection.insert_one(array)
