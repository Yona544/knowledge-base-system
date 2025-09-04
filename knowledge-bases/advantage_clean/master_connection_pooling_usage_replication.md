---
title: Master Connection Pooling Usage Replication
slug: master_connection_pooling_usage_replication
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_connection_pooling_usage_replication.htm
source: Advantage CHM
tags:
  - master
checksum: 885de7e9aa0669c985ee9895262c964865d17f3f
---

# Master Connection Pooling Usage Replication

Connection Pooling Usage

Connection Pooling Usage

Advantage Concepts

| Connection Pooling Usage  Advantage Concepts |  |  |  |  |

Replication requires connections both to the source server and the target server. The connections to the source server are internal connections and do not count against the maximum allowed user count. The connection to the target server is counted on the target as a new user and does count toward the maximum allowed user count.

In both cases, it may be desirable to increase the connection count (see [Advantage Database Server Configuration](master_advantage_database_server_configuration_overview.md)) at both source and target servers to allow for the additional connections.

To improve performance, a connection pool is used for both types of connections used by the replication processing. After approximately one minute of inactivity, unused connections will be released.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.md)
