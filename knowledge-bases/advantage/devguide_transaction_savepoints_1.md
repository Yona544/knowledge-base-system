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
| Transaction Savepoints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Transaction Savepoints Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Transaction\_Savepoints\_1 Advantage Developer's Guide > Part II - Advantage SQL > Chapter 12 - SQL to Perform Common Tasks > Transaction Savepoints / Dear Support Staff, |  |
| Transaction Savepoints  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Beginning with Advantage 8, ADS supports transaction savepoints. A savepoint identifies a state during a transaction to which you may want to roll back to, without having to roll back the entire transaction.

You can have multiple savepoints for a single transaction. You specify which savepoint you want to roll back to when you want to perform a partial rollback. When you roll back to a given savepoint, those operations within the transaction that were executed prior to the savepoint remain intact and the transaction is still active.

You create a savepoint within a transaction by calling the SAVEPOINT keyword followed by a savepoint name. A savepoint name is similar to a variable name.

You roll back to a savepoint using the ROLLBACK keyword. However, instead of calling ROLLBACK WORK, you follow the ROLLBACK keyword with the TO SAVEPOINT keywords followed by the name you assigned when you created the savepoint.

As must be obvious, when you create multiple savepoints within a single transaction, each must have a different name.

The following example, demonstrates the partial rollback to a savepoint:

BEGIN TRANSACTION;  
TRY  
  UPDATE Products Set "Product Name" = 'Accounting Suite II'  
    WHERE "Product Code" = 'H10302';  
  SAVEPOINT Midpoint;  
  DELETE FROM Products WHERE "Product Code" = 'H10302';  
  ROLLBACK TO SAVEPOINT Midpoint;  
  COMMIT WORK;  
CATCH ALL  
    ROLLBACK WORK;  
END TRY;