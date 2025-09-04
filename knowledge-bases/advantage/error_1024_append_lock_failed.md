1024 Append Lock Failed




Advantage Database Server 12  

1024 Append Lock Failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1024 Append Lock Failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 1024 Append Lock Failed Advantage Error Guide error\_1024\_append\_lock\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 1024 Append Lock Failed  Advantage Error Guide |  |  |  |  |

Problem: A new record could not be appended because a lock could not be obtained for the new record.

Solution: For a shared work area, the append blank operation automatically obtains a record lock for the newly appended record. If the record cannot be locked, the append fails. This generally occurs because another process has obtained a file lock on the table. Change the program to handle the lock contention.