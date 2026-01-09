from pymongo import MongoClient
import os
from dotenv import load_dotenv

# ============================================================================
# STEP 2: DATABASE CONNECTION
# ============================================================================
# This file handles the connection between our Python application and MongoDB.
# It's like plugging the cord into the concept.

# 1. Load environment variables
# This looks for a .env file and loads the variables inside (like keys, passwords)
load_dotenv()

# 2. Get the connection string
# We try to get MONGO_URL from the .env file.
# If it's not there, we use the default local address "mongodb://localhost:27017"
MONGO_CONNECTION_STRING = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# 3. Create the Database Client
# The client is the main entry point to the MongoDB system
try:
    client = MongoClient(MONGO_CONNECTION_STRING)
    print(f"Connecting to MongoDB at: {MONGO_CONNECTION_STRING}")
except Exception as e:
    print(f"Error creating MongoDB client: {e}")

# 4. Connect to our specific database
# We name our database "cloud_kitchen_db"
db = client.cloud_kitchen_db

# 5. Define Collections
# MongoDB stores documents in "collections" (similar to Tables in SQL)
# We creating easy-to-use variables for each collection we need

users_collection = db["users"]        # Stores User profiles
kitchens_collection = db["kitchens"]  # Stores Kitchen details
menu_items_collection = db["menu_items"] # Stores Dishes
orders_collection = db["orders"]      # Stores Orders
reviews_collection = db["reviews"]    # Stores Reviews

# 6. Connection Check Function
# We can call this to verify everything is working
def check_connection():
    try:
        # The 'ismaster' command is a quick way to check if the server is responding
        client.admin.command('ismaster')
        print("✅ MongoDB connection successful!")
        return True
    except Exception as e:
        print(f"❌ MongoDB connection failed: {e}")
        return False
