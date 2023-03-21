
// This is Javascript code to execute the same functionality.
// You can try java if you are a fun.
//

URIBuilder builder = new URIBuilder(); builder.setScheme("http").setHost("https://api.sigfox.com").setPath("/v2/devices/32F7A8/messages")
URI uri = builder.build();
String user = "xxxxxxxxxxxxxxxxxxxxx";
String pwd = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx";
HttpGet httpget = new HttpGet(uri);
httpGet.addHeader("Authorization", "Basic " + Base64.encodeToString((user + ":" + pwd).getBytes(), Base64.NO_WRAP));

response = httpget.getURI();
System.out.println(response);
// The variable response contains the response from the server


// another Java code worth trying 

