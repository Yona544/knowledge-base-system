---
title: Error 7122 Local Server Failed To Rebuild Index
slug: error_7122_local_server_failed_to_rebuild_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7122_local_server_failed_to_rebuild_index.htm
source: Advantage CHM
tags:
  - error
checksum: a80400073f50615e9020d5577fc6f3983768d406
---

# Error 7122 Local Server Failed To Rebuild Index

7122 Local server failed to rebuild index

7122 Local server failed to rebuild index

Advantage Error Guide

| 7122 Local server failed to rebuild index  Advantage Error Guide |  |  |  |  |

Problem: Advantage Local server attempted to rebuild a corrupt index but the parent table was not opened exclusively. If the Advantage Database Server shutdown abnormally, it is possible that some updates to index files were not saved to disk. The next time such an index is opened, Advantage will attempt to rebuild the index automatically. To do this the table (and index) must be opened exclusively or by Advantage Remote Server.

Solution: Open the parent table and the index exclusively or using remote server. In the future, avoid shutting down the Advantage Database Server when index files are still open or disable the caching of index updates by setting the MAX\_CACHE\_MEMORY configuration value to zero.
