
// This is Javascript code to execute the same functionality.

URIBuilder builder = new URIBuilder(); builder.setScheme("http").setHost("https://api.sigfox.com")
.setPath("/v2/devices/32F7A8/messages")

URI uri = builder.build();
String user = "username";
String pwd = "apipassword";
HttpGet httpget = new HttpGet(uri);
httpGet.addHeader("Authorization", "Basic " + Base64.encodeToString((user + ":" + pwd).getBytes(), Base64.NO_WRAP));

response = httpget.getURI();
// The variable response contains the response from the server