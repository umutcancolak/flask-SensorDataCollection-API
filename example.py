import requests
import json

def post(endpoint, data):
    header = {
        "Content-Type":"application/json",
        }
    data = json.dumps(data)
    server_url = "http://127.0.0.1:5000" + endpoint
    try:    
        res = requests.post(url = server_url,headers = header,data = data)
        return res.status_code,json.loads(res.content) 
    except:
        return 400

def get(endpoint):
    header = {
        "Content-Type":"application/json",
    }
    server_url = "http://127.0.0.1:5000" + endpoint
    try:    
        res = requests.get(url = server_url,headers = header)
        return res.status_code,json.loads(res.content) 
    except:
        return 400

# Specific sensor id
_id = "1_5"

print("Insert database to {}'s sensor values : ".format(_id), post(
    endpoint = "/sensor/" + _id,
    data = {
        "moisture": 15.3, 
        "temperature" : 23.2 
        }
    )
)
print()
print("{}'s sensor values : ".format(_id), get(endpoint = "/sensor/"+ _id ))
print()
print("All sensor values : ", get(endpoint = "/sensors" ))


