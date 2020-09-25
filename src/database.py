#from config import DBURL
from pymongo import MongoClient

client = MongoClient("mongodb://localhost/RankingDB")
db = client.get_database()