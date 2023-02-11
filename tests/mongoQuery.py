import pymongo

username = ''
password = ''

def mongo_call(input):
    client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@testcluster.yxijioi.mongodb.net/?retryWrites=true&w=majority")
    db = client['sample_mflix']
    movies = db['movies']
    docs = movies.find_one({"title" : input})
    print(docs)

def main():
    uin = input('query: ')
    mongo_call(uin)

if __name__ == '__main__':
    main()
