7182 Online Operation Index Collation Mismatch




Advantage Database Server 12  

7182 Online Operation Index Collation Mismatch

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7182 Online Operation Index Collation Mismatch  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7182 Online Operation Index Collation Mismatch Advantage Error Guide Error\_7182\_Online\_Operation\_In Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7182 Online Operation Index Collation Mismatch  Advantage Error Guide |  |  |  |  |

Problem: The index collation specified on the connection is different than the collation that was used when an index was opened.

Solution: Set the correct collation on the connection before attempting an online operation (pack, reindex, alter).  Conversely, make sure any other users of the table or index is using the same collation that the online operation uses.