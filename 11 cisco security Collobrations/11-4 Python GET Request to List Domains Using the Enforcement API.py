""" List domains using the Enforcement API """

import requests
import json
url = "https://s-platform.api.opendns.com/1.0/domains"
querystring = {"customerKey":"XXXXXXX-YYYY-ZZZZ-YYYY-XXXXXXXXXXXX"}
response = requests.request("POST", url, headers=headers, params=querystring)
print(response.text)