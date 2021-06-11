""" Get Server Version """
import requests
url = "https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/info/serverversion"
headers = {
    'X-auth-access-token': "2abd7bdc-16f8-477f-8022-7f193e71c847",
    }
response = requests.request("GET", url, headers=headers, verify=False)
print(response.text)