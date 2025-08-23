# app.py
from flask import Flask, jsonify
import random
import time
import threading

app = Flask(__name__)

# Simulated cryptocurrency price
crypto_price = 100.00

def update_price():
    """Background thread to update cryptocurrency price every 3 seconds"""
    global crypto_price
    while True:
        time.sleep(3)
        # Random price fluctuation between -2% to +2%
        change = random.uniform(-0.02, 0.02)
        crypto_price *= (1 + change)
        print(f"Price updated: ${crypto_price:.2f}")

# Start price updater thread
threading.Thread(target=update_price, daemon=True).start()

@app.route('/crypto-price')
def get_crypto_price():
    """Endpoint to get current cryptocurrency price"""
    return jsonify({
        'price': round(crypto_price, 2),
        'timestamp': time.time()
    })

if __name__ == '__main__':
    app.run(port=5000)
