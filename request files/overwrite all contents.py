import requests
from uuid import getnode
import random

mac_add = str(getnode())+"t"

list = [["tomato", "2024-03-12"], ["bread", "2024-03-13"]]

url = "http://localhost:3000/api/receivedevice"
data = {"token":mac_add, "contents":list}

try:
    reponse = requests.post(url, json=data)
    print(reponse.json())
except requests.ConnectionError:
    print("Could not establish a connection")
