Using a Reverse Proxy




Advantage Database Server 12  

Using a Reverse Proxy

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Using a Reverse Proxy  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Using a Reverse Proxy Advantage Web Platform web\_Reverse\_Proxy Advantage Web Development > Advantage Web Platform > Using a Reverse Proxy / Dear Support Staff, |  |
| Using a Reverse Proxy  Advantage Web Platform |  |  |  |  |

Depending on how you deploy and use the Advantage Web Platform, it might be desirable to use a reverse proxy in conjunction with the web server. In general, a reverse proxy is a server that acts as an intermediary (proxy) between the client application and the actual server. At the simplest level, the client sends the request to the proxy, which forwards it on to the server. And the reply is just the opposite:  the server sends the response to the proxy, which forwards it to the client.

One reason to consider using a reverse proxy is for additional security. For example, the proxy can hide the server (or servers) behind it and provide firewall functionality. And because the client application makes requests that are sent to the proxy, it has no knowledge of the actual server, so it is possible to change database locations, server names, etc. without affecting the client application. In addition, a reverse proxy can provide load balancing by redirecting requests to different servers, caching, etc.

With a RESTful service such as OData, there is more work involved for the proxy than to simply forward requests and responses. OData responses commonly have URLs in them that refer to data on the OData server. When the server generates these URLs, it does so without knowledge that a proxy is involved. If these URLs are sent unchanged to the client, then attempts by the client to use those URLs (e.g., in a POST or a GET) would fail unless the client was able to access the server directly, which would defeat much of the purpose of using a proxy. So a form of URL rewriting is necessary; this is described in the example steps given for setting up a reverse proxy.

There are a number of different reverse proxy servers available such as nginx, Squid, PortFusion, and others. Apache also has reverse proxy support available through the mod\_proxy module.

The following briefly describes the steps for setting up Apache as a reverse proxy. It is not meant to be a full tutorial on the subject; there are resources available on the Internet. For example, <http://www.apachetutor.org/admin/reverseproxies> contains useful information about this subject. Note that this particular site focuses much on the mod\_proxy\_html Apache Module, which provides the ability to rewrite URLs within HTML responses. The OData responses require similar rewrites, however, the mod\_proxy\_html module does not help since it only supports HTML.

Install Proxy Server

Install Apache on the server that will host the reverse proxy. For testing purposes, you can use the Advantage Web Platform installation since it installs Apache as part of the process. If you use the Advantage Web Platform installer, do not choose to install the example DB. You may want to choose to create the test SSL certificate in order to test SSL if you do not already have a certificate available.

If you use the Advantage installation, make the following changes to httpd.conf in the apache/conf folder:

|  |  |
| --- | --- |
| · | Comment out (or delete) the "Include conf/adsweb.conf" directive near the bottom. |

|  |  |
| --- | --- |
| · | Comment out (or delete) the "AddType application/x-httpd-php .php" and "PHPIniDir" directives near the bottom of httpd.conf. |

|  |  |
| --- | --- |
| · | Comment out the LoadModule directive for adsweb\_module. |

|  |  |
| --- | --- |
| · | Comment out the LoadModule directive for php5\_module. |

Uncomment (if they aren't already), the LoadModule directives for the following modules:

|  |  |
| --- | --- |
| · | mod\_proxy.so |

|  |  |
| --- | --- |
| · | mod\_proxy\_http.so |

|  |  |
| --- | --- |
| · | mod\_headers.so |

|  |  |
| --- | --- |
| · | mod\_substitute.so |

|  |  |
| --- | --- |
| · | mod\_filter.so |

Specify the desired listen ports in httpd.conf and extra/httpd-ssl.conf.  For example, if you are using the Apache version installed with the Advantage Web Platform, change the listen port in httpd.conf from 6272 to another port if desired. The following examples assume that the port was changed to 8080.

Specify Proxy and URL Rewriting Directives

Add the following configuration directives (e.g., in httpd.conf or in another .conf file that you include):

<Proxy \*>

  Order deny,allow

  Deny from all

  # maybe use an entry such as the following to limit access

  #Allow from 10.6.199

</Proxy>

 

# Important: Be sure to set ProxyRequests to "off"

ProxyRequests off

# Define the rules to route requests to the OData server.  In this

# example, a request sent to this proxy server beginning with /myproxy/ in the

# URL (after the host name) will send requests to the specified address

ProxyPass /myproxy/ http://myodataserver.com:6272/

 

# Define a filter for modifications to the possible response types from the server

FilterDeclare CTSF\_RESP

# You could use the following to hit all content types

#FilterProvider CTSF\_RESP SUBSTITUTE resp=Content-Type \*

 

# Or you can list specific content types, which is probably better.

# The following are the current possible MIME types from the Advantage

# Web Platform. Include the ones that you need.  For example, if you exclusively

# are using JSON, then you may only need the application/json directive. However,

# if you are using batch requests, the multipart/mixed type is also needed.

FilterProvider CTSF\_RESP SUBSTITUTE resp=Content-Type $application/json

FilterProvider CTSF\_RESP SUBSTITUTE resp=Content-Type $application/atom+xml

FilterProvider CTSF\_RESP SUBSTITUTE resp=Content-Type $application/xml

FilterProvider CTSF\_RESP SUBSTITUTE resp=Content-Type $multipart/mixed

 

<Location /myproxy/>

  # This directive maps URLs in HTTP headers back to the proxy address.

  ProxyPassReverse http://myodataserver.com:6272/

  # Handle compression

  SetOutputFilter INFLATE;DEFLATE

 

  # Apply the substitution of the data in the response body (e.g., \_\_next elements,

  # and other embedded URIs).  mod\_proxy only handles changing the

  # top level URI and headers

  # This changes any URIs of the form "http://myoadataserver.com:6272/" to

  # "http://myproxy.com:8080/".

  FilterChain CTSF\_RESP

  Substitute s|http://myodataserver.com:6272/|http://myproxy.com:8080/myproxy/|nq

 

</Location>

After making the changes described above, restart Apache and you should be able to send requests to the proxy server and have them forwarded to the actual OData server.

Using SSL between the client and the reverse proxy is fairly straightforward. You have to install the SSL certificate on the proxy and connect to the port defined in extra\httpd-ssl.conf. Note that, by default, the traffic from the proxy to the server will not be encrypted. If you need to encrypt that traffic as well, it is necessary to use the SSLProxy\* directives of mod\_ssl.  That is not covered in this example. The SSL must be handled at the proxy because of the URL rewriting that it must perform.  If it dealt simply with the encrypted traffic and did not decrypt/encrypt, it would not be able to modify the URLs.