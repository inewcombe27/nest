import requests
import os
# from urllib.parse import urlparse


token = {'Authorization': 'Bearer {0}'.format(os.environ['AUTH_TOKEN'])}  # Update with your token

r = requests.get('https://developer-api.nest.com', params=token)


# if r.status == 307:
#     redirectLocation = urlparse(response.getheader("location"))
#     conn = http.client.HTTPSConnection(redirectLocation.netloc)
#     conn.request("GET", "/", headers=headers)
#     response = conn.getresponse()
#     if response.status != 200:
#         raise Exception("Redirect with non 200 response")

data = r.text
print(data)
