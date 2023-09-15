from fastapi import FastAPI
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
mongoDBClient = client["IKEA"]
user_collection=mongoDBClient["user_collection"]