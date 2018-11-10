import requests
from urllib.parse import urlparse
import json
import os
import authorization_code

token = "c.7g6kZcnQY41pYILaNqZMYYXcLNYIfSjbnCAKYLYAGX6KZ1R6iLCPT0E1oH1UIh6JL7ph9Xi56IYhAYcsxbqASpwJVnu8x0ZwnOP3FcbUOR7fWtmUcZppUFBs9msfIVCGfYfKtXiEUbsvbvYx"  # Update with your token

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
