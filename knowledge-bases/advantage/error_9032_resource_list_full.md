9032 Resource list full




Advantage Database Server 12  

9032 Resource list full

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 9032 Resource list full  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 9032 Resource list full Advantage Error Guide error\_9032\_resource\_list\_full Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 9032 Resource list full  Advantage Error Guide |  |  |  |  |

Pre-allocated resources are all in use. The internal list (which is an array of structures) that keeps track of memory allocations, internal file creations, semaphore/mutex creations, etc., is full. There are two likely causes for this error:

|  |  |
| --- | --- |
| 1. | Large transactions are being performed and/or many users are doing one-at-a-time transactions with the "Transaction List Elements" setting too low. |

|  |  |
| --- | --- |
| 2. | The "Transaction List Elements" setting is set greater than 50,000 while using the Advantage Database Server v4.4 and older. |

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.