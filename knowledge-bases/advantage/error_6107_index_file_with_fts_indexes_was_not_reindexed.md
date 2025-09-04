6107 Index file with FTS indexes was not reindexed




Advantage Database Server 12  

6107 Index file with FTS indexes was not reindexed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6107 Index file with FTS indexes was not reindexed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6107 Index file with FTS indexes was not reindexed Advantage Error Guide error\_6107\_index\_file\_with\_fts\_indexes\_was\_not\_reindexed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6107 Index file with FTS indexes was not reindexed  Advantage Error Guide |  |  |  |  |

Problem: This is an informational code that indicates the Advantage Clipper RDD did not rebuild at least one of the index files during a reindex operation because the file contains one or more full text search (FTS) tags. The RDD ignores FTS index files during reindex operations. This informational code can be retrieved after a call to reindex (or dbreindx()) via the AX\_Error() function.

Solution: To rebuild index files that contain FTS tags, use another Advantage client or Advantage Data Architect.