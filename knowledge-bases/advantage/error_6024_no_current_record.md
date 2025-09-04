6024 No current record




Advantage Database Server 12  

6024 No current record

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6024 No current record  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6024 No current record Advantage Error Guide error\_6024\_no\_current\_record Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6024 No current record  Advantage Error Guide |  |  |  |  |

Problem: AX\_KeyAdd() or AX\_KeyDrop() was called and the record pointer was not positioned on a record. For example, you would not be positioned on a record if you were at EOF due to a failed seek operation.

Solution: Perform a GO TOP, GO BOTTOM, SEEK or some other operation to position yourself in the file to a valid record.