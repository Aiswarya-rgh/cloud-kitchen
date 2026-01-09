import urllib.request
import json
import time

def create_user():
    print("⏳ Attempting to create a new user via API...")
    
    url = "http://127.0.0.1:8000/users/signup"
    
    # Data to send
    payload = {
        "name": "Rahul",
        "email": "rahul@example.com",
        "phone": "9876543210",
        "address": "Mumbai, India"
    }
    
    # Prepare the request
    # we convert dictionary -> json string -> bytes
    data = json.dumps(payload).encode('utf-8')
    
    req = urllib.request.Request(
        url,
        data=data,
        headers={'Content-Type': 'application/json'},
        method='POST'
    )
    
    try:
        # Send the request
        with urllib.request.urlopen(req) as response:
            result = response.read().decode('utf-8')
            print("\n✅ SUCCESS! Server responded:")
            print(result)
            print("\nNow run 'python check_db.py' to verify it is in global database.")
            
    except urllib.error.URLError as e:
        print(f"\n❌ REQUEST FAILED: {e}")
        print("💡 HINT: Is the 'uvicorn' server running? Please make sure you have a separate terminal running 'uvicorn app.main:app --reload'")

if __name__ == "__main__":
    create_user()
