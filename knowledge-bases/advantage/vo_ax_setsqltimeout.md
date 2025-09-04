AX\_SetSQLTimeout()




Advantage Database Server 12  

AX\_SetSQLTimeout()

Advantage SQL RDDs

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_SetSQLTimeout()  Advantage SQL RDDs |  |  | Feedback on: Advantage Database Server 12 - AX\_SetSQLTimeout() Advantage SQL RDDs vo\_Ax\_setsqltimeout Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_SetSQLTimeout() / Dear Support Staff, |  |
| AX\_SetSQLTimeout()  Advantage SQL RDDs |  |  |  |  |

Syntax

AX\_SetSQLTimeout( AS DWORD )

Returns

The previous SQL Timeout setting.

Description

This function specifies the SQL Timeout setting to use when executing SQL Statements and working with resulting cursors. By default, no timeout is used and SQL operations will be allowed to execute indefinitely. When a timeout value is specified, any query whose execution exceeds the timeout value will be cancelled, and an error 7209 (SQL query aborted by user) is returned to the client.

NOTE: This function is only valid for use with the Advantage SQL RDDs (AXSQLNTX, AXSQLCDX, AXSQLVFP, and AXSQLADT).

See also

[AdsSetSQLTimeout](ace_adssetsqltimeout.htm)