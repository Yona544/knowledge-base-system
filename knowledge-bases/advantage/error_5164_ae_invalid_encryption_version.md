5164 AE\_INVALID\_ENCRYPTION\_VERSION




Advantage Database Server 12  

5164 AE\_INVALID\_ENCRYPTION\_VERSION

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5164 AE\_INVALID\_ENCRYPTION\_VERSION  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5164 AE\_INVALID\_ENCRYPTION\_VERSION Advantage Error Guide error\_5164\_ae\_invalid\_encryption\_version Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5164 AE\_INVALID\_ENCRYPTION\_VERSION  Advantage Error Guide |  |  |  |  |

Problem: The database table encryption version that is stored in the table header is incorrect.

Solution: The likely cause of this corruption problem is that the database table file has been overwritten by the user. The database should be maintained using the data dictionary management API or the Advantage Data Architect (arc32.exe). Using OS commands or the API to update the file will likely cause corruption.