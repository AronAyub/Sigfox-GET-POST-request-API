# Working With GET API In Sigfox Backend


## Introduction 
APIs access in Sigfox Backend is restricted to authenticated API user, the first step to access API is to **generate API** credentials. Generating API can be done by your SO in the Sigfox Backend. API credentials are *name,* & *applicable time zone*. Accessible API methods and output response will be determined by the *roles* which are set for API credential. E,g *Read only* will allow you to access reading of the data only.
API with Device *Manger[W]* is one of useful API for device management which allows registration or moving devices, creating and editing callbacks and accessing a device's PAC, etc.

More on REST request for POST, GET, DELETE, PUT HTTP requests used are widely covered in the full documentation
### Useful Documentation

- [support-Sigfox](https://support.sigfox.com/docs/apidocs))
- [V2 Documentation](https://support.sigfox.com/document/api-documentation)
- [HTTP Satus](https://support.sigfox.com/docs/api-response-code-references)

### Highlight:

- No pooling message and device sync status through API
- Reasonable API calls according to fleet
- Retrieve message and device status by Callback
- Reasonable callbacks per Device type

## HTTPS GET REQUEST PYTHON SCRIPT 
This API is very much useful for data consumption.
#### Consuming open Source data
Start by consuming unauthenticated APIs. In python, a few lines of code are used to do this:

```
# Consuming open source APIs
# import requests module

import requests
response  = requests.get("https://datausa.io/api/data?drilldowns=Nation&measures=Population")
print(response) # Get 200 as response for a correct Request.
print(response.json()) # Print JSON data from the requested URL
```
## GET REQUEST Using SigfoxAPI
- To demonstrate  the GET Request, i am retriving a **list of messages** , this can be found in [API](https://support.sigfox.com/apidocs#operation/getDeviceMessagesListForDevice) documentation.

<img width="972" alt="screen1" src="https://user-images.githubusercontent.com/55284959/221021827-e70c367a-6513-4762-89a5-704fd7454417.png">

So far there are two methods i found when using Python.
### Direct Method
Involves having the *auth* parameters directly embedded in the code.
### Enconded method
Using encoded method to hide your password in the code.


### Python Scripts to obtain JSON Data
Install and Import Requests 
```
pip install requests
```
Import Request 
```
import requests
```
Define your auntentication variables from your API
```
login = "yourapiusername"
password = "yourapipassword"
```
Assign your login and password a variable.
```
authentication = (login, password)
```
From the sample we are using our API format is: https://api.sigfox.com/v2/devices/{id}/messages, rreplace id with your device ID, should be in Hex.

Below is the url format and how you pass the authentication details.
I am using auth module to pass my authentication details.
```
response = requests.get("https://api.sigfox.com/v2/devices/id/messages",auth=authentication) 
print(response.json())
```
##### Sample returned data with my device ID and API defined 

<img width="759" alt="SCREEN2" src="https://user-images.githubusercontent.com/55284959/221025177-9c494a04-5f4f-4294-b29f-157ebf3b5b74.png">

**Same *auth parsing* should apply for other HTTPs Request, unless specified otherwise in the documentations**