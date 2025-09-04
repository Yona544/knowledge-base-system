---
title: Error 6031 No Memo File
slug: error_6031_no_memo_file
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6031_no_memo_file.htm
source: Advantage CHM
tags:
  - error
checksum: 48b49630e10868874f49c5e2da60f2ccb7ffc8f5
---

# Error 6031 No Memo File

6031 No memo file

6031 No memo file

Advantage Error Guide

| 6031 No memo file  Advantage Error Guide |  |  |  |  |

Problem: A memo file (DBT or FPT file) does not exist and an operation that requires a memo file was issued. Currently, functions that require a memo file to exist are AX\_BLOB2File() and AX\_File2BLOB().

Solution: Make sure the table being used also has a memo file before attempting an operation that requires a memo file.
