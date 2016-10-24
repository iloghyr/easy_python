#!/bin/env python
#coding: utf-8



import pymongo
print [x for x in range(2)]

con = pymongo.MongoClient("localhost", 27017)
db = con.mars
collection = db.users

data = collection.find_one({"username":"hyr"})
print data
data['age'] = 225
print collection.update({"_idd":data['_id']}, data)
print collection.find_one({"username":"hyr"})

# for i in collection.find().sort('_id', pymongo.DESCENDING).limit(1):
#     print i




