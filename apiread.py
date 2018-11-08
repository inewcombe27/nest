import http.client
from urllib.parse import urlparse
import get_auth

token = get_auth.code  # Update with your token

conn = http.client.HTTPSConnection("developer-api.nest.com")
headers = {'authorization': "Bearer {0}".format(token)}
conn.request("GET", "/", headers=headers)
response = conn.getresponse()

if response.status == 307:
    redirectLocation = urlparse(response.getheader("location"))
    conn = http.client.HTTPSConnection(redirectLocation.netloc)
    conn.request("GET", "/", headers=headers)
    response = conn.getresponse()
    if response.status != 200:
        raise Exception("Redirect with non 200 response")

data = response.read()
print(data.decode("utf-8"))
