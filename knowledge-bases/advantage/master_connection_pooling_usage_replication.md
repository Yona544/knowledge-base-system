Connection Pooling Usage




Advantage Database Server 12  

Connection Pooling Usage

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Connection Pooling Usage  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Connection Pooling Usage Advantage Concepts master\_Connection\_pooling\_usage\_replication Advantage Concepts > Advantage Functionality > Replication > Connection Pooling Usage / Dear Support Staff, |  |
| Connection Pooling Usage  Advantage Concepts |  |  |  |  |

Replication requires connections both to the source server and the target server. The connections to the source server are internal connections and do not count against the maximum allowed user count. The connection to the target server is counted on the target as a new user and does count toward the maximum allowed user count.

In both cases, it may be desirable to increase the connection count (see [Advantage Database Server Configuration](master_advantage_database_server_configuration_overview.htm)) at both source and target servers to allow for the additional connections.

To improve performance, a connection pool is used for both types of connections used by the replication processing. After approximately one minute of inactivity, unused connections will be released.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.htm)