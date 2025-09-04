---
title: Error 7073 The Maximum Number Of Memo Blocks Has Been Reached
slug: error_7073_the_maximum_number_of_memo_blocks_has_been_reached
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7073_the_maximum_number_of_memo_blocks_has_been_reached.htm
source: Advantage CHM
tags:
  - error
checksum: b9055caa720d196545c1f9b73c3e28e112b6f64a
---

# Error 7073 The Maximum Number Of Memo Blocks Has Been Reached

7073 The maximum number of memo blocks has been reached

7073 The maximum number of memo blocks has been reached

Advantage Error Guide

| 7073 The maximum number of memo blocks has been reached  Advantage Error Guide |  |  |  |  |

Problem: The number of blocks in the memo file has reached the 4,294,967,296 block (4 GB) limit.

Solution 1: Create a new table with the same structure as the table in question, but with a larger memo block size. Copy all data from the old table into the new table. See documentation in your client help file for more information on choosing a memo block size.

Solution 2: It is possible that memo blocks can be orphaned in memo files. Packing the table will free these orphaned blocks and allow them to be used again.
