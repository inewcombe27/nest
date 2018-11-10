import requests
import os
import config

url = "https://developer-api.nest.com/devices/thermostats/" + config.down_id

token = config.auth_token# Update with your token

payload = "{\"target_temperature_f\": 70}"

headers = {'Authorization': 'Bearer {0}'.format(token), 'Content-Type': 'application/json'}

response = requests.put(url, headers=headers, data=payload, allow_redirects=False)
if response.status_code == 307: # indicates a redirect is needed
    response = requests.put(response.headers['Location'], headers=headers, data=payload, allow_redirects=False)

print(response.text)
