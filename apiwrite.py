import requests
import config


def thermo_write(dev_id, tparm, tvalue):
    url = "https://developer-api.nest.com/devices/thermostats/" + dev_id

    token = config.auth_token  # Update with your token

    # payload = "{'\\' tparm: tvalue '\\'}"
    payload = "{\"" + tparm + ":\"" + tvalue + "\"""}"
    print (payload)
    headers = {'Authorization': 'Bearer {0}'.format(token),
               'Content-Type': 'application/json'}

    response = requests.put(url, headers=headers, data=payload,
                            allow_redirects=False)
    print (response.url)

    if response.status_code == 307:  # indicates a redirect is needed
        response = requests.put(response.headers['Location'],
                                headers=headers, data=payload,
                                allow_redirects=False)
    print(response.text)


thermo_write(config.down_id, "target_temperature_f", "69")
