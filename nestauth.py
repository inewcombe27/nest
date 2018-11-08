import http.client
import os

conn = http.client.HTTPSConnection("api.home.nest.com")

payload = "code =" + os.environ['AUTH_CODE'] + \
    "&client_id=" + os.environ['PRODUCT_ID']+"&client_secret=" \
    + os.environ['PRODUCT_SECRET'] + "&grant_type=authorization_code"

print (payload)

headers = {'content-type': "application/x-www-form-urlencoded"}

conn.request("POST", "/oauth2/access_token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
