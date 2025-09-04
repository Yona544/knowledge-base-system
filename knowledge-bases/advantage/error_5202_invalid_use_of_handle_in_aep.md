5202 INVALID\_USE\_OF\_HANDLE\_IN\_AEP




Advantage Database Server 12  

5202 INVALID\_USE\_OF\_HANDLE\_IN\_AEP

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5202 INVALID\_USE\_OF\_HANDLE\_IN\_AEP  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5202 INVALID\_USE\_OF\_HANDLE\_IN\_AEP Advantage Error Guide error\_5202\_invalid\_use\_of\_handle\_in\_aep Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5202 INVALID\_USE\_OF\_HANDLE\_IN\_AEP  Advantage Error Guide |  |  |  |  |

Problem: The server detected that an invalid handle is being used by Advantage Extended Procedure. The stored procedure is attempting to use a table, cursor or SQL statement handle that was created on a different connection other than the connection executing the stored procedure. A sample scenario that causes this error is: Proc1() is executed on Connection1 and it opens Table1 as hTable. Proc2() is then executed on Connection2 and it tries to do a GoTop on hTable. The 5202 error will be returned because it is illegal for a procedure executing on Connection2 to use a handle created on Connection1.

Solution: Modify the stored procedure to ensure that it only uses handles created on the same connection. Normally, handles created in stored procedure should be closed before return. However, if the handle must be retained and used by other stored procedures, then those stored procedures must only use the handles that are created on the same connection.