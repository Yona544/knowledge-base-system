8040 Error creating shared memory object




Advantage Database Server 12  

8040 Error creating shared memory object

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 8040 Error creating shared memory object  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 8040 Error creating shared memory object Advantage Error Guide error\_8040\_error\_creating\_shared\_memory\_object Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 8040 Error creating shared memory object  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server failed to create a shared memory object to use for inter-process communications (IPC) with clients running on the same physical workstation. This error is logged for informational purposes and is not returned to the client. The entry preceding this error in the error log will show the specific system error code.

Solution: This error can occur if a client application has stopped responding and has been disconnected by Advantage Database Server. The client application will hold the IPC objects for a specific connection entry and prevent future use of them. Close the unresponsive client application to free up the IPC objects.