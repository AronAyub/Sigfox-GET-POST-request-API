# APIs In Sigfox Backend.

## Introduction 
APIs access in Sigfox Backend is restricted to aunthenticated API user, the first step to access API is to generate API credentials. Generating API can be done by your SO in the Sigfox Backend. API creditials are name, applicable time zone and, the most important part, the accessible roles for this new API. Accessible API methods and output response will be determined by the roles which are set for API credential. E,g Read only will allow you to access reading of the data only.

API with Device Manger[W] is one of useful API for device management which allows registration or moving devices, creating and editing callbacks and accessing a device's PAC, etc.

The REST principle - usage of POST, GET, DELETE, PUT HTTP request used are widely covered in the full documentation
### Useful Documentation

[support-Sigfox](https://support.sigfox.com/docs/apidocs))
[V2 Documentation](https://support.sigfox.com/document/api-documentation)
[HTTP Satus](https://support.sigfox.com/docs/api-response-code-references)

### Highlight:

• No pooling message and device sync status through API
• Reasonable API calls according to fleet
• Retrieve message and device status by Callback
• Reasonable callbacks per Device type

### HTTPS GET REQUEST PYTHON SCRIPT 
- This API is very much useful for data consumption.




### Coverage Prediction API Python Script
This API helps in getting Global Coverage API (single point) to get coverage levels for any location. The API description shows that two mandatory parameters must be provided, and two being optional, lat, lng are mandatory and radius optional.

This helps predict coverage of any location. 
"
```
import requests
parameters = {"lat": 43.52, "lng": 1.55, "radius": 200}
login = "password"
password = "user password"
authentication = (login, password)
response = requests.get("https://api.sigfox.com/v2/coverages/global/predictions", auth=authentication, params=parameters)
print(response.iter_content())
print(response.json())
```
# The variable response contains the response from the server