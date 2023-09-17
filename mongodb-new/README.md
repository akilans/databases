# MongoDB - Basics

- SQL - DB, Table, Row
- NoSQL - DB, Collections, Document,

```bash
# Installation
docker run --name mongo -d -p 27017:27017 mongodb/mongodb-community-server:latest
docker exec -it mongo mongosh
```

```
# mongosh commands
use school; #create & switch db
show collections; # list collections
db.createCollection("students"); # create collection
db.students.drop(); # drop collection
db.getCollectionNames(); # list all the collections
db.dropDatabase() # Drop database;
db.student.insertOne({
     name: "Akilan",
     details: {
     isWorking: true,
     age: 34,
     height: 168.0
     },
     friends: [
        "Alex",
        "Kumar",
        "Jegan"
     ]
     });

db.student.insertMany([
    {
        name: "Alex",
        details: {
            isWorking: true,
            age: 40,
            height: 168.0
         },
        friends: [
            "Akilan",
            "Kumar",
            "Jegan"
        ]
    },
    {
        name: "Kumar",
        details: {
            isWorking: true,
            age: 36,
            height: 168.0
         },
        friends: [
            "Akilan",
            "Alex",
            "Jegan"
        ]
    }

    ]);

# List all
db.student.find();

# List all
db.student.find().limit(2)

# find by name
db.student.find({name:"Alex"});

# sort
db.student.find().sort({name:-1})
# ignore, include fields
db.student.find({},{_id:false,name: true, friends: true});

db.student.updateOne({name:'Akilan'},{$set:{company: 'Oracle'}});
db.student.updateMany({},{$set:{industry: "Information Technology"}});
#update many if key doesn't exists
db.student.updateMany({industry:{$exists: false}},{$set:{industry: "IT"}});

db.student.deleteOne({sName: "Mark"});
# delete documents if key exists
db.student.deleteMany({age: {$exists: true}});

#operator
db.student.find({name:'Kumar'})
db.student.find({name:{$in:['Akilan','Inba']}});
db.student.find({name:{$nin:['Akilan','Inba']}});
db.student.find({"details.age": {$gte: 35}});
db.student.find({"details.age": {$lte: 35}});

# logical operator
db.student.find({$and: [{name: 'Akilan'},{"details.age":{$gte: 30}}]});
db.student.find({$or: [{name: 'Akilan'},{"details.age":{$gte: 35}}]});
db.student.find({$or: [{name: 'Akilan'},{"details.age":{$lte: 36}}]});

db.student.find({$or: [{name: 'Akilan'},{"details.age":{$lte: 36}}]},{_id: false});

# Index
db.student.find({name: 'Akilan'}).explain("executionStats") # without index scan all docs
db.student.createIndex({name: 1})
db.student.find({name: 'Akilan'}).explain("executionStats")
db.student.dropIndex('name_1');
```
