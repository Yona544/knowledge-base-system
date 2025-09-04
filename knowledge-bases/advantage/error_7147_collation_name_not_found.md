7147 Collation Name Not Found




Advantage Database Server 12  

7147 Collation Name Not Found

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7147 Collation Name Not Found  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7147 Collation Name Not Found Advantage Error Guide error\_7147\_collation\_name\_not\_found Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7147 Collation Name Not Found  Advantage Error Guide |  |  |  |  |

Problem: An attempt to load a [dynamic collation](master_collation_support.htm) failed because the given collation name was not found.

Solution: Verify that the correct collation name was specified in the application. The error log (ads\_err.adt or ads\_err.dbf) entry for this error will show the name that was being searched for.