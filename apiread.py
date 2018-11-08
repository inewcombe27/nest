import http.client
from urllib.parse import urlparse

token = 'c.7ESa5B1r9fv6RTMtw8gr4dgqvltmKyM5jdTG7hWJ0BgfEx1kBfY46zINwA5fSmeblorJPV7fEPVJ7n4QFsklq5wm3YtTnZl85DvYZTDfBlR83YCGQ5fgzbhkrVWKIZvxOihUPqOCJzplohlA'  # Update with your token

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
