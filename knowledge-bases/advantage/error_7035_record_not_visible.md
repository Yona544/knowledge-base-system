7035 Record not visible




Advantage Database Server 12  

7035 Record not visible

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7035 Record not visible  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7035 Record not visible Advantage Error Guide error\_7035\_record\_not\_visible Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7035 Record not visible  Advantage Error Guide |  |  |  |  |

Problem: The application is trying to GOTO a record number that is being appended by another application during a transaction.

Solution: The user will be positioned to EOF. This behavior exists because records appended during another clients transactions are "invisible" to all other users until that transaction is committed.