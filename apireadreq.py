import requests
import os

token = {'Authorization': 'Bearer {0}'.format(os.environ['AUTH_TOKEN']),
         'Content-Type': 'application/json'}  # Update with your token


response = requests.get('https://developer-api.nest.com/', headers=token,
                    allow_redirects=False)

if response.status_code == 307:
     response = requests.get(response.headers['Location'], headers=token, allow_redirects=False)

print (response.text)
