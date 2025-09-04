7215 ROWID Invalidated During Pack




Advantage Database Server 12  

7215 ROWID Invalidated During Pack

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7215 ROWID Invalidated During Pack  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7215 ROWID Invalidated During Pack Advantage Error Guide Error\_7215\_ROWID\_Invalidated\_D Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7215 ROWID Invalidated During Pack  Advantage Error Guide |  |  |  |  |

Problem: A query used a ROWID value for a table that has been packed online.

Solution: ROWID values for packed tables may be invalid and shouldn't be used.  ROWID values should be recalculated after a table has been packed online.