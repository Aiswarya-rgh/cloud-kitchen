import urllib.request
import json
import time

def create_kitchen():
    print("🥘 Attempting to open a new Kitchen...")
    
    url = "http://127.0.0.1:8000/kitchens/create"
    
    # Data: A typical Home Kitchen profile
    payload = {
        "name": "Priya's Authentic Gujarati",
        "owner_name": "Priya Patel",
        "description": "Authentic home-cooked thalis and snacks from Gujarat.",
        "cuisine_type": "Gujarati",
        "address": "42, Shanti Nagar, Mumbai",
        "opening_time": "10:00",
        "closing_time": "20:00",
        "speciality": "Dhokla and Thepla"
    }
    
    data = json.dumps(payload).encode('utf-8')
    req = urllib.request.Request(url, data=data, headers={'Content-Type': 'application/json'}, method='POST')
    
    try:
        with urllib.request.urlopen(req) as response:
            print("\n✅ SUCCESS! Server responded:")
            print(response.read().decode('utf-8'))
            print("\n🎉 Priya's Kitchen is now OPEN on the platform!")
            
    except urllib.error.URLError as e:
        print(f"\n❌ FAILED: {e}")
        print("💡 Is the server running? (uvicorn app.main:app --reload)")

if __name__ == "__main__":
    create_kitchen()
