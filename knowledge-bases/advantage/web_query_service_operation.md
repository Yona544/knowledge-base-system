Advantage Web Platform \_\_Query Service




Advantage Database Server 12  

\_\_Query Service Operation

Advantage Web Platform

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| \_\_Query Service Operation  Advantage Web Platform |  |  | Feedback on: Advantage Database Server 12 - \_\_Query Service Operation Advantage Web Platform web\_query\_service\_operation Advantage Web Development > Advantage Web Platform > Query Service / Dear Support Staff, |  |
| \_\_Query Service Operation  Advantage Web Platform |  |  |  |  |

NOTE: For security purposes, the query service operation is disabled by default.  If you would like to execute queries, the suggested approach is to use views in your database. This helps limit the kind of operations consumers can use your service for, and prevents users from constructing ad hoc queries that could adversely affect server performance. To enable the query service, you must provide the [DbEnableQueryService](web_installing_the_awp.htm) directive in the desired Location entry in adsweb.conf. If you do enable the query service, you might consider adding "SQLTimeout=30;" to the [DbConnectionString](web_installing_the_awp.htm) to limit the processing time any one query can use to help avoid denial of service attacks.

The \_\_query service can be consumed in two basic fashions; SQL in the URL, and SQL in the payload. Both methods are described below.

\_\_Query with SQL in the URI

An SQL query string is passed in the URL as an http query param named statement. A few examples:

https://localhost:6282/adsweb/example/v1/\_\_query?statement=select \* from mytable

A note about URL encoding: For readability, these examples are not using URL encoding. Most browsers and client libraries will URL encode for you when you send a request. Some will not. The example above URL-encoded would look like: https://localhost:6282/adsweb/example/v1/\_\_query?statement=select%20\*%20from%20mytable

Parameters can be passed as http query params:

.../\_\_query?statement=select \* from mytable where id = :id&id=42

Result sets can be limited via the OData style $top query option:

.../\_\_query?statement=select \* from mytable&$top=10

Multiple http query params are supported as in standard web requests (separated with the & char).

.../\_\_query&statement=select \* from mytable where salary > :sal&sal=36000&$top=10

SQL scripts are supported, just separate SQL statements with a semicolon.

.../\_\_query?statement=insert into t1 values (1);insert into t1 values (2)

\_\_Query with SQL in the Payload

Queries can be passed in the HTTP payload as a JSON object. You call the \_\_query service using a POST method and posting the JSON string in the body:

{

"querystring":"select lastname from tbl where empid < :empid and lastname = :lastname",

"parameters":[{"name":"lastname","value":"Coles"},{"name":"empid","value":"5"}]

}

 

Inserts, Updates and Deletes

All are supported, and return some metadata (rows\_affected and last\_autoinc), but they do not currently return a JSON representation of the rows modified. For example, you will likely want the rowversion of the new rows, which can be used to implement optimistic locking. This functionality is planned for a later update.

For now, you can use an SQL script to explicitly request the new row data after an update. For example, in the following script, rv is a rowversion field used to determine if a row was updated by another user after we last read the record:

update test4 set branch = '1' where empid = :empid and rv = :rv;select \* from test4 where empid = :empid;

When the results are returned, you can check the \_\_metadata.rows\_affected value to verify 1 row was updated. If not, that means the rv field was not the same, meaning another user has modified this row since we last read it. In addition to the rows\_affected value, the result set will also include a fresh copy of the row.