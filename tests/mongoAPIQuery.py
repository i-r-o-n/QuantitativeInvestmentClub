import requests
import json
url = ""

payload = json.dumps({
    "collection": "companies",
    "database": "companyBalanceSheet",
    "dataSource": "TestCluster",
    "projection": {
        "_id": 1
    }
})
headers = {
  'Content-Type': 'application/json',
  'Access-Control-Request-Headers': '*',
  'api-key': '', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
