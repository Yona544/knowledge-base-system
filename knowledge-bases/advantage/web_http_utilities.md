Advantage Web Platform HTTP Utilities




Advantage Database Server 12  

HTTP Utilities

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| HTTP Utilities  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - HTTP Utilities Advantage Web Platform web\_HTTP\_Utilities Advantage Web Development > Advantage Web Platform > HTTP Utilities / Dear Support Staff, |  |
| HTTP Utilities  Advantage Web Platform |  |  |  |  |

Sometimes it can be difficult to determine why an HTTP request to an OData server is not working as expected or what is contained in the result. Here are a couple of utilities that may be useful for debugging purposes.

Fiddler

Fiddler is a utility that can be used to sniff traffic between the client and server. It works at a higher level than some sniffing utilities and can display HTTP(S) requests and responses.  It can also be used for generating test requests based on captured traffic. See <http://fiddler2.com/fiddler2/>

Curl

Curl is useful for sending requests from the command line. Curl can be downloaded from http://curl.haxx.se/  Be sure to download a version that supports SSL.

You will want to use the -k option if you are using a self-signed certificate, this will allow access to the untrusted site.

The URL needs to be manually URL encoded. It may also be necessary (depending on your command line prompt ) to escape the % a second time. The following command is an example:

curl -k --basic --user adssys:thepasswd --url https://localhost:6282/adsweb/pupdir/v1/query/select%20\*%20from%20test7z

The following example (e.g., with TCC uses two % characters):

curl -k --basic --user adssys:thepasswd --url https://localhost:6282/adsweb/pupdir/v1/query/select%%20\*%%20from%%20test7z

Posting JSON data with Curl can be done as well, but you need to escape the quote characters inside the JSON data with a backslash. For example to insert a row:

curl -k --basic --user adssys:thepasswd --url https://localhost:6282/adsweb/pupdir/v1/test7z --data "{\"\_\_metadata\":{\"uri\":\"\",\"key\_fields\":\"\"},\"character\":\"inserted guy\"}"

If you do not have an adssys password assigned you can simply provide --user adssys: for the username parameter (note the colon on the end).