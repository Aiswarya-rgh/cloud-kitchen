from fastapi import FastAPI
from app.database import check_connection

# ============================================================================
# STEP 3: API SERVER ENTRY POINT
# ============================================================================
# This file is the "Receptionist" of our application. All requests come here first.

# 1. Create the App
# We initialize the FastAPI application.
# title: The name that will appear in the automatic documentation
app = FastAPI(title="Cloud Kitchen API", version="1.0.0")

# ============================================================================
# CORS CONFIGURATION (Allow Frontend to talk to Backend)
# ============================================================================
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (for learning purposes)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# 2. Server Startup Event
# This runs automatically ONE time when we start the server.
@app.on_event("startup")
def startup_evet():
    print("🚀 Starting up Cloud Kitchen Server...")
    # We call our database check function from Step 2 to make sure we are connected
    check_connection()

# 3. The Root Route (Home Page)
# When someone visits the base URL (http://localhost:8000/), this function runs.
# @app.get("/") -> This is a "Decorator". It tells the server "When a GET request comes to /, run this function".
@app.get("/")
def read_root():
    return {
        "message": "Welcome to the Cloud Kitchen API!",
        "status": "active"
    }

# Explanation for Learning:
# - FastAPI: The framework that handles the web server part.
# - Decorator (@): A special Python syntax to modify functions (like telling them to react to URLs).
# - JSON: The data format we return (looks like a Python dictionary) - frontend understands this easily.


# ============================================================================
# ROUTER REGISTRATION
# ============================================================================
# We connect our separate route files to the main app here.
from app.routes import user, kitchen, menu

app.include_router(user.router, prefix="/users", tags=["Users"])
app.include_router(kitchen.router, prefix="/kitchens", tags=["Kitchens"])
app.include_router(menu.router, prefix="/menu", tags=["Menu"])
