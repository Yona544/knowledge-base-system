Replication and Connections




Advantage Database Server 12  

     Replication and Connections

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Replication and Connections  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Replication and Connections Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Replication\_and\_Connections Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 10 - Replication > Replication and Connections / Dear Support Staff, |  |
| Replication and Connections  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

When a record is modified in a published table, that record is written to the queue table. An ADS thread uses a connection to the target database from a connection pool to perform the data transfer. This transfer is always in the form of a parameterized SQL INSERT, UPDATE, or DELETE statement. If the record is successfully updated on the target, the record is deleted from the queue table.

Sometimes records in the queue table cannot be replicated. For example, if the source data dictionary loses its connection to the target data dictionary, the queue receives records but cannot replicate them.

Normally, over time, a connection can be reestablished and the queue table records will be replicated to the target; that is, unless the last connection to the data dictionary for the source data dictionary is disconnected before the queue table can be emptied. In this case, the queue table records will remain in the source database until replication can begin again.

There are two mechanisms that will restart replication following the last disconnect from a data dictionary. The most common is that a client application once again connects to the source data dictionary. Once connected, ADS will find records in that data dictionary's queue table, after which it will attempt to connect to the target data dictionary and process the replication queue.

There is a second mechanism. Advantage SQL supports a system stored procedure named sp\_ProcessReplicationQueues. This procedure takes a single integer parameter. If you pass a value of 1, the replication queue on the current connection will be processed immediately. The need for this call is rare, but is useful when a dropped connection is reestablished and you want replication to proceed immediately.

If you pass a value of 2 to sp\_ProcessReplicationQueues, ADS examines all known replication queue tables. If it finds records in any of the queue tables, it restarts the replication on the associated connection until the process queue tables are empty.