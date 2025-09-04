6064 Getting the computer name failed




Advantage Database Server 12  

6064 Getting the computer name failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6064 Getting the computer name failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6064 Getting the computer name failed Advantage Error Guide error\_6064\_getting\_the\_computer\_name\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6064 Getting the computer name failed  Advantage Error Guide |  |  |  |  |

Problem: When using 16-bit Windows applications with local drive letters, the name of the local machine is needed. An error occurred while getting the name of the current machine.

Solution: Make sure that the IP and/or IPX protocol is installed. Verify that NETAPI.DLL is in your search path. If possible, specify a UNC path instead of a drive letter.