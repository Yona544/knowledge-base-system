---
title: Error 7091 Collation Sequence Used To Create The Index Differs From Current Collation Sequence
slug: error_7091_collation_sequence_used_to_create_the_index_differs_from_current_collation_sequence
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7091_collation_sequence_used_to_create_the_index_differs_from_current_collation_sequence.htm
source: Advantage CHM
tags:
  - error
checksum: 6aa26c533264bf1484c12efed19aaba556540f82
---

# Error 7091 Collation Sequence Used To Create The Index Differs From Current Collation Sequence

7091 Collation sequence used to create the index differs from current collation sequence

7091 Collation sequence used to create the index differs from current collation sequence

Advantage Error Guide

| 7091 Collation sequence used to create the index differs from current collation sequence  Advantage Error Guide |  |  |  |  |

Problem: Advantage detected a mismatch between the collation sequence used to create the index file and the current collation sequence.

Solution: See error code [5175](error_5175_ae_index_collation_mismatch.md) for more information about this error. The 7091 error is only written to the error log. If you are using a client that is version 6.2 or greater, the client will also detect the mismatch and return a 5175 error.
