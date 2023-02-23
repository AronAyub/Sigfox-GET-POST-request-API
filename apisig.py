import requests
parameters = {"lat": 43.52, "lng": 1.55, "radius": 200}
login = "63f5edb8fecdeb76b337b802"
password = "44bd9e69742f6240ce53f643043261db"
authentication = (login, password)
response = requests.get("https://api.sigfox.com/v2/devices/79C030/messages", auth = authentication, params = parameters)
print(response.json())
# The variable response contains the response from the server