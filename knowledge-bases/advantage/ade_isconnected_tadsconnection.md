IsConnected




Advantage Database Server 12  

TAdsConnection.IsConnected

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.IsConnected  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.IsConnected Advantage TDataSet Descendant ade\_Isconnected\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.IsConnected  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies whether or not the connection has been established.

Syntax

property IsConnected: Boolean;

Description

Use IsConnected to determine or set a connection.

Setting IsConnected to True:

|  |  |
| --- | --- |
| · | Triggers the OnConnect event handler if one is defined for the connection component. |

|  |  |
| --- | --- |
| · | Opens a connection to the server. |

If an error occurs during the getting of the connection, IsConnected is set to False.

Note Setting the Active property of a TAdsTable attached to a TAdsConnection component to True will cause the TAdsConnection component to request a connection.

See also

[IsConnectionAlive](ade_isconnectionalive_tadsconnection.htm)