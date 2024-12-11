from app.database import db
from app.schemas.user_schema import UserCreate
from bson import ObjectId

async def create_user(user: UserCreate):
    user_dict = user.model_dump()
    result = await db.database.users.insert_one(user_dict)
    user_dict["id"] = str(result.inserted_id)
    return user_dict

async def get_user_by_id(user_id: str):
    try:
        user = await db.database.users.find_one({"_id": ObjectId(user_id)})
        if user:
            user["id"] = str(user["_id"])
            del user["_id"]
        return user
    except Exception:
        return None
    
async def get_all_users():
    """
    Fetch all users from the 'users' collection in the database.
    Converts MongoDB ObjectId to string for the id field.
    """
    try:
        # Ensure the database connection is initialized
        if not db.database:
            raise Exception("Database connection is not initialized.")

        # Fetch all users from the collection
        users = []
        async for user in db.database["users"].find():
            # Transform ObjectId to string for the id field
            user["id"] = str(user["_id"])
            user.pop("_id", None)  # Safely remove the '_id' field
            users.append(user)

        # Print retrieved users for debugging (optional)
        print("Users retrieved:", users)
        return users
    except Exception as e:
        # Log the exception and re-raise it if needed
        print(f"Error retrieving users: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")
