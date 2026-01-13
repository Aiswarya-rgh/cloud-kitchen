import sys
import os

# Add the project root to the Python path so we can import 'app'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import kitchens_collection, menu_items_collection

def add_images():
    print("🖼️ Adding beautiful images to your database...")

    # 1. Update Kitchen (Priya's Gujarati Kitchen)
    # Using a beautiful traditional Indian kitchen/cooking image
    kitchen_image = "https://images.unsplash.com/photo-1589302168068-964664d93dc0?auto=format&fit=crop&w=800&q=80"
    
    kitchen_result = kitchens_collection.update_many(
        {"name": {"$regex": "Priya", "$options": "i"}},
        {"$set": {"image_url": kitchen_image}}
    )
    print(f"✅ Updated {kitchen_result.modified_count} kitchen(s)")

    # 2. Update Menu Items (Dishes)
    # Map dish names to beautiful food images
    dish_images = {
        "Masala Chai": "https://images.unsplash.com/photo-1594631252845-29fc4586db90?auto=format&fit=crop&w=400&q=80",
        "Dhokla": "https://images.unsplash.com/photo-1626074353765-517a681e40be?auto=format&fit=crop&w=400&q=80",
        "Gujarati Thali": "https://images.unsplash.com/photo-1585937421612-70a008356fbe?auto=format&fit=crop&w=400&q=80"
    }

    for dish_name, img_url in dish_images.items():
        menu_result = menu_items_collection.update_many(
            {"name": {"$regex": dish_name, "$options": "i"}},
            {"$set": {"image_url": img_url}}
        )
        print(f"✅ Updated image for: {dish_name}")

    print("\n🎉 Done! Refresh your browser to see the beautiful food!")

if __name__ == "__main__":
    add_images()
