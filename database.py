import pymongo

class Database(object):
    URI = "mongodb://127.0.0.1:27017"
    DATABASE = None
    
    @staticmethod
    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client["dature"]

    @staticmethod
    def insert(collection, data):
        # data must be dictionary
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection, query):
        return Database.DATABASE[collection].find(query,{"_id":0})

    @staticmethod
    def find_one(collection, query):
        return Database.DATABASE[collection].find_one(query,{"_id":0})

db = Database() 