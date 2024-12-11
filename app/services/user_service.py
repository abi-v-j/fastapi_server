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
    try:
        # Fetch all users using find()
        users = []
        async for user in db.database.users.find():
            user["id"] = str(user["_id"])
            del user["_id"]
            users.append(user)
        print("Users retrieved:", users)
        return users
    except Exception as e:
        # Optionally, log the exception
        print(f"Error retrieving users: {e}")
        return None
