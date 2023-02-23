# import requests module

import requests
import json
from requests.auth import HTTPBasicAuth

url = "https://api.sigfox.com/v2/devices/79C030/messages"

#response  = requests.get("https://api.ipify.org?format=json")

response = requests.get(url,auth=HTTPBasicAuth('63f5edb8fecdeb76b337b802','44bd9e69742f6240ce53f643043261db'),data=json.dumps(body), headers={'content-type': 'application/json'})
print(response)



# from requests.auth import HTTPBasicAuth
# user = 63f5edb8fecdeb76b337b802
# pass = 44bd9e69742f6240ce53f643043261db

# Making a get request
# response = requests.get('https://api.sigfox.com/v2/devices/79C030/messages/',
			#auth = HTTPBasicAuth('user', 'pass'))

# print request object




