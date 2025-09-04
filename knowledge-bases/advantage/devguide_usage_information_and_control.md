Usage Information and Control




Advantage Database Server 12  

     Usage Information and Control

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Usage Information and Control  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Usage Information and Control Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Usage\_Information\_and\_Control Advantage Developer's Guide > Part II - Advantage SQL > Chapter 14 - System Management and Metadata > Usage Information and Control / Dear Support Staff, |  |
| Usage Information and Control  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The system stored procedures in this category provide you with information about connections, as well as providing you with general control of access to your databases.

The value of the information returned by these procedures is largely influenced by whether you are using ADS or ALS. When the Advantage Database Server is controlling your data access, these procedures communicate to the server to get information about all current connections, locks, queries, and the like. When used with the Advantage Local Server, only information about the current connection is returned. (Each ALS client is largely unaware of what other ALS clients are doing, unlike with ADS, which provides centralized control for all access for all connections.)

The same is true about the procedures in this category that you use to control usage. For example, when executed against ADS, sp\_mgKillUser can be called from an ADSSYS connection to forcibly terminate a specific user's connection. This procedure has no effect when called from ALS.

On the information side of this category, many of these procedures are designed to let you discover the current server configuration, as well as to get specific details about connected users, active locks, executing queries, and other similar details. For example, you can call sp\_mgGetConnectedUsers to create a table listing all users currently connected to ADS. Similarly, you can call sp\_mgGetTableUsers to learn which users are currently working with a specific table.

Control-oriented procedures in this category permit you to influence the server. For example, as you learned in Chapter 11, sp\_EnableQueryLogging and sp\_DisableQueryLogging allow you to control whether or not queries are logged for a particular database. Similarly, sp\_CancelQuery can be used to terminate a query that is currently executing.

The system stored procedures that you use to discover usage information and exert control over the server are listed in Table 14-12. For detailed information about these procedures, refer to the Advantage help.