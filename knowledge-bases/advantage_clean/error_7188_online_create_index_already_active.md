---
title: Error 7188 Online Create Index Already Active
slug: error_7188_online_create_index_already_active
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7188_online_create_index_already_active.htm
source: Advantage CHM
tags:
  - error
checksum: 4d15286ef9005ba227c42d2594d7343f41f40ce8
---

# Error 7188 Online Create Index Already Active

Online Create Index Already Active

7188 Online Create Index Already Active

Advantage Error Guide

| 7188 Online Create Index Already Active  Advantage Error Guide |  |  |  |  |

Problem: An online create index operation was already active on a table when another online table maintenance operation was requested on the same table.

Solution1: Allow the previous online create index operation to finish before attempting to perform another online maintenance operation on the same table.

Solution2: Cancel the active online create index operation before attempting to start a different online table maintenance operation on the same table.
