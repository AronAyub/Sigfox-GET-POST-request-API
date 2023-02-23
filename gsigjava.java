URI uri = builder.build();
String user = "5***6";
String pwd = "2***3";
HttpGet httpget = new HttpGet(uri);
httpGet.addHeader("Authorization",
"Basic " + Base64.encodeToString(
(user + ":" + pwd).getBytes(),
Base64.NO_WRAP));
response = httpget.getURI();
// The variable response contains the response from the server