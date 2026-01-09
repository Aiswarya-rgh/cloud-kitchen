import urllib.request
import json

def add_menu_items():
    print("📋 Adding items to the menu...")
    
    # 1. First, we need a Kitchen ID.
    # Ideally, we would get this from the created kitchen.
    # For TEST purposes, paste your Kitchen ID below if you know it,
    # OR we can ask the user to type it.
    
    kitchen_id = input("Enter the Kitchen ID (copy from browser/terminal): ").strip()
    
    url = "http://127.0.0.1:8000/menu/add"
    
    # List of dishes to add
    dishes = [
        {
            "kitchen_id": kitchen_id,
            "name": "Masala Chai",
            "description": "Hot tea with ginger and cardamom",
            "price": 20.0,
            "category": "Beverage",
            "cuisine_style": "Indian"
        },
        {
            "kitchen_id": kitchen_id,
            "name": "Dhokla",
            "description": "Steamed savory cake made from rice and chickpea flour",
            "price": 60.0,
            "category": "Appetizer",
            "cuisine_style": "Gujarati"
        },
        {
            "kitchen_id": kitchen_id,
            "name": "Gujarati Thali",
            "description": "Complete meal with Roti, Dal, Rice, and Shaak",
            "price": 150.0,
            "category": "Main Course",
            "cuisine_style": "Gujarati"
        }
    ]
    
    for dish in dishes:
        data = json.dumps(dish).encode('utf-8')
        req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
        
        try:
            with urllib.request.urlopen(req) as response:
                print(f"✅ Added: {dish['name']}")
        except urllib.error.URLError as e:
            print(f"❌ Failed to add {dish['name']}: {e}")

if __name__ == "__main__":
    add_menu_items()
