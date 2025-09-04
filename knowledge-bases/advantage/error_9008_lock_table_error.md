9008 Lock table error




Advantage Database Server 12  

9008 Lock table error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 9008 Lock table error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 9008 Lock table error Advantage Error Guide error\_9008\_lock\_table\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 9008 Lock table error  Advantage Error Guide |  |  |  |  |

Server received an unlock request from a client that didn't have any locks (record or file). The client code should not issue an unlock to the Advantage server if there are no locks.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.