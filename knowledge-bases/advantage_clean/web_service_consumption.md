---
title: Web Service Consumption
slug: web_service_consumption
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_service_consumption.htm
source: Advantage CHM
tags:
  - web
checksum: 7406c09f8d5a6adce72c4b6444e4c9733c5b1be3
---

# Web Service Consumption

Service Consumption

Service Consumption

Advantage Web Platform

| Service Consumption  Advantage Web Platform |  |  |  |  |

Clients

There are many ways to consume and use the data returned from the Advantage Web Platform. Data can be manually parsed, serialized/deserialized with XML/JSON librarys, and OData-specific client libraries can be used. When available for your environment, the OData client libraries are the easiest approach and provide the most functionality (although functionality varies per-client).

There are OData clients for:

- iOS

- Android/Java

- Ruby

- .NET

- PHP

- etc.

See <http://www.odata.org/developers/odata-sdk> for a complete list and documentation. The Advantage Web Platform supports the OData service-level [metadata document](web_metadata.md), which means consuming the service via an OData client usually just involves pointing the client (or the proxy class generation utility) at the [base URI](web_uri_format.md) for your service.

Tutorials

Some getting started tutorials and notes for mobile development can be found at:

<http://go.sap.com/solution/platform-technology/mobile-application-development-platform.html>

A tutorial video based on using JavaScript is available at:

<http://devzone.advantagedatabase.com/dz/Screencasts/javascript/JavaScriptWebApp.html>

The source code for the JavaScript demo is installed with the Advantage Web Platform installation under the apache/htdocs folder (e.g., c:\Program Files\Advantage 11.0\adsweb\apache\htdocs).
