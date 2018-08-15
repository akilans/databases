from bottle import template, route,run
from pymongo import MongoClient

client = MongoClient("localhost",27017)

db = client.test

@route("/")
def index():
    akilan = db.friends.find_one()
    return "Hello %s" %akilan["name"]

@route("/<name>")
def index_with_name(name):
    return template("<h1>Hello {{name}}</h1>",name=name)

run(host="localhost",port=5000)