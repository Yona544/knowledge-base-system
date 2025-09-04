Query Logging




Advantage Database Server 12  

     Query Logging

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Query Logging  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Query Logging Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Query\_Logging\_1 Advantage Developer's Guide > Part II - Advantage SQL > Chapter 11 - Introduction to Advantage SQL > Query Logging / Dear Support Staff, |  |
| Query Logging  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage 8 now supports query logging. With query logging enabled, some or even all of the queries executed against the tables of a connection (data dictionary or free tables) are logged. The log for each query identifies the SQL statement that was executed, whether or not the query was optimized, and how long (in milliseconds) the query took to execute, as well as other informative data, such as which user account executed the query.

Query logging is implemented through a set of system stored procedures: sp\_EnableQueryLogging and sp\_DisableQueryLogging. If you are logging queries against a data dictionary, these procedures can only be executed from an ADSSYS connection.

Query logging is a powerful tool for uncovering problem queries. It also increases the amount of work that Advantage must perform during queriessignificantly in some cases. For this reason, query logging is not a feature that you leave enabled for long. For example, if you suspect performance problems in some of your queries in a production application, you typically turn query logging on just long enough to capture several examples of queries whose performance can be improved. Once you have enough data to address performance problems, you turn query logging off.

Query logging can also be employed as part of your pre-deployment strategy. By turning on query logging during your test cycle, you can identify potential performance problems in your applications before they reach your end users.

To enable query logging, execute the system stored procedure sp\_EnableQueryLogging. This procedure requires five parameters. The first parameter is the name of the table that queries will be logged to. This table name is limited to 255 characters. If the named table does not already exist, it will be created once logging starts.

The second parameter is a Boolean parameter. If you pass a value of True, and the logging table already exists when logging starts, any existing log data will be deleted before logging commences. To append new query logs to the existing data, pass a value of False.

The third parameter is also a Boolean parameter. Pass a value of True to log only queries that are not optimized. Since these queries are likely to be of interest, this setting can focus logging on the most potentially problematic queries.

The fourth parameter is an Integer that can also limit which queries are logged. If you want to only log queries that take a long time to execute, pass the minimum number of seconds of execution time before which a query will be logged. Queries that take less than the specified number of seconds are not logged. Pass 0 to log all queries.

If you are enabling query logging on free tables, and your log table is encrypted, use the fifth parameter to pass a CHAR(20) that contains the log table encryption password. If you are enabling query logging on a data dictionary connection, or your free log table is not encrypted, pass a null string.

   
WARNING: SQL queries often contain sensitive data that needs to be protected. For this reason, when logging free tables, it is advisable that your log table be an encrypted table.  
 

The log table that is populated through query logging has the structure described in Table 11-7.

 

|  |  |  |  |
| --- | --- | --- | --- |
| Name | Type | Size | Comments |
| ID | Autoinc | 4 | A unique key for the query |
| Start Time | Timestamp | 8 | Query start timestamp |
| Optimized | Boolean | 1 | True if optimized |
| Return Code | Integer | 4 | Query result code |
| Rows Affected | Integer | 4 | Rows affected by the query |
| End Time | Timestamp | 8 | Query end timestamp |
| Run Time | Double | 8 | Query duration in milliseconds |
| Database | Char | 255 | Database name |
| User Name | Char | 100 | Connected user name |
| Connection Name | Char | 100 | Connection name |
| Application ID | Memo |  | Application ID |
| Query | Memo |  | The SQL statements |

Table 11-7: Structure of the Log Table Resulting from Query Logging

If DemoDictionary is connected and active, you can use the following SQL in the SQL Utility to enable query logging. In this case, queries are logged to the logtable.adt table:

EXECUTE PROCEDURE sp\_EnableQueryLogging('logtable.adt',  
  True, False, 0, '')

The following statement is similar to the previous, except that only unoptimized queries that take longer than 2 seconds to execute will be logged:

EXECUTE PROCEDURE sp\_EnableQueryLogging('logtable.adt',  
  True, True, 2, '')

There are two ways to disable query logging. When you stop the Advantage Database Server and start it again, it always starts with query logging disabled. This prevents you from introducing an inadvertent but permanent performance bottleneck into a production application.

To disable query logging without stopping the server, execute the sp\_DisableQueryLogging system stored procedure. This procedure takes no parameters, but must be executed from the ADSSYS account for data dictionary connections.

   
NOTE: If you enabled query logging on the DemoDictionary connection in order to test query logging, do not forget to disable query logging on this connection when you are through testing.  
 

Advantage also provides a system stored procedure that permits you to view which connections are currently logging queries. This system stored procedure is sp\_ViewQueryLogging, and it also takes no parameters.

Figure 11-8 shows the result set returned by executing sp\_ViewQueryLogging from the SQL Utility when the DemoDictionary connection is logging queries. The Database column contains the names of the data dictionaries for which query logging has been enabled, and the Table field lists the log table to which query information is being written.

Figure 11-8: The procedure sp\_ViewQueryLogging reports which databases are logging queries