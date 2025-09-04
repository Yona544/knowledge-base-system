7122 Local server failed to rebuild index




Advantage Database Server 12  

7122 Local server failed to rebuild index

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7122 Local server failed to rebuild index  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7122 Local server failed to rebuild index Advantage Error Guide error\_7122\_local\_server\_failed\_to\_rebuild\_index Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7122 Local server failed to rebuild index  Advantage Error Guide |  |  |  |  |

Problem: Advantage Local server attempted to rebuild a corrupt index but the parent table was not opened exclusively. If the Advantage Database Server shutdown abnormally, it is possible that some updates to index files were not saved to disk. The next time such an index is opened, Advantage will attempt to rebuild the index automatically. To do this the table (and index) must be opened exclusively or by Advantage Remote Server.

Solution: Open the parent table and the index exclusively or using remote server. In the future, avoid shutting down the Advantage Database Server when index files are still open or disable the caching of index updates by setting the MAX\_CACHE\_MEMORY configuration value to zero.