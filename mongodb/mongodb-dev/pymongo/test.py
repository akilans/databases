from pymongo import MongoClient

client = MongoClient("localhost",27017)

db = client.test

friends = db.friends.find()

for friend in friends:
    print(friend['name'])
