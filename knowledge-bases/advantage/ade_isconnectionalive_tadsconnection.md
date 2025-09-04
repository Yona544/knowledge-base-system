IsConnectionAlive




Advantage Database Server 12  

IsConnectionAlive

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| IsConnectionAlive  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - IsConnectionAlive Advantage TDataSet Descendant ade\_Isconnectionalive\_tadsconnection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| IsConnectionAlive  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Indicates whether the underlying connection to Advantage Database Server is still active.

Syntax

property IsConnectionAlive: Boolean;

Description

IsConnectionAlive is a read-only property that can be used by an application to test if the connection to Advantage Database Server is still usable. If this property returns false, it indicates that the connection has been lost. Reasons for a lost connection include network failure, server failure, Advantage Database Server failure, or cluster node failover. If an application needs to stay connected at all times, it can use this property to test a connection. If the connection is lost, a possible course of action is to close all objects (tables, cursors, SQL statements, and the connection itself) and attempt to reconnect to the server, which may succeed if the server was stopped momentarily or if it is part of a cluster and was moved to another node by the cluster manager.

Note This property will return false if the TAdsConnection.IsConnected property has not been set to true.

See Also

[IsConnected](ade_isconnected_tadsconnection.htm)