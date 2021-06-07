""""Get cunstomer details given a customerID"""
import requests

url='https://management.api.umbrella.com/v1/serviceproviders/serviceProviderId/customers/customerId'
headers={
    'accepts':"application/json",
    'authorization':"Basic  ZGV2YXNjOnN0cm9uZ3Bhc3N3b3Jk"
  }
response=requests.request("GET",url,headers=headers)
print(response.text)