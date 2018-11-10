import requests
from urllib.parse import urlparse
import nestauth

token = {'authorization': authreq.authr["access_token"]}  # Update with your token

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
