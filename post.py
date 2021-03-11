import requests
import json

res = requests.post('http://localhost:5000/api/v1/resources/programming/3', json={"title":"C++", "text":"Arduino"})
if res.ok:
    print (res.json())