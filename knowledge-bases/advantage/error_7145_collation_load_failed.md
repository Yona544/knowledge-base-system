7145 Collation Load Failed




Advantage Database Server 12  

7145 Collation Load Failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7145 Collation Load Failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7145 Collation Load Failed Advantage Error Guide error\_7145\_collation\_load\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7145 Collation Load Failed  Advantage Error Guide |  |  |  |  |

Problem: Advantage was not able to open and use the collation repository that stores the [dynamic collations](master_collation_support.htm).

Solution: An error occurred when trying to read the collation repository, which is an ADT table named adscollate.adt with an associated memo file named adscollate.adm. Check the error log (ads\_err.adt or ads\_err.dbf) for details.