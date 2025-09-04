---
title: Web Pass Through Queries
slug: web_pass_through_queries
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_pass_through_queries.htm
source: Advantage CHM
tags:
  - web
checksum: b0f65e699a948146d6bcc5e53242d449bfaeec9e
---

# Web Pass Through Queries

Pass-through Queries

Pass-through Queries

Advantage Web Platform

| Pass-through Queries  Advantage Web Platform |  |  |  |  |

When making requests to a [root dictionary](master_root_dictionary.md), it is possible to run queries against other databases. The primary reason for this is to provide additional management functionality through the Advantage  Web Administrator utility. The idea behind this functionality is to be able to expose a single root dictionary for configuration purposes yet still be able to run queries against other data dictionaries without exposing them directly via a Location in adsweb.conf.

When using pass-through queries, the following restrictions apply.

- The query must made through a [root dictionary](master_root_dictionary.md).

- The [\_\_Query service](web_query_service_operation.md) operation must be enabled on the root dictionary ([DbEnableQueryService)](web_installing_the_awp.md).

- Pass-through queries must be allowed on the target dictionary.  See the [root dictionary](master_root_dictionary.md) topic and QUERY\_VIA\_ROOT in [sp\_ModifyDatabase](master_sp_modifydatabase.md).

- The target dictionary must be on the same physical server as the root dictionary.

A pass-through query is signified by including the "ConnectionString" parameter in the URI as part of a GET request or in the body of a POST request. Note that the ConnectionString parameter can be used with [stored procedure](web_stored_procedures.md) calls as well to pass them through to another dictionary. The given connection string must be a full connection string including Data Source, credentials, communications type if necessary, etc.

The following is an example POST with the ConnectionString included in the body to another server:

POST https://myserver.com:6282/adsweb/rootdd/v1/\_\_query?$format=json HTTP/1.1

Authorization: Basic YWRzc3lzOg==

Host: myserver.com:6282

Content-Length: 235

Expect: 100-continue

Connection: Keep-Alive

 

{"querystring":"select \* from sometable where i = :constant;","ConnectionString":" servertype=ads\_remote\_server; pooling=true; Data Source=\\\\myserver\\mypath\\test.add;user id=adssys","parameters":[{"name":"constant","value":"123"}]}

The following shows the same example but passes the pass-through connection string as part of the URI:

GET https://myserver.com:6282/adsweb/rootdd/v1/\_\_query?statement=select%20\*%20from%20sometable%20where%20i%20=%20:constant;&constant=123&connectionstring=%20servertype=ads\_remote\_server;pooling=true;%20Data%20Source=%5C%5Cmyserver%5Cmypath%5Ctest.add;user%20id=adssys&$format=json HTTP/1.1
