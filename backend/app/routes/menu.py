from fastapi import APIRouter, HTTPException
from app.models.kitchen import MenuItem
from app.database import menu_items_collection, kitchens_collection
from bson import ObjectId

# ============================================================================
# STEP 6: MENU ROUTES
# ============================================================================
# This file handles the Food!

router = APIRouter()

# 1. Add item to menu
# URL: POST /menu/add
@router.post("/add")
def add_menu_item(item: MenuItem):
    print(f"🥘 Adding dish: {item.name} for Kitchen: {item.kitchen_id}")
    
    # Validation: Does the kitchen actually exist?
    # We use the "Reference Key" (kitchen_id) to check the parent.
    try:
        k_id = ObjectId(item.kitchen_id)
        kitchen = kitchens_collection.find_one({"_id": k_id})
        if not kitchen:
            raise HTTPException(status_code=404, detail="Kitchen not found")
    except:
        raise HTTPException(status_code=400, detail="Invalid Kitchen ID")

    # Save the dish
    item_data = item.dict()
    result = menu_items_collection.insert_one(item_data)
    
    return {
        "message": "Dish added to menu!",
        "item_id": str(result.inserted_id)
    }

# 2. Get Menu for a specific Kitchen
# URL: GET /menu/{kitchen_id}
@router.get("/{kitchen_id}")
def get_menu(kitchen_id: str):
    print(f"📜 Fetching menu for Kitchen: {kitchen_id}")
    
    # Query: Find all dishes where 'kitchen_id' MATCHES the one we asked for.
    # This is the "Linking" in action.
    dishes = list(menu_items_collection.find({"kitchen_id": kitchen_id}))
    
    # Fix the IDs for display
    for dish in dishes:
        dish["_id"] = str(dish["_id"])
        
    return dishes
