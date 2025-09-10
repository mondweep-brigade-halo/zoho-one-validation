import requests
import json
import sys

def get_tokens(client_id, client_secret, code):
    url = "https://accounts.zoho.com/oauth/v2/token"
    params = {
        "grant_type": "authorization_code",
        "client_id": client_id,
        "client_secret": client_secret,
        "code": code,
    }
    response = requests.post(url, params=params)
    if response.status_code == 200:
        tokens = response.json()
        with open("zoho_tokens.json", "w") as f:
            json.dump(tokens, f)
        print("Successfully generated and saved tokens to zoho_tokens.json")
    else:
        print(f"Error generating tokens: {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python get_zoho_tokens.py <client_id> <client_secret> <code>")
        sys.exit(1)

    client_id = sys.argv[1]
    client_secret = sys.argv[2]
    code = sys.argv[3]

    get_tokens(client_id, client_secret, code)
