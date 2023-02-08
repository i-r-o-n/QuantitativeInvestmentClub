
from pymongo import MongoClient
password = 'OJRpUn4mtBxi51Oq'
client = MongoClient(f'mongodb+srv://johnstreetcapital:<{password}>@testcluster.yxijioi.mongodb.net/?retryWrites=true&w=majority')

db = client.sample_mflix
movies = db['movies']

#query document
uin = input('which movie do you want to search?')

#query
query = {'title': uin}
print(movies.find_one(query))
print('done')