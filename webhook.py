import requests
import json

webhook_url = 'http://127.0.0.1:5000/webhook'
data = { 'name' : 'Ghey'}

r = requests.post(webhook_url, data=json.dumps(data), headers = {'Content-Type': 'application/json'})
#https://webhook.site/7b119a58-1dd3-4a5d-aa2e-3119fdf103f7
