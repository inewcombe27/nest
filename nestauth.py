import http.client

conn = http.client.HTTPSConnection("api.home.nest.com")

payload = "code=AUTH_CODE&client_id=CLIENT_ID&client_secret=CLIENT_SECRET&grant_type=authorization_code"

print (payload)

headers = {'content-type': "application/x-www-form-urlencoded"}

conn.request("POST", "/oauth2/access_token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
