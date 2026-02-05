import os
from motor.motor_asyncio import AsyncIOMotorClient

MONGODB_URI = os.getenv("MONGO_URL", "mongodb://admin:qwerty@localhost:27017?authSource=admin")
DATABASE_NAME = "task_manager"

client = AsyncIOMotorClient(MONGODB_URI)
database = client[DATABASE_NAME]

def get_database():
    return database