from fastapi import APIRouter
from app.models.user import User
from app.schemas.user import UserCreate, UserResponse
from fastapi import HTTPException
import app.database.dbconfig as dbconfig

router = APIRouter()

@router.post("/users/", response_model=UserResponse)
async def create_user(user: UserCreate):
    # Logic to create a new user
    pass

@router.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: int):
    resp = dbconfig.get_specific_user(user_id)
    return resp.data
    pass

@router.get("/users/", response_model=list[UserResponse])
async def read_users():
    resp=supabase.table("users").select("*").execute()
    return resp.data
    # Logic to read all users
    pass

@router.put("/users/{user_id}", response_model=UserResponse)
async def update_user(user_id: int, user: UserCreate):
    # Logic to update a user by ID
    pass

@router.delete("/users/{user_id}")
async def delete_user(user_id: int):
    # Logic to delete a user by ID
    pass