9057 TPS Transaction failed




Advantage Database Server 12  

9057 TPS Transaction failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 9057 TPS Transaction failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 9057 TPS Transaction failed Advantage Error Guide error\_9057\_tps\_transaction\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 9057 TPS Transaction failed  Advantage Error Guide |  |  |  |  |

A transaction failed. This may happen when a critical error occurs on the server during a transaction rollback or when the server goes down while transactions are in progress. A failed transaction recovery should be attempted immediately. Restart/reload the Advantage Database Server to attempt recovery.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.