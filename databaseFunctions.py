import pymongo
from bson.objectid import ObjectId

'''
Define the following global variables in your code with your assigned JSCG credentials:
username = ''
password = ''

To perform CRUD operations on our database, define the following global variables in your code:
database = ''
collection = ''
'''

def mongoPost(post):
    '''
    This function takes a dictionary as an argument and inserts it into the database.
    
    '''
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@testcluster.yxijioi.mongodb.net/?retryWrites=true&w=majority")
    db = client[database]
    collection = db[collection]
    collection.insert_one(post)