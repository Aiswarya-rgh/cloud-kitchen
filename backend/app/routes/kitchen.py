from fastapi import APIRouter, HTTPException
from app.models.kitchen import Kitchen
from app.database import kitchens_collection
from datetime import datetime
from bson import ObjectId

# ============================================================================
# STEP 5: KITCHEN ROUTES
# ============================================================================
# This file handles everything related to Kitchens.

router = APIRouter()

# 1. Create a New Kitchen
# URL: POST /kitchens/create
@router.post("/create")
def create_kitchen(kitchen: Kitchen):
    print(f"👩‍🍳 Opening new kitchen: {kitchen.name}")
    
    # Validation: Check if kitchen name already exists?
    # (Optional, but good practice)
    
    kitchen_data = kitchen.dict()
    kitchen_data["created_at"] = datetime.now()
    
    # Save to MongoDB
    result = kitchens_collection.insert_one(kitchen_data)
    
    return {
        "message": "Kitchen opened successfully!",
        "kitchen_id": str(result.inserted_id),
        "owner": kitchen.owner_name
    }

# 2. List All Kitchens
# URL: GET /kitchens
@router.get("/")
def get_all_kitchens():
    # Fetch all kitchens from database
    kitchens = list(kitchens_collection.find())
    
    # Convert weird MongoDB ID to string for every kitchen
    for k in kitchens:
        k["_id"] = str(k["_id"])
        
    return kitchens

# 3. Get Specific Kitchen
# URL: GET /kitchens/{kitchen_id}
@router.get("/{kitchen_id}")
def get_kitchen(kitchen_id: str):
    # Search by ID
    try:
        obj_id = ObjectId(kitchen_id)
    except:
        raise HTTPException(status_code=400, detail="Invalid Kitchen ID format")
        
    kitchen = kitchens_collection.find_one({"_id": obj_id})
    
    if not kitchen:
        raise HTTPException(status_code=404, detail="Kitchen not found")
        
    kitchen["_id"] = str(kitchen["_id"])
    return kitchen
