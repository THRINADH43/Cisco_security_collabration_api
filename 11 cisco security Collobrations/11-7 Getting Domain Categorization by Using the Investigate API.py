""" Domains categorization using the Investigate API """

import requests
url = "https://investigate.api.umbrella.com/domains/categorization/cisco.com"
querystring = {"showLabels":""}
headers = {
    'authorization': "Bearer deadbeef-24d7-40e1-a5ce-3b064606166f",
    'cache-control': "no-cache",
    }
response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)