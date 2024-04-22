#& ".venv/Scripts/Activate.ps1"

import requests
from uuid import getnode

# device token
dev_token = str(getnode())

url = "http://localhost:3000/api/getcontents"
data = {"data" : dev_token}

try:
    response = requests.post(url, json=data)
    contents = response.json()["contents"]

    for i in contents:
        print(i["name"], i["expires"])


except requests.ConnectionError:
    print("Could not establish a connection")
