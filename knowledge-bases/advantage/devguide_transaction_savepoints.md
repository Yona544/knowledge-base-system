Transaction Savepoints




Advantage Database Server 12  

     Transaction Savepoints

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Transaction Savepoints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Transaction Savepoints Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Transaction\_Savepoints Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > Transaction Savepoints / Dear Support Staff, |  |
| Transaction Savepoints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Transactions in Advantage now support savepoints. A savepoint identifies a state during a transaction to which you may want to roll back to, without having to roll back the entire transaction.

You can have multiple savepoints for a single transaction. You specify which savepoint you want to roll back to when you want to perform a partial rollback. When you roll back to a given savepoint, those operations within the transaction that were executed prior to the savepoint remain intact.

Transaction savepoints are discussed in detail in Chapter 12.