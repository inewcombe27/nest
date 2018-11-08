import http.client
import os

conn = http.client.HTTPSConnection("api.home.nest.com")

payload = "code=" + os.environ['AUTH_CODE'] + \
    "&client_id=" + os.environ['PRODUCT_ID']+"&client_secret=" \
    + os.environ['PRODUCT_SECRET'] + "&grant_type=authorization_code"

#print (payload)

headers = {'content-type': "application/x-www-form-urlencoded"}


def get_auth(code):
    conn.request("POST", "/oauth2/access_token", payload, headers)
    res = conn.getresponse()
    code = res.read()
    print (code.decode("utf-8"))


get_auth

#print(code.decode("utf-8"))
