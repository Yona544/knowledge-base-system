---
title: Error 2157 Too Many Key Columns For Index
slug: error_2157_too_many_key_columns_for_index
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2157_too_many_key_columns_for_index.htm
source: Advantage CHM
tags:
  - error
checksum: c3f8920e3977d5072acd1271a0660bc1f82617bd
---

# Error 2157 Too Many Key Columns For Index

2157 Too many key columns for index

2157 Too many key columns for index

Advantage Error Guide

| 2157 Too many key columns for index  Advantage Error Guide |  |  |  |  |

Problem: A CREATE INDEX statement contained too many columns.

Solution: The maximum number of columns allowed in an SQL CREATE INDEX statement is 15. Content indexes (for full text searches) can only have one column.
