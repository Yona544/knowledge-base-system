---
title: Web Advantage Web Platform
slug: web_advantage_web_platform
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_advantage_web_platform.htm
source: Advantage CHM
tags:
  - web
checksum: df1312882b6e80d2d7b9bf070876000d2f0bbd10
---

# Web Advantage Web Platform

Advantage Web Platform

Advantage Web Platform

Advantage Web Platform

| Advantage Web Platform  Advantage Web Platform |  |  |  |  |

The Advantage Web Platform is a web service that allows client-less access to Advantage data from any device, platform, or development environment that can make HTTP requests. This includes but is not limited to devices such as desktops/laptops, mobile phones, PDAs, and tablets. It allows access from any current operating system including Mac OS and Android because no Advantage client is required. The Advantage Web Platform extends your application development opportunities and opens up endless possibilities to access Advantage from many different types of architectures, hardware, and business scenarios.

The Advantage Web Platform is a web service built on the standard OData web protocol to access data (<http://www.odata.org>).  The OData standard, follows RESTful principles, and allows you to build web applications that can run in limitless scenarios. You can write one application that can run equally well on an iPhone, Android, or a Windows or Mac desktop machine.

Some web platform features include:

- OData Protocol Support

- Ability to work with multiple [OData Clients](web_service_consumption.md) including .NET, Objective-C (iOS), Android, Silverlight, PHP, Java, and more

- [XML (AtomPub), JSON](web_result_set_format.md), and [JSONP](web_jsonp.md) Support

- [Read](web_uri_format.md) and [Update](web_update_operations.md) Operations

- [Connection and Statement Caching](web_connection_pooling.md)

- [Batch support](web_batch_operations.md)

- [Filter support](web_collections.md)

- [OrderBy query support](web_collections.md)

- [Metadata support](web_metadata.md)

- Unicode support

- [Referential Integrity support](web_referential_integrity.md)

- Off-line data storage synchronization through OData reference caching ([delta support](web_delta_operations.md))

- [Stored Procedure](web_stored_procedures.md) support via service operations

- Chunked HTTP requests (handled automatically by most clients as required)

- Tunneled HTTP requests (handled automatically by most clients as required)

- MIME encoding of binary updates

- [Full SQL query support](web_query_service_operation.md) (optional)

- [Pass-through query](web_pass_through_queries.md) support

The Advantage Web Platform is a web service packaged and built on a stand alone light Apache Web Server module. It is written in C and uses the Advantage Client Engine (ACE) to communicate from the web server to Advantage Database Server.  The web service can run on the same hardware as ADS or different hardware on different networks. Communication between the web service and ADS is through Inter-Process Communication (IPC), Transmission Control Protocol (TCP), or User Datagram Protocol (UDP). Clients communicate with the Advantage Web Platform through HTTP and XML or JSON based on the Open Data Protocol (OData) standard (<http://www.odata.org>).
