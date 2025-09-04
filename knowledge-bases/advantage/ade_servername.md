ServerName




Advantage Database Server 12  

TAdsConnection.ServerName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.ServerName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.ServerName Advantage TDataSet Descendant ade\_Servername Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.ServerName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Read-only property that will retrieve the server name that the connection is on.

Syntax

property ServerName: String;

Description

This is the property to retrieve if there is a question as to the name of the server to which TAdsConnection is connected. The connection must be established before getting this property. If accessing data on a local drive and using [Advantage Local Server](master_advantage_local_server.htm), the drive letter is returned.