5200 AE\_BLURRY\_SNAPSHOT




Advantage Database Server 12  

5200 AE\_BLURRY\_SNAPSHOT

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5200 AE\_BLURRY\_SNAPSHOT  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5200 AE\_BLURRY\_SNAPSHOT Advantage Error Guide error\_5200\_ae\_blurry\_snapshot Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5200 AE\_BLURRY\_SNAPSHOT  Advantage Error Guide |  |  |  |  |

Problem: The server was unable to stage a backup and get a logic snapshot. The backup continued, but with the chance that other worker threads could have changed data and made this a logically inconsistent backup.

Solution: To resolve this issue, run the backup again.

 

If the error persists, contact Advantage Technical Services. Configuration values exist that can be used to extend the period of time the server will wait before continuing.