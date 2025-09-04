9027 Receive request out of sequence




Advantage Database Server 12  

9027 Receive request out of sequence

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 9027 Receive request out of sequence  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 9027 Receive request out of sequence Advantage Error Guide error\_9027\_receive\_request\_out\_of\_sequence Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 9027 Receive request out of sequence  Advantage Error Guide |  |  |  |  |

The server received a resend request or acknowledge that didn't have the current sequence number. It is not logged in the error log but is visible by the Advantage Management Utility.

In general, 9000 class errors indicate an internal problem within the Advantage server.

On the Windows platform, when Advantage logs a 9000 class error it will also generate a crash dump file. This file will be placed in the error log path (default is c:\), and the filename will be prefixed with "adsdump". Please send this crash dump file, along with all ads\_err error log files to Advantage Technical Support.

For other platforms, please send a small re-creation, along with all ads\_err error log files to Advantage Technical Support.