7142 The maximum number of debuggees was exceeded




Advantage Database Server 12  

7142 The maximum number of debuggees was exceeded

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7142 The maximum number of debuggees was exceeded  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7142 The maximum number of debuggees was exceeded Advantage Error Guide error\_7142\_the\_maximum\_number\_of\_debuggees\_was\_exceeded Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7142 The maximum number of debuggees was exceeded  Advantage Error Guide |  |  |  |  |

Problem: When using the SQL DEBUG command, a connection cannot be made a debuggee because the server has reached the limit of number of concurrent debuggee connections.

Solution: When debugging an SQL script on the Advantage Database server, the maximum number of concurrent debuggees is the number of configured worker threads minus one. Increase the number of configured worker threads and restart the server to debug additional connections.