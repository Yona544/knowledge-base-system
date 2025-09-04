7146 Collation Name Not Unique




Advantage Database Server 12  

7146 Collation Name Not Unique

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7146 Collation Name Not Unique  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7146 Collation Name Not Unique Advantage Error Guide error\_7146\_collation\_name\_not\_unique Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7146 Collation Name Not Unique  Advantage Error Guide |  |  |  |  |

Problem: When loading a [dynamic collation](master_collation_support.htm), multiple entries in the repository were found that match the name.

Solution: The error log (ads\_err.adt or ads\_err.dbf) entry for this error will show the name that was found to be non-unique. It may be necessary to replace the adscollate.adt and adscollate.adm files with valid copies.