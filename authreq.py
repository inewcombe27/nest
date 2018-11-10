import requests
import os
import config

payload = {'code': os.environ['AUTH_CODE'],
           'client_id': config.client_id, 'client_secret':
           config.client_secret, 'grant_type': 'authorization_code'}

print (payload)

authr = requests.post('https://api.home.nest.com/oauth2/access_token',
                      params=payload)

authcode = authr.json()

print (authcode['access_token'])

os.environ['AUTH_TOKEN'] = authcode['access_token']
