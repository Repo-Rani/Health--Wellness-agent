import os
from dotenv import load_dotenv
from pymongo import MongoClient 


load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)

db = client["health_wellness_data"]  
chat_collection = db["chat_collection"] 