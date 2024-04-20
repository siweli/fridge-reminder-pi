#& ".venv/Scripts/Activate.ps1"

import requests
from uuid import getnode

# device token
dev_token = str(getnode())

url = "http://localhost:3000/api/checkdevice"
data = {"data" : dev_token}

try:
    response = requests.post(url, json=data)
    print(response.json())
    if response.json()["claimed"]:
        print("run main code")
    else:
        print("run register script")

except requests.ConnectionError:
    print("Could not establish a connection")
