---
title: Error 7178 Online Reindex Alre
slug: error_7178_online_reindex_alre
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7178_online_reindex_alre.htm
source: Advantage CHM
tags:
  - error
checksum: 12e1cee2fccb575ebe94ff2c7ca2b5416183ce3a
---

# Error 7178 Online Reindex Alre

7178 Online Reindex Already Active

7178 Online Reindex Already Active

Advantage Error Guide

| 7178 Online Reindex Already Active  Advantage Error Guide |  |  |  |  |

Problem: An online reindex operation was already active on a table when another online reindex operation was requested on the same table.

Solution1: Allow the previous online reindex operation to finish before attempting to reindex the same table again.

Solution2: Cancel the active online reindex operation before attempting to reindex the same table again.  Consider specifying a timeout value in the sp\_ReindexOnline call if the operation is taking too long.
