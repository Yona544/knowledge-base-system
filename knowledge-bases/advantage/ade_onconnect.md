OnConnect




Advantage Database Server 12  

TAdsConnection.OnConnect

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.OnConnect  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.OnConnect Advantage TDataSet Descendant ade\_Onconnect Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.OnConnect  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

OnConnect occurs when an application makes a request to get a connection.

Syntax

type TNotifyEvent = procedure of object;

 

property OnConnect: TNotifyEvent;

Description

Write an OnConnect event handler to take specific action when an application makes a request to get a connection.