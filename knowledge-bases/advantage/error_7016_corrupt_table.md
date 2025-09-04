7016 Corrupt table




Advantage Database Server 12  

7016 Corrupt table

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7016 Corrupt table  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7016 Corrupt table Advantage Error Guide error\_7016\_corrupt\_table Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7016 Corrupt table  Advantage Error Guide |  |  |  |  |

Problem: The specified table contains corrupted data in the file or field headers.

Solution 1: Make sure the specified file is a valid table. Also, make sure you are not attempting to open a DBF table with an ADT table type, or vice versa.

Solution 2: If the table is an ADT (Advantage Proprietary Table), run the ADT table repair utility (ADTFIX.EXE) against the offending ADT table. This utility is available for download from the Advantage Developer Zone Web site in the "Tools & Utilities" section, <http://DevZone.AdvantageDatabase.com>. Once the table is fixed, all indexes on the table must then be rebuilt.