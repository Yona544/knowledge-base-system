6012 Invalid key length




Advantage Database Server 12  

6012 Invalid key length

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6012 Invalid key length  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6012 Invalid key length Advantage Error Guide error\_6012\_invalid\_key\_length Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6012 Invalid key length  Advantage Error Guide |  |  |  |  |

Problem: The key length of the stored index and the actual length when evaluating the key expression were different.

Solution: Make sure the key expression will produce a value of the same length for all records. Do not use functions such as TRIM() in the key expression. To restrict the length of the key values, use the LEFT() or PADR() functions. If a User-Defined Function (UDF) is used in the key expression, verify that the same function is available in all applications that use the index and that the function returns a value of the same length for all records.