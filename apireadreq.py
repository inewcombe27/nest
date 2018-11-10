import requests
import os
import json
# from urllib.parse import urlparse



# url = "https://developer-api.nest.com/"
#
# token = os.environ['AUTH_TOKEN']  # Update with your token
#
# headers = {'Authorization': 'Bearer {0}'.format(token), 'Content-Type': 'application/json'}
#
# response = requests.get(url, headers=headers, allow_redirects=False)
#
# if response.status_code == 307:
#     response = requests.get(response.headers['Location'], headers=headers, allow_redirects=False)

# print (response.text)
token = {'Authorization': 'Bearer {0}'.format(os.environ['AUTH_TOKEN']),
         'Content-Type': 'application/json'}  # Update with your token


resp = requests.get('https://developer-api.nest.com/', headers=token,
                    allow_redirects=False)

if response.status_code == 307:
     response = requests.get(response.headers['Location'], headers=headers, allow_redirects=False)

print (response.text)

# if r.status == 307:
#     redirectLocation = urlparse(response.getheader("location"))
#     conn = http.client.HTTPSConnection(redirectLocation.netloc)
#     conn.request("GET", "/", headers=headers)
#     response = conn.getresponse()
#     if response.status != 200:
#         raise Exception("Redirect with non 200 response")

# data = r.text
