from motor.motor_asyncio import AsyncIOMotorClient
from app.config import settings  # Assuming settings contain your MongoDB URL

class Database:
    client: AsyncIOMotorClient = None
    database = None  # This will hold the MongoDB database instance

db = Database()

# Connect to MongoDB
async def connect_to_mongo():
    print("Attempting to connect to MongoDB...")

    db.client = AsyncIOMotorClient("mongodb+srv://aj123:aj123@shoppify.fsyemvp.mongodb.net/my_database")  # Use the URL from the config
    db.database = db.client["my_database"]  # Replace with your database name
    print("Database connection established.")


# Close the MongoDB connection
async def close_mongo_connection():
    db.client.close()
