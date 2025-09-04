COMMIT WORK




Advantage Database Server 12  

COMMIT WORK

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| COMMIT WORK  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - COMMIT WORK Advantage SQL Engine master\_Commit\_work Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| COMMIT WORK  Advantage SQL Engine |  |  |  |  |

Commits a transaction on the server.

Syntax

COMMIT [WORK]

Remarks

COMMIT WORK commits any work done inside a transaction. The transaction state is shared with the client, so a transaction cannot be committed in SQL if one has not been started either by an Advantage client (i.e., ACE API AdsBeginTransaction) or through the Advantage SQL engine.

When used in [nested transactions](master_nesting_transactions.htm), a commit of an inner transaction does not commit the data or release locks. Only committing the outer most transaction will commit the work and end the transaction.

Note SQL transactions behave exactly like client transactions. Therefore, with Advantage Local Server, transactions are not supported, but are expected to be executed in a correct sequence.

Examples

BEGIN TRANSACTION

UPDATE sal SET salary = 35000.00 WHERE emp\_id = 25089

COMMIT WORK

 

BEGIN TRAN

UPDATE sal SET salary = 20000 WHERE hire\_date < '1992-02-14'

COMMIT