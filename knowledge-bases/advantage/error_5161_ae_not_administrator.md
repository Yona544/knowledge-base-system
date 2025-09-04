5161 AE\_NOT\_ADMINISTRATOR




Advantage Database Server 12  

5161 AE\_NOT\_ADMINISTRATOR

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5161 AE\_NOT\_ADMINISTRATOR  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5161 AE\_NOT\_ADMINISTRATOR Advantage Error Guide error\_5161\_ae\_not\_administrator Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5161 AE\_NOT\_ADMINISTRATOR  Advantage Error Guide |  |  |  |  |

Problem: The requested operation requires administrative access to the data dictionary. All operations that modify the data dictionary and some operations that retrieve information from the data dictionary require the user to connect to the database as the administrator. This error is returned when a regular user tries to perform one of those operations.

Solution: Obtain a connection to database as the administrator using "ADSSYS" as the user name.