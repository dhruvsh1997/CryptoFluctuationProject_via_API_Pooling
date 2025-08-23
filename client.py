# client.py
import requests
import time

API_URL = "http://localhost:5000/crypto-price"

print("Starting cryptocurrency price API polling...")

while True:
    try:
        # 1. Make request to server
        response = requests.get(API_URL)
        data = response.json()
        
        # 2. Process response
        price = data['price']
        timestamp = data['timestamp']
        print(f"Price: ${price:.2f} | Time: {timestamp}")
        
    except Exception as e:
        print(f"Error: {e}")
    
    # 3. Wait before next poll
    time.sleep(2)  # Poll every 2 seconds
