import http.client
from urllib.parse import urlparse
import nestauth

token = "c.5iXGtBW1m0nhHlu3S9GXyoFUipaZmUIoqGknFLxqAKzIDHxSPai4HvJoCmWXWEozNfyBC60kl7ckQaYdchhaz7xgRKtn5GxnHDcRLKQbbMU9s3TqilWlwvRnGJRW06Voi9yyKWZCmRuoyrnz"  # Update with your token

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
