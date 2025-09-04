ConnectionType




Advantage Database Server 12  

TAdsConnection.ConnectionType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.ConnectionType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.ConnectionType Advantage TDataSet Descendant ade\_Connectiontype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.ConnectionType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies the type of connection to the server.

Syntax

property ConnectionType: String;

Description

If there is a connection, this property will return that either the AIS (Advantage Internet Server), LOCAL (Advantage Local Server), or REMOTE (Advantage Database Server) is being used. The string returned is not guaranteed to be all upper case, so a case insensitive comparison should be done if you want to do comparison to the return value.If there is no connection, the return string is empty.