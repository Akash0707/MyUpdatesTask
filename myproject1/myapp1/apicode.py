import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
 r = requests.get(url = URL)
 data = r.json()
 print(data)

 get_data()
