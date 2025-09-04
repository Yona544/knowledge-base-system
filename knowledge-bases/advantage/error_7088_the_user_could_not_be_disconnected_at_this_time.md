7088 The user could not be disconnected at this time




Advantage Database Server 12  

7088 The user could not be disconnected at this time

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7088 The user could not be disconnected at this time  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7088 The user could not be disconnected at this time Advantage Error Guide error\_7088\_the\_user\_could\_not\_be\_disconnected\_at\_this\_time Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7088 The user could not be disconnected at this time  Advantage Error Guide |  |  |  |  |

Problem: When attempting to disconnect a user from the server by performing a "kill user" management operation, a 7088 error occurs.

Solution: The "kill user" management operation failed because the server is processing a request from the user that cannot be stopped at this time. Retry the "kill user" operation at some later time when the user's current operation has completed.