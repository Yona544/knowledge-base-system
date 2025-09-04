7175 Online Pack Already Active




Advantage Database Server 12  

7175 Online Pack Already Active

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7175 Online Pack Already Active  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7175 Online Pack Already Active Advantage Error Guide Error\_7175\_Online\_Pack\_Already Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7175 Online Pack Already Active  Advantage Error Guide |  |  |  |  |

Problem: An online pack operation was already active on a table when another online pack operation was requested on the same table.

Solution1: Allow the previous online pack operation to finish before attempting to pack the same table again.

Solution2: Cancel the active online pack operation before attempting to pack the same table again.  Consider specifying a timeout value in the sp\_PackTableOnline call if the operation is taking too long.