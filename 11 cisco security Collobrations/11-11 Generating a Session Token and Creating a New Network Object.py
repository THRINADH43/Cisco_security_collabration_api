""" generate a session token and create a new network object """

import json
import requests

## Globals used in this file
url = "https://fmcrestapisandbox.cisco.com/api/fmc_platform/v1/auth/generatetoken"
server = "https://fmcrestapisandbox.cisco.com"
username = "johnsmith"
password = "pwgDvQt3"
domain = "Global"
token = ""
headers = {
    'Content-Type': "application/json",
}

## Definition of Lab Network (10.10.10.0)

network_lab = {
    "name": "labnetwork-1",
    "value": "10.10.10.0/24",
    "overridable": False,
    "description": "Lab Network Object",
    "type": "Network"
}

def networkOject(network, uuid):
    """ Create a new Network object """

    netpath = "/api/fmc_config/v1/domain/" + uuid + "/object/networks"
    url = server + netpath
    print("-------------------")
    print(headers)
    try:
        response = requests.post(url, data=json.dumps(network), headers=headers,
        verify=False)
        status_code = response.status_code
        resp = response.text
        json_response = json.loads(resp)
        print("status code is: " + str(status_code))
        if status_code == 201 or status_code == 202:
            print("Successfully network created")
        else:
            response.raise_for_status()
        return json_response["name"], json_response["id"]
    except requests.exceptions.HTTPError as err:
        print("Reason Code: " + str(err))
    finally:
        if response:
            response.close()

def generateSessionToken():
    """ Generate a new session token using the username and password """
    global uuid
    global headers
    tokenurl = "/api/fmc_platform/v1/auth/generatetoken"
    url = server + tokenurl
    response = requests.request(
        "POST",
        url,
        headers=headers,
        auth=requests.auth.HTTPBasicAuth(username, password),
        verify=False
    )
    print(response.headers)
    status_code = response.status_code
    if status_code == 201 or status_code == 202:
        print("Successfully network created")
    else:
        response.raise_for_status()

    auth_headers = response.headers
    token = auth_headers.get('X-auth-access-token', default=None)
    headers['X-auth-access-token'] = token
    domains = auth_headers.get('DOMAINS', default=None)
    domains = json.loads("{\"domains\":" + domains + "}")
    for item in domains["domains"]:
        if item["name"] == domain:
            uuid = item["uuid"]
        else:
            print("no UUID for the domain found!")

    print(domains)
    print(uuid)
    print(headers)

## Main - Entry point - Invoke generate token and create network object
if __name__ == "__main__":
    generateSessionToken()
    networkOject(network_lab, uuid)