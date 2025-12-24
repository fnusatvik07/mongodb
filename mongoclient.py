# mongo_client.py
from pymongo import MongoClient
from pymongo.errors import PyMongoError
from config import MONGO_URI
from dotenv import load_dotenv 
load_dotenv()


class MongoDBClient:
    """
    Responsible only for creating and holding MongoDB connection.
    """

    def __init__(self):
        self.client = MongoClient(
            MONGO_URI,
            serverSelectionTimeoutMS=5000
        )
        self._ping()

    def _ping(self):
        """Verify MongoDB Atlas connection"""
        try:
            self.client.admin.command("ping")
            print("✅ MongoDB Atlas connected")
        except PyMongoError as e:
            raise RuntimeError(f"MongoDB connection failed: {e}")

    def get_database(self, db_name: str):
        return self.client[db_name]
