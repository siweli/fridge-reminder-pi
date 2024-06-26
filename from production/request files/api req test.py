#& ".venv/Scripts/Activate.ps1"

import requests
from uuid import getnode
import re

mac_add = str(getnode())+"t"
print(mac_add)

url = "http://localhost:3000/api/pi/regdevice"
data = {"data" : mac_add}

try:
    reponse = requests.post(url, json=data)
    print(reponse.json())
except requests.ConnectionError:
    print("Could not establish a connection")
