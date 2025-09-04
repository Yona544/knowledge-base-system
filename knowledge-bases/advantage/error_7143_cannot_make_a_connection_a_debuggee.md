7143 Cannot make a connection a debuggee




Advantage Database Server 12  

7143 Cannot make a connection a debuggee

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7143 Cannot make a connection a debuggee  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7143 Cannot make a connection a debuggee Advantage Error Guide error\_7143\_cannot\_make\_a\_connection\_a\_debuggee Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7143 Cannot make a connection a debuggee  Advantage Error Guide |  |  |  |  |

Problem: When using the SQL DEBUG command, a connection cannot be made a debuggee connection because it is processing a client request.

Solution: A connection can only be made a debuggee when it is in an idle state. Wait till the client is idle to retry the command or repeat the command until successful.