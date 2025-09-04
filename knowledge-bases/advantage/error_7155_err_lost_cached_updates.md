7155 Lost Cached Updates




Advantage Database Server 12  

7155 Lost Cached Updates

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7155 Lost Cached Updates  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7155 Lost Cached Updates Advantage Error Guide error\_7155\_ERR\_LOST\_CACHED\_UPDATES Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7155 Lost Cached Updates  Advantage Error Guide |  |  |  |  |

Problem: A table had updates in the cache when Advantage was improperly shutdown.

Solution1: The table should be restored with a recent backup to correct any corruption due to the lost updates.

Solution2: If the table isnt corrupt and is still usable, making an update to the table will clear the lost cached updates flag and keep the error from being logged again.

See [Table Data Caching](master_table_data_caching.htm) for details.