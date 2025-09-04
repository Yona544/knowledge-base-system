5204 AE\_INVALID\_COLLATION




Advantage Database Server 12  

5204 AE\_INVALID\_COLLATION

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5204 AE\_INVALID\_COLLATION  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5204 AE\_INVALID\_COLLATION Advantage Error Guide error\_5204\_ae\_invalid\_collation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5204 AE\_INVALID\_COLLATION  Advantage Error Guide |  |  |  |  |

Problem: The application attempted to load a [dynamic collation](master_collation_support.htm) that has invalid information associated with it.

Solution: This problem may be that the adscollate.adt table has been corrupted. Replace adscollate.adt and adscollate.adm with valid copies of the files.