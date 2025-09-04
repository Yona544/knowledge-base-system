6101 Transaction command out of sequence




Advantage Database Server 12  

6101 Transaction command out of sequence

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6101 Transaction command out of sequence  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6101 Transaction command out of sequence Advantage Error Guide error\_6101\_transaction\_command\_out\_of\_sequence Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6101 Transaction command out of sequence  Advantage Error Guide |  |  |  |  |

Problem: The application contained a nested transaction.

Solution: Make sure a BEGIN TRANSACTION command is followed either by a COMMIT TRANSACTION or a ROLLBACK TRANSACTION before another BEGIN TRANSACTION is issued. Also, a COMMIT TRANSACTION or a ROLLBACK TRANSACTION cannot be issued without first issuing a successful BEGIN TRANSACTION.