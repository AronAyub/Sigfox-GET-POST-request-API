URIBuilder builder = new URIBuilder(); builder.setScheme("http").setHost("https://api.sigfox.com")
.setPath("/v2/devices/32F7A8/messages")

URI uri = builder.build();
String user = "63f7ce5c33d968201d7f4e45";
String pwd = "0aa5beba30af812055c135f9fe6b5c6d";
HttpGet httpget = new HttpGet(uri);
httpGet.addHeader("Authorization", "Basic " + Base64.encodeToString((user + ":" + pwd).getBytes(), Base64.NO_WRAP));

response = httpget.getURI();
// The variable response contains the response from the server