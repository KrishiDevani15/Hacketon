import requests
import json
import base64
import hmac
import hashlib
import time

class GeminiAPI:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = 'https://generativelanguage.googleapis.com'

    def create_headers(self, endpoint, payload):
        payload = json.dumps(payload).encode()
        b64_payload = base64.b64encode(payload)
        signature = hmac.new(self.api_secret.encode(), b64_payload, hashlib.sha384).hexdigest()

        headers = {
            'Content-Type': 'text/plain',
            'Content-Length': '0',
            'X-GEMINI-APIKEY': self.api_key,
            'X-GEMINI-PAYLOAD': b64_payload,
            'X-GEMINI-SIGNATURE': signature,
            'Cache-Control': 'no-cache'
        }

        return headers

    def get_account_balances(self):
        endpoint = '/balances'
        url = self.base_url + endpoint

        payload = {
            "request": "/v1/balances",
            "nonce": int(time.time() * 1000),
        }

        headers = self.create_headers(endpoint, payload)

        try:
            response = requests.post(url, headers=headers)
            if response.status_code == 200:
                balances = response.json()
                return balances
            else:
                print("Error:", response.status_code, response.text)
                return None
        except Exception as e:
            print("Exception:", e)
            return None

# Example usage
if __name__ == "__main__":
    # Replace with your actual Gemini API key and secret
    API_KEY = 'AIzaSyDiHIeAsfCOY2bhV_S1bXk4Y966xFay4s8'
    API_SECRET = '3e5e22139f29e2833bacafc37b8aadddf0585f97'

    gemini = GeminiAPI(API_KEY, API_SECRET)
    balances = gemini.get_account_balances()
    if balances:
        print("Account Balances:")
        for balance in balances:
            print(f"{balance['currency']}: {balance['amount']}")