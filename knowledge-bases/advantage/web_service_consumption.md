Service Consumption




Advantage Database Server 12  

Service Consumption

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Service Consumption  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Service Consumption Advantage Web Platform web\_Service\_Consumption Advantage Web Development > Advantage Web Platform > Service Consumption / Dear Support Staff, |  |
| Service Consumption  Advantage Web Platform |  |  |  |  |

Clients

There are many ways to consume and use the data returned from the Advantage Web Platform. Data can be manually parsed, serialized/deserialized with XML/JSON librarys, and OData-specific client libraries can be used. When available for your environment, the OData client libraries are the easiest approach and provide the most functionality (although functionality varies per-client).

There are OData clients for:

|  |  |
| --- | --- |
| · | iOS |

|  |  |
| --- | --- |
| · | Android/Java |

|  |  |
| --- | --- |
| · | Ruby |

|  |  |
| --- | --- |
| · | .NET |

|  |  |
| --- | --- |
| · | PHP |

|  |  |
| --- | --- |
| · | etc. |

See <http://www.odata.org/developers/odata-sdk> for a complete list and documentation. The Advantage Web Platform supports the OData service-level [metadata document](web_metadata.htm), which means consuming the service via an OData client usually just involves pointing the client (or the proxy class generation utility) at the [base URI](web_uri_format.htm) for your service.

Tutorials

Some getting started tutorials and notes for mobile development can be found at:

<http://go.sap.com/solution/platform-technology/mobile-application-development-platform.html>

A tutorial video based on using JavaScript is available at:

<http://devzone.advantagedatabase.com/dz/Screencasts/javascript/JavaScriptWebApp.html>

The source code for the JavaScript demo is installed with the Advantage Web Platform installation under the apache/htdocs folder (e.g., c:\Program Files\Advantage 11.0\adsweb\apache\htdocs).