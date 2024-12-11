from fastapi import APIRouter, HTTPException, Depends
from app.schemas.user_schema import UserCreate, UserResponse
from app.services.user_service import create_user, get_user_by_id,get_all_users
from typing import List

router = APIRouter()

@router.post("/", response_model=UserResponse)
async def create_user_api(user: UserCreate):
    new_user = await create_user(user)
    return new_user

@router.get("/{user_id}", response_model=UserResponse)
async def get_user_api(user_id: str):
    user = await get_user_by_id(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/",  response_model=List[UserResponse])
async def get_user_api():
    user = await get_all_users()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
