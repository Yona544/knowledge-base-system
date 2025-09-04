ROLLBACK WORK




Advantage Database Server 12  

ROLLBACK WORK

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ROLLBACK WORK  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - ROLLBACK WORK Advantage SQL Engine master\_Rollback\_work Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| ROLLBACK WORK  Advantage SQL Engine |  |  |  |  |

Rolls back a transaction on the server.

Syntax

ROLLBACK [WORK] [TO [SAVEPOINT] savepointname]

Remarks

ROLLBACK WORK rolls back all work done inside a transaction or rolls back all work to the savepoint. The transaction state is shared with the client, so a transaction cannot be rolled back in SQL if one has not been started either by an Advantage client (i.e., ACE API AdsBeginTransaction) or through the Advantage SQL engine.

When using [nested transactions](master_nesting_transactions.htm), a rollback statement without a savepoint name rolls back all work to the outermost begin transaction operation, releases all locks, and ends the transaction.

When the TO SAVEPOINT clause is specified, all updates done after establishing of the savepointname will be rolled back, and all savepoints established subsequent to the savepointname will be destroyed. The savepointname will remain valid in the current savepoint level.

Note SQL transactions behave exactly like client transactions. Therefore, with [Advantage Local Server](master_advantage_local_server.htm), transactions are not supported but are expected to be executed in a correct sequence.

Examples

BEGIN TRANSACTION;

UPDATE sal SET salary = 35000.00 WHERE emp\_id = 25089;

ROLLBACK WORK;

 

BEGIN TRAN;

UPDATE sal SET salary = 20000 WHERE hire\_date < '1992-02-14';

ROLLBACK;

 

BEGIN TRANSACTION;

UPDATE sal SET salary = 20000 WHERE hire\_date < '1992-02-14';

SAVEPOINT save1;

DELETE FROM employees WHERE hire\_date < '1900-01-01';

IF User() <> 'Admin' THEN

  ROLLBACK TO SAVEPOINT save1;

END;

COMMIT WORK;