Direct Table Access in ADO.NET




Advantage Database Server 12  

Direct Table Access in ADO.NET

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Direct Table Access in ADO.NET  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - Direct Table Access in ADO.NET Advantage .NET Data Provider dotnet\_Direct\_table\_access\_in\_ado\_net Advantage .NET Data Provider > Introduction > Direct Table Access in ADO.NET / Dear Support Staff, |  |
| Direct Table Access in ADO.NET  Advantage .NET Data Provider |  |  |  |  |

While ADO.NET uses a disconnected data model, it is often very convenient to have direct access to a table. The [AdsExtendedReader](dotnet_adsextendedreader.htm) class can be used to perform advanced table navigation, indexed searches, scopes, filters, locks and direct data manipulation.

While this class is a descendant of the AdsDataReader class, its functionality is not limited to reading data. It is basically a class that exposes much of the Advantage ISAM functionality to ADO.NET users, and is part of what makes Advantage unique.

The AdsExtendedReader class provides direct access to tables, elminating the need to read an entire result set into an in-memory dataset on the client. Because it supports ISAM functionality, it can also provide the functionality necessary to migrate legacy code to the ADO.NET framework.