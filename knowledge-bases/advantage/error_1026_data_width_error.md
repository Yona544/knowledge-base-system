1026 Data Width Error




Advantage Database Server 12  

1026 Data Width Error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 1026 Data Width Error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 1026 Data Width Error Advantage Error Guide error\_1026\_data\_width\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 1026 Data Width Error  Advantage Error Guide |  |  |  |  |

Problem: When building an index, the initial evaluation of the key expression (on a blank record) produced a character value of zero length.

Solution: Make sure the key expression will produce a value of the same length for all records. Do not use functions such as TRIM() in the key expression. To restrict the length of the key values, use the LEFT() or PADR() functions.