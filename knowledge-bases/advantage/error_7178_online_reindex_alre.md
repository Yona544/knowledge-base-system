7178 Online Reindex Already Active




Advantage Database Server 12  

7178 Online Reindex Already Active

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7178 Online Reindex Already Active  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7178 Online Reindex Already Active Advantage Error Guide Error\_7178\_Online\_Reindex\_Alre Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7178 Online Reindex Already Active  Advantage Error Guide |  |  |  |  |

Problem: An online reindex operation was already active on a table when another online reindex operation was requested on the same table.

Solution1: Allow the previous online reindex operation to finish before attempting to reindex the same table again.

Solution2: Cancel the active online reindex operation before attempting to reindex the same table again.  Consider specifying a timeout value in the sp\_ReindexOnline call if the operation is taking too long.