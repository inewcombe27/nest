import http.client

conn = http.client.HTTPSConnection("api.home.nest.com")

payload = "code=5QMYQ6YP&client_id=445f81da-c1b5-4c18-a8bd-39c241c5ff24&client_secret=5M3RGmvgCpsMloSBMca5kwyj6&grant_type=authorization_code"

print (payload)

headers = {'content-type': "application/x-www-form-urlencoded"}

conn.request("POST", "/oauth2/access_token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
