DataServiceVersion, MaxDataServiceVersion




Advantage Database Server 12  

DataServiceVersion, MaxDataServiceVersion

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| DataServiceVersion, MaxDataServiceVersion  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - DataServiceVersion, MaxDataServiceVersion Advantage Web Platform web\_DataServiceVersion Advantage Web Development > Advantage Web Platform > DataServiceVersion / Dear Support Staff, |  |
| DataServiceVersion, MaxDataServiceVersion  Advantage Web Platform |  |  |  |  |

DataServiceVersion

DataServiceVersion is an HTTP header that specifies which version of the OData spec is being used.  The OData server includes this header with each response to let the client know how to process the response.  A client should include this header to let the server know which version of the spec it supports.  Because the format of a response is different for different versions of the spec, it is important for the client to provide this header.  If the client doesnt provide this header the server will assume it supports the most current version of the spec.  Initially the Advantage OData service only supports version 2.0 of the spec.  Any request for an unsupported version will result in a 4xx class error.

For example:

GET http://odata.example.org/Customers(5) HTTP/1.1

Host: odata.example.org

Connection: keep-alive

User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.152 Safari/535.19

Accept: application/json

Accept-Encoding: gzip,deflate,sdch

Accept-Language: en-US,en;q=0.8

Accept-Charset: ISO-8859-1,utf-8;q=0.7,\*;q=0.3

DataServiceVersion: 2.0

MaxDataServiceVersion

MaxDataServiceVersion is an HTTP header that specifies the maximum version of the OData spec that is supported.  A client should provide this to the server to inform it which version it can support.  If the client only supports one version of the spec, this value should be equal to DataServiceVersion.  If the client specifies a MaxDataServiceVersion that is less than the minimum version the Advantage OData service supports, a 4xx class error is returned.

For example:

GET http://odata.example.org/Customers(5) HTTP/1.1

Host: odata.example.org

Connection: keep-alive

User-Agent: Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.152 Safari/535.19

Accept: application/json

Accept-Encoding: gzip,deflate,sdch

Accept-Language: en-US,en;q=0.8

Accept-Charset: ISO-8859-1,utf-8;q=0.7,\*;q=0.3

DataServiceVersion: 2.0

MaxDataServiceVersion: 2.0