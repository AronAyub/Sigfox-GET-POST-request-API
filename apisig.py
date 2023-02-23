import requests
parameters = {"lat": 43.52, "lng": 1.55, "radius": 200}
login = "63f5edb8fecdeb76b337b802"
password = "44bd9e69742f6240ce53f643043261db"
authentication = (login, password)
response = requests.get("https://api.sigfox.com/v2/coverages/global/predictions", auth=authentication, params=parameters)
print(response.iter_content())
print(response.json())
# The variable response contains the response from the server