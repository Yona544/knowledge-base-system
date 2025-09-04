Advantage Web Platform




Advantage Database Server 12  

Advantage Web Platform

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Web Platform  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - Advantage Web Platform Advantage Web Platform web\_advantage\_web\_platform Advantage Web Development > Advantage Web Platform / Dear Support Staff, |  |
| Advantage Web Platform  Advantage Web Platform |  |  |  |  |

The Advantage Web Platform is a web service that allows client-less access to Advantage data from any device, platform, or development environment that can make HTTP requests. This includes but is not limited to devices such as desktops/laptops, mobile phones, PDAs, and tablets. It allows access from any current operating system including Mac OS and Android because no Advantage client is required. The Advantage Web Platform extends your application development opportunities and opens up endless possibilities to access Advantage from many different types of architectures, hardware, and business scenarios.

The Advantage Web Platform is a web service built on the standard OData web protocol to access data (<http://www.odata.org>).  The OData standard, follows RESTful principles, and allows you to build web applications that can run in limitless scenarios. You can write one application that can run equally well on an iPhone, Android, or a Windows or Mac desktop machine.

Some web platform features include:

|  |  |
| --- | --- |
| · | OData Protocol Support |

|  |  |
| --- | --- |
| · | Ability to work with multiple [OData Clients](web_service_consumption.htm) including .NET, Objective-C (iOS), Android, Silverlight, PHP, Java, and more |

|  |  |
| --- | --- |
| · | [XML (AtomPub), JSON](web_result_set_format.htm), and [JSONP](web_jsonp.htm) Support |

|  |  |
| --- | --- |
| · | [Read](web_uri_format.htm) and [Update](web_update_operations.htm) Operations |

|  |  |
| --- | --- |
| · | [Connection and Statement Caching](web_connection_pooling.htm) |

|  |  |
| --- | --- |
| · | [Batch support](web_batch_operations.htm) |

|  |  |
| --- | --- |
| · | [Filter support](web_collections.htm) |

|  |  |
| --- | --- |
| · | [OrderBy query support](web_collections.htm) |

|  |  |
| --- | --- |
| · | [Metadata support](web_metadata.htm) |

|  |  |
| --- | --- |
| · | Unicode support |

|  |  |
| --- | --- |
| · | [Referential Integrity support](web_referential_integrity.htm) |

|  |  |
| --- | --- |
| · | Off-line data storage synchronization through OData reference caching ([delta support](web_delta_operations.htm)) |

|  |  |
| --- | --- |
| · | [Stored Procedure](web_stored_procedures.htm) support via service operations |

|  |  |
| --- | --- |
| · | Chunked HTTP requests (handled automatically by most clients as required) |

|  |  |
| --- | --- |
| · | Tunneled HTTP requests (handled automatically by most clients as required) |

|  |  |
| --- | --- |
| · | MIME encoding of binary updates |

|  |  |
| --- | --- |
| · | [Full SQL query support](web_query_service_operation.htm) (optional) |

|  |  |
| --- | --- |
| · | [Pass-through query](web_pass_through_queries.htm) support |

The Advantage Web Platform is a web service packaged and built on a stand alone light Apache Web Server module. It is written in C and uses the Advantage Client Engine (ACE) to communicate from the web server to Advantage Database Server.  The web service can run on the same hardware as ADS or different hardware on different networks. Communication between the web service and ADS is through Inter-Process Communication (IPC), Transmission Control Protocol (TCP), or User Datagram Protocol (UDP). Clients communicate with the Advantage Web Platform through HTTP and XML or JSON based on the Open Data Protocol (OData) standard (<http://www.odata.org>).