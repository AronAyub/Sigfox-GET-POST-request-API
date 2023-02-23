# import requests module
import requests
# url = https://datausa.io/api/data?drilldowns=Nation&measures=Population

response  = requests.get("https://api.ipify.org?format=json")
# from requests.auth import HTTPBasicAuth
# user = 63f5edb8fecdeb76b337b802
# pass = 44bd9e69742f6240ce53f643043261db

# Making a get request
# response = requests.get('https://api.sigfox.com/v2/devices/79C030/messages/',
			#auth = HTTPBasicAuth('user', 'pass'))

# print request object
print(response)

