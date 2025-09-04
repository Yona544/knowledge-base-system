7154 Index Automatically Rebuilt




Advantage Database Server 12  

7154 Index Automatically Rebuilt

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7154 Index Automatically Rebuilt  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7154 Index Automatically Rebuilt Advantage Error Guide error\_7154\_index\_automatically\_rebuilt Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7154 Index Automatically Rebuilt  Advantage Error Guide |  |  |  |  |

A 7154 error indicates an index file was not closed properly the last time it was opened. The server detected this state and automatically re-indexed the file.

This can happen if you use a file system command to copy an index file while Advantage has the file open. Advantage may have portions of the file cached, and if this cache has not been flushed to disk you can not make copies of the file until Advantage closes it. Any copies you make will need to be re-indexed before they are opened again by Advantage. If this situation arises, Advantage will detect it and automatically re-index and log the 7154 error.