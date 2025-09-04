6027 Invalid master index




Advantage Database Server 12  

6027 Invalid master index

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6027 Invalid master index  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6027 Invalid master index Advantage Error Guide error\_6027\_invalid\_master\_index Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6027 Invalid master index  Advantage Error Guide |  |  |  |  |

Problem: A tag that already existed in a CDX was being reindexed using a master index, but the master index was the tag being reindexed.

Solution: If reindexing an existing tag such that a master index is involved (e.g., the tag is a subindex), make sure the active index order is not set to the index that is to be reindexed.