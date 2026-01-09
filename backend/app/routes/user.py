from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.kitchen import User
from app.database import users_collection
from datetime import datetime

# ============================================================================
# STEP 4: USER ROUTES
# ============================================================================
# This file handles all URLs that start with /users
# It's like a specific department in our office.

# 1. Create the Router
# This is a mini-app that only handles user stuff.
router = APIRouter()

# 2. Signup Endpoint
# URL: POST /users/signup
# Why POST? Because we are SENDING data to create something new.
@router.post("/signup")
def create_user(user: User):
    print(f"📝 Received signup request for: {user.email}")
    
    # A. Check if user already exists
    # We look in the database for any document with this email
    existing_user = users_collection.find_one({"email": user.email})
    if existing_user:
        # If found, stop and return an error
        print("❌ User already exists!")
        raise HTTPException(status_code=400, detail="Email already registered")
    
    # B. Prepare data for saving
    # .dict() converts our Pydantic model to a standard dictionary
    user_data = user.dict()
    user_data["created_at"] = datetime.now()
    
    # C. Save to Database
    # insert_one() is the command to write to MongoDB
    result = users_collection.insert_one(user_data)
    
    # D. Return Success
    # We send back the ID of the new user to confirm it worked
    print(f"✅ User created with ID: {result.inserted_id}")
    return {
        "message": "User created successfully",
        "user_id": str(result.inserted_id)
    }

    print(f"✅ User created with ID: {result.inserted_id}")
    return {
        "message": "User created successfully",
        "user_id": str(result.inserted_id)
    }


# 3. Login Endpoint
# URL: POST /users/login
# We need a small model just for the login data (so we don't need phone/address)
class LoginRequest(BaseModel):
    email: str

@router.post("/login")
def login_user(login_data: LoginRequest):
    print(f"🔑 Received login attempt for: {login_data.email}")
    
    # A. Search for user
    user = users_collection.find_one({"email": login_data.email})
    
    # B. Check if found
    if not user:
        print("❌ Login failed: User not found")
        raise HTTPException(status_code=404, detail="User not found")
        
    # C. Return Success
    print(f"✅ Login successful for: {user['name']}")
    return {
        "message": "Login successful",
        "user_name": user["name"],
        "user_id": str(user["_id"])
    }

# Explanation:
# - LoginRequest: A specific "form" that only asks for Email.
# - find_one: MongoDB command to Find exactly one document match.
