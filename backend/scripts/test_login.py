import urllib.request
import json
import time

def test_login():
    url = "http://127.0.0.1:8000/users/login"
    
    # CASE 1: SUCCESS (Rahul)
    print("\n1️⃣  Testing Valid User (Rahul)...")
    payload_success = {"email": "rahul@example.com"}
    data_success = json.dumps(payload_success).encode('utf-8')
    req_success = urllib.request.Request(url, data=data_success, headers={'Content-Type': 'application/json'}, method='POST')
    
    try:
        with urllib.request.urlopen(req_success) as response:
            print("✅ SUCCESS! " + response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"❌ FAILED with code {e.code}: {e.read().decode('utf-8')}")
        
    # CASE 2: FAILURE (Fake User)
    print("\n2️⃣  Testing Invalid User (Fake)...")
    payload_fail = {"email": "fake@example.com"}
    data_fail = json.dumps(payload_fail).encode('utf-8')
    req_fail = urllib.request.Request(url, data=data_fail, headers={'Content-Type': 'application/json'}, method='POST')
    
    try:
        with urllib.request.urlopen(req_fail) as response:
            print("❓ Unexpected Success (Should have failed): " + response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        if e.code == 404:
             print("✅ CORRECT BEHAVIOR! Server refused login: User not found.")
        else:
             print(f"❌ WRONG ERROR CODE {e.code}: {e}")

if __name__ == "__main__":
    test_login()
