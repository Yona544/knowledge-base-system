---
title: Error 7155 Err Lost Cached Updates
slug: error_7155_err_lost_cached_updates
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7155_err_lost_cached_updates.htm
source: Advantage CHM
tags:
  - error
checksum: 1fab45278b0c1ebd0c19510a9a9681bb59bcdb2a
---

# Error 7155 Err Lost Cached Updates

7155 Lost Cached Updates

7155 Lost Cached Updates

Advantage Error Guide

| 7155 Lost Cached Updates  Advantage Error Guide |  |  |  |  |

Problem: A table had updates in the cache when Advantage was improperly shutdown.

Solution1: The table should be restored with a recent backup to correct any corruption due to the lost updates.

Solution2: If the table isnt corrupt and is still usable, making an update to the table will clear the lost cached updates flag and keep the error from being logged again.

See [Table Data Caching](master_table_data_caching.md) for details.
