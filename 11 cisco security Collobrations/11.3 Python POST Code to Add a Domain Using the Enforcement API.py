""" Add domain using the Enforcement API """

import json
import requests

url = "https://s-platform.api.opendns.com/1.0/events"

querystring = {"customerKey":"XXXXXXX-YYYY-ZZZZ-YYYY-XXXXXXXXXXXX"}
payload = [
    {
        "alertTime": "2020-01-01T09:33:21.0Z",
        "deviceId": "deadbeaf-e692-4724-ba36-c28132c761de",
        "deviceVersion": "13.7a",
        "dstDomain": "looksfake.com",
        "dstUrl": "http://looksfake.com/badurl",
        "eventTime": "2020-01-01T09:33:21.0Z",
        "protocolVersion": "1.0a",
        "providerName": "Security Platform"
    }
]

headers = {
    'Content-Type': "text/plain",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "s-platform.api.opendns.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

response = requests.request(
    "POST",
    url,
    data=json.loads(payload),
    headers=headers,
    params=querystring)

print(response.text)