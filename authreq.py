import requests
import os

payload = {'code': os.environ['AUTH_CODE'],
        'client_id': os.environ['PRODUCT_ID'], 'client_secret': os.environ
        ['PRODUCT_SECRET'], 'grant_type': 'authorization_code'}

print (payload)

auth = requests.post('https://api.home.nest.com/oauth2/access_token',
        params=payload)

print (r.url)
