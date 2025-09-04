5146 AE\_RI\_RULE\_EXISTS




Advantage Database Server 12  

5146 AE\_RI\_RULE\_EXISTS

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5146 AE\_RI\_RULE\_EXISTS  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5146 AE\_RI\_RULE\_EXISTS Advantage Error Guide error\_5146\_ae\_ri\_rule\_exists Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5146 AE\_RI\_RULE\_EXISTS  Advantage Error Guide |  |  |  |  |

A referential integrity rule exists, making the attempted operation illegal. Remove the referential integrity rule, perform the desired operation, and add the referential integrity rule back to the database.

Note Operations for which this is necessary are prone to integrity problems (AdsZapTable, etc.). When re-creating the referential integrity rule in question, use the "fail table" option and verify the desired rows (if any) are removed.