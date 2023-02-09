import requests
import json
url = "https://data.mongodb-api.com/app/data-phtlr/endpoint/data/v1/action/findOne"

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
  'api-key': '52iCIhtTWfqdy5q7goZdmirF2MjAUVlBha5pL4qngvwEG8IJ4gxJDmB7flPRuZOT', 
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
