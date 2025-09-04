OnDisconnect




Advantage Database Server 12  

TAdsConnection.OnDisconnect

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.OnDisconnect  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.OnDisconnect Advantage TDataSet Descendant ade\_Ondisconnect Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.OnDisconnect  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

OnDisconnect occurs when an application makes a request to release a connection.

Syntax

type TNotifyEvent = procedure of object;

 

property OnDisconnect: TNotifyEvent;

Description

Write an OnDisconnect event handler to take specific action when an application makes a request to release a connection.