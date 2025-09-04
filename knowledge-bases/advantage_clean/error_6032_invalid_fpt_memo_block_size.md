---
title: Error 6032 Invalid Fpt Memo Block Size
slug: error_6032_invalid_fpt_memo_block_size
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6032_invalid_fpt_memo_block_size.htm
source: Advantage CHM
tags:
  - error
checksum: 7a1260f699423dfda1349768c0f081f2ea5d55d8
---

# Error 6032 Invalid Fpt Memo Block Size

6032 Invalid FPT memo block size

6032 Invalid FPT memo block size

Advantage Error Guide

| 6032 Invalid FPT memo block size  Advantage Error Guide |  |  |  |  |

Problem: An invalid FPT memo block size was specified.

Solution: Correct the program so that a valid FPT memo block size is set. Set the block size to <n>. If <n> is 1-32 inclusive, the block size is 512 \* bytes where <n> is 1 to unlimited bytes. If <n> is greater than 32, the block size is <n> bytes.
