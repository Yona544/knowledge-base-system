---
title: Error 6107 Index File With Fts Indexes Was Not Reindexed
slug: error_6107_index_file_with_fts_indexes_was_not_reindexed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6107_index_file_with_fts_indexes_was_not_reindexed.htm
source: Advantage CHM
tags:
  - error
checksum: f5461e4b6f6f0dbbb7021a6119fdf77a6cd5b18f
---

# Error 6107 Index File With Fts Indexes Was Not Reindexed

6107 Index file with FTS indexes was not reindexed

6107 Index file with FTS indexes was not reindexed

Advantage Error Guide

| 6107 Index file with FTS indexes was not reindexed  Advantage Error Guide |  |  |  |  |

Problem: This is an informational code that indicates the Advantage Clipper RDD did not rebuild at least one of the index files during a reindex operation because the file contains one or more full text search (FTS) tags. The RDD ignores FTS index files during reindex operations. This informational code can be retrieved after a call to reindex (or dbreindx()) via the AX\_Error() function.

Solution: To rebuild index files that contain FTS tags, use another Advantage client or Advantage Data Architect.
