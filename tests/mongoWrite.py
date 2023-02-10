import pymongo
from bson.objectid import ObjectId
import datetime

username = 'johnstreetcapital'
password = 'OJRpUn4mtBxi51Oq'
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@testcluster.yxijioi.mongodb.net/?retryWrites=true&w=majority")
db = client['companyBalanceSheet']
companies = db['companies']


def mongoPost(post):
    postID = companies.insert_one(post).inserted_id
    print(postID)
    return postID

def mongoQuery(query):
    print(companies.find_one({"_id": ObjectId(query)}))

def main():

    post = {"name": "zim",
            "industry": ['technology', 'consumer electronics'],
            "cashflow": -100000,
            "lastUpdate": datetime.datetime.utcnow()}

    mongoQuery(mongoPost(post))

if __name__ == '__main__':
    main()
