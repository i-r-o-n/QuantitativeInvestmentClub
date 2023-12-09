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

def companyPost(ticker, sector, industry, eps): 
    '''
    This function defines the data structure for a company document.
    '''
    post = {
        "ticker": ticker,
        "sector":sector,
        "industry": industry,
        "eps": eps
    }

    mongoPost(post)
    return print(f'posted {ticker} to {database}')

def mongoPost(post):
    '''
    This function takes a dictionary as an argument and inserts it into the database.
    Post strucutre:
   
    '''
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@testcluster.yxijioi.mongodb.net/?retryWrites=true&w=majority")
    db = client[database]
    collection = db[collection]
    collection.insert_one(post)

def mongoQuery(query):
    '''
    This function takes a string as an argument and returns the document with the corresponding ID.
    '''
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@testcluster.yxijioi.mongodb.net/?retryWrites=true&w=majority")
    db = client[database]
    collection = db[collection]
    return collection.find_one({"name": query})
