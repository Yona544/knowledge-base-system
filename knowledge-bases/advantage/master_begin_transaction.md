BEGIN TRANSACTION




Advantage Database Server 12  

BEGIN TRANSACTION

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| BEGIN TRANSACTION  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - BEGIN TRANSACTION Advantage SQL Engine master\_Begin\_transaction Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| BEGIN TRANSACTION  Advantage SQL Engine |  |  |  |  |

Begins a transaction on the server.

Syntax

BEGIN TRAN[SACTION]

Remarks

BEGIN TRANSACTION begins a transaction for the calling user. Transactions can be [nested](master_nesting_transactions.htm) by executing BEGIN TRANSACTION inside of an existing transaction.

Note SQL transactions behave exactly like client transactions. Therefore, with Advantage Local Server, transactions are not supported, but are expected to be executed in a correct sequence.

Examples

BEGIN TRANSACTION

UPDATE sal SET salary = 35000.00 WHERE emp\_id = 25089

COMMIT WORK

 

BEGIN TRAN

UPDATE sal SET salary = 20000 WHERE hire\_date < '1992-02-14'

ROLLBACK WORK