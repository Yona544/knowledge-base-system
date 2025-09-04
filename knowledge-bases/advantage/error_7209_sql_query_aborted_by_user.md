7209 SQL query aborted by user




Advantage Database Server 12  

7209 SQL query aborted by user

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7209 SQL query aborted by user  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7209 SQL query aborted by user Advantage Error Guide error\_7209\_sql\_query\_aborted\_by\_user Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7209 SQL query aborted by user  Advantage Error Guide |  |  |  |  |

Problem: The SQL query was aborted by the user.

Solution: If using ADO and executing a query that can take quite a while to complete, set the Command.CommandTimeout property to a value greater than its default of 30 seconds. If using ADO.Net and executing a query that can take quite a while to complete, set the OleDbCommand.CommandTimeout property to a value greater than its default of 30 seconds.