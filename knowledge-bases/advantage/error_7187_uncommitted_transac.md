Uncommitted Transaction




Advantage Database Server 12  

7187 Uncommitted Transaction

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7187 Uncommitted Transaction  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7187 Uncommitted Transaction Advantage Error Guide Error\_7187\_uncommitted\_transac Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7187 Uncommitted Transaction  Advantage Error Guide |  |  |  |  |

Problem: A subprogam, i.e. stored procedure, user defined function or trigger, started a transaction without committing it.

Solution: This is a warning that a nested transaction should be committed in the same subprogram that initiated it. Advantage will automatically commit unbalanced transaction that started in a subprogram. It is a good programming practice to explicitly commit nested transactions. See [Nesting Transactions](master_nesting_transactions.htm) for additional information.