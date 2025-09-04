Online Create Index Already Active




Advantage Database Server 12  

7188 Online Create Index Already Active

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7188 Online Create Index Already Active  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7188 Online Create Index Already Active Advantage Error Guide Error\_7188\_Online\_Create\_Index\_Already\_Active Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7188 Online Create Index Already Active  Advantage Error Guide |  |  |  |  |

Problem: An online create index operation was already active on a table when another online table maintenance operation was requested on the same table.

Solution1: Allow the previous online create index operation to finish before attempting to perform another online maintenance operation on the same table.

Solution2: Cancel the active online create index operation before attempting to start a different online table maintenance operation on the same table.