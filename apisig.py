# Doing request 
# Consuming open source APIs
# import requests module

#import requests
#response  = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
#print(response) # Get 200 as response for a correct Request.
#print(response.json()) # Print JSON data from the requested URL

# Getting Data from Sigfox Backened using API.


import requests

login = "63f7ce5c33d968201d7f4e45"
password = "0aa5beba30af812055c135f9fe6b5c6d"
authentication = (login, password)
response = requests.get("https://api.sigfox.com/v2/devices/32F7A8/messages",auth=authentication) 

print(response.json())


# The variable response contains the response from the server


