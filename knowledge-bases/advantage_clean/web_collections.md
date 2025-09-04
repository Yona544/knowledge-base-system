---
title: Web Collections
slug: web_collections
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: web_collections.htm
source: Advantage CHM
tags:
  - web
checksum: 8427e2c4a0ab5b7abc5232ab9adb9aedc1ccab42
---

# Web Collections

Advantage Web Platform Collections

Collections

Advantage Web Platform

| Collections  Advantage Web Platform |  |  |  |  |

The basic URI for retrieving a collection is shown in the topic [URI Format](web_uri_format.md). $filter, $orderby and paging options are supported to provide the ability to limit result sets and to specify the desired order. For unlimited filtering support via the SQL WHERE clause, you can use the [\_\_Query service](web_query_service_operation.md). Once you obtain a result set, you can use POST and PUT on the collection URI in order to insert and update rows in the table.

For example, if you have a primary key defined, you can get the row with key 5 with:

https://localhost:6282/adsweb/example\_db/v1/Tasks(5)

Or you can use simple data types in filter expressions:

https://localhost:6282/adsweb/example\_db/v1/Tasks(id = 5)

A string key is specified inside single quotes:

https://localhost:6282/adsweb/example\_db/v1/Tasks(Skey = 'test')

Filtering and Ordering

Filtering a collection is performed with the $filter option:

https://localhost:6282/adsweb/example\_db/v1/Tasks?$filter=Skey eq 'test'

Note that the above request returns the same result as the preceding request that uses the primary key predicate. However, the $filter option is more flexible, allowing filtering on non-primary key columns:

https://localhost:6282/adsweb/example\_db/v1/Tasks?$filter=Owner eq 'Engineering' and Status eq 'Started'

The collection may be sorted using the $orderby option:

https://localhost:6282/adsweb/example\_db/v1/Tasks?$filter=Status eq 'Started'&$orderby=Owner

Paging

The request may also specify paging options to limit the number of rows returned by the server. The Advantage Web Platform default is to return 20 rows per request. If there are more rows in the collection, a \_\_next link is returned in the result. The client can reduced the page window using the $top option in the request. For example, the following request will retrieve 10 rows from the collection:

https://localhost:6282/adsweb/example\_db/v1/Tasks?$filter=Owner eq 'Engineering'&$top=10

To retrieve additional rows, the following sequence requests may be used until no more rows are returned:

https://localhost:6282/adsweb/example\_db/v1/Tasks?$filter=Owner eq 'Engineering'&$top=10&$skip=10

https://localhost:6282/adsweb/example\_db/v1/Tasks?$filter=Owner eq 'Engineering'&$top=10&$skip=20

Limiting Columns

The set of columns returned in a collection can be controlled with the $select option.  For example, the following request will return just the Owner and Status columns in the Tasks collection:

https://localhost:6282/adsweb/example\_db/v1/Tasks?$select=Owner,Status

If the $select option is not specified in the URI all columns in the collection will be returned.  To explicitly return all columns in a collection using the $select option, specify a \* as the column list.  For example, this request will return all columns in the collection:

https://localhost:6282/adsweb/example\_db/v1/Tasks?$select=\*
