6091 Index(es) open on destination table




Advantage Database Server 12  

6091 Index(es) open on destination table

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6091 Index(es) open on destination table  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6091 Index(es) open on destination table Advantage Error Guide error\_6091\_index\_es\_open\_on\_destination\_table Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6091 Index(es) open on destination table  Advantage Error Guide |  |  |  |  |

Problem: A Copy To or Append From operation was attempted on the server, but index(es) are open on the destination table, so the operation was performed on the client.

Solution: Close all open indexes on the destination table before attempting the Copy To or Append From operation on the server. Then re-open the indexes when the operation is completed and re-build the indexes.