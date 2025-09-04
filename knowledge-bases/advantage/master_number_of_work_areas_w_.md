Number of Work Areas (-W)




Advantage Database Server 12  

Number of Work Areas (-W)

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Number of Work Areas (-W)  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - Number of Work Areas (-W) Advantage Database Server master\_Number\_of\_work\_areas\_w\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Number of Work Areas (-W)  Advantage Database Server |  |  |  |  |

Default = (25 x CONNECTIONS) work areas. Range = 1 no upper limit.

This is the initial number of work areas that can be in use at one time.

A work area is a logical "container" that consists of a single open table, an optional memo file, and up to 15 index files. The Number of Work Areas configuration setting on the Advantage Database Server is a per-client setting. That is, one work area must be available for each table opened by every client. For example, if five Advantage clients have opened 10 tables, there must be at least 50 work areas configured on the Advantage Database Server. It does not matter if those 10 tables are the same tables, or if they are completely different tables.

If an SQL statement is executed and is still active, it will consume additional work areas on the connection. The actual number of work areas used by the SQL engine depends on the type of the statement executed. For example, for a SQL statement that returns a cursor (result set) based on a join of two tables, three work areas will be used on the connectionone is used by the client for the cursor and two are used by the server to maintain the two tables used in the join.

If an Advantage application attempts to open a table on the Advantage Database Server, and the configured number of work areas have already been used, the Advantage Database Server will attempt to allocate more resources to accommodate more work areas. If that allocation fails, the Advantage application which is attempting to open that table will receive a 7004 error, Maximum number of work areas exceeded, until a work area "element" becomes available.