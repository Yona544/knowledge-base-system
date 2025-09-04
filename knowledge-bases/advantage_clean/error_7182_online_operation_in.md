---
title: Error 7182 Online Operation In
slug: error_7182_online_operation_in
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7182_online_operation_in.htm
source: Advantage CHM
tags:
  - error
checksum: ebb2192232cc0ce2e214ba3039002f4ac2ca282d
---

# Error 7182 Online Operation In

7182 Online Operation Index Collation Mismatch

7182 Online Operation Index Collation Mismatch

Advantage Error Guide

| 7182 Online Operation Index Collation Mismatch  Advantage Error Guide |  |  |  |  |

Problem: The index collation specified on the connection is different than the collation that was used when an index was opened.

Solution: Set the correct collation on the connection before attempting an online operation (pack, reindex, alter).  Conversely, make sure any other users of the table or index is using the same collation that the online operation uses.
