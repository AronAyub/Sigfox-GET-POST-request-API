# Doing request 
# Consuming open source APIs
# import requests module

#import requests
#response  = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
#print(response) # Get 200 as response for a correct Request.
#print(response.json()) # Print JSON data from the requested URL

# Getting Data from Sigfox Backened using API.

import requests

login = "username"
password = "loginpassword"
authentication = (login, password)
response = requests.get("https://api.sigfox.com/v2/devices/device-ID/messages",auth=authentication) 

print(response)

# The variable response contains the response from the server

