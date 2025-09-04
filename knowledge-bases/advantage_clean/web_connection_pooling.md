---
title: Web Connection Pooling
slug: web_connection_pooling
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_connection_pooling.htm
source: Advantage CHM
tags:
  - web
checksum: 40a198b4e5e3e0d25f8439998fcb4d291b8461e3
---

# Web Connection Pooling

Connection Pooling

Connection Pooling

Advantage Web Platform

| Connection Pooling  Advantage Web Platform |  |  |  |  |

Connection pooling can be turned on by adding Pooling=true; to the connection string specified by the [DbConnectionString](web_installing_the_awp.md) directive. If this option is not specified, pooling is not enabled.

Connection pooling can provide a significant performance boost in situations where a large number of requests are made to the server. Each request sent to the web server typically results in at least two connections being made to the database server: one to perform authentication and another one to perform the requested operation (e.g., GET, POST, etc.).

If connection pooling is not enabled, then each time a connection is needed by the web server, it must request a new connection from Advantage Database Server. This is relatively expensive and can often far outweigh the cost of the request itself. When pooling is enabled, the web server maintains a pool of connections that can quickly be reused with very little cost.

In addition, each pooled connection maintains a pool of cached statement handles to further reduce the cost of a request.

\_\_ClearConnectionPool

It is possible to clear the connection pool by using the \_\_ClearConnectionPool service operation. This can be useful if it is necessary to perform an action on a table that requires exclusive access. To invoke the \_\_ClearConnectionPool service operation, send a POST request with a URI of the form:

https://hostname:6282/adsweb/<LOCATION>/v1/\_\_ClearConnectionPool

In order for this operation to be allowed, you must be using Database authentication (see DbAuthentication) with either the adssys (admin) user or a user that is a member of the DB:Admin group.
