5047 AE\_TRANS\_OUT\_OF\_SEQUENCE




Advantage Database Server 12  

5047 AE\_TRANS\_OUT\_OF\_SEQUENCE

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5047 AE\_TRANS\_OUT\_OF\_SEQUENCE  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5047 AE\_TRANS\_OUT\_OF\_SEQUENCE Advantage Error Guide error\_5047\_ae\_trans\_out\_of\_sequence Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5047 AE\_TRANS\_OUT\_OF\_SEQUENCE  Advantage Error Guide |  |  |  |  |

The transaction command was not in a valid sequence. The following are possible causes:

|  |  |
| --- | --- |
| 1. | Attempting to commit or rollback a transaction when there is no active transaction. |

|  |  |
| --- | --- |
| 2. | Attempting to create a savepoint when there is no active transaction. |

|  |  |
| --- | --- |
| 3. | Trying to commit or rollback a transaction across transaction boundary, i.e. trying to commit or rollback a nested transaction in a subprogram without initiating the transaction . See [Nesting Transactions](master_nesting_transactions.htm) for additional information. |