from app.database import users_collection

def view_all_users():
    print("\n🔎 Checking MongoDB for Users...")
    
    # Get all documents from the users collection
    # list() converts the cursor to a standard Python list
    users = list(users_collection.find())
    
    if len(users) == 0:
        print("❌ No users found in the database yet.")
    else:
        print(f"✅ Found {len(users)} user(s):\n")
        for user in users:
            print(f"--- User ID: {user['_id']} ---")
            print(f"Name:  {user.get('name')}")
            print(f"Email: {user.get('email')}")
            print(f"Phone: {user.get('phone')}")
            print("--------------------------\n")

if __name__ == "__main__":
    view_all_users()
