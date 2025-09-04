---
title: Error 2206 Update Statement Is Ambiguous
slug: error_2206_update_statement_is_ambiguous
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2206_update_statement_is_ambiguous.htm
source: Advantage CHM
tags:
  - error
checksum: 2c463fafbb18a20181f1c2835e3b9acc0b9f1aa3
---

# Error 2206 Update Statement Is Ambiguous

2206 Update statement is ambiguous

2206 Update statement is ambiguous

Advantage Error Guide

| 2206 Update statement is ambiguous  Advantage Error Guide |  |  |  |  |

The table to be updated is listed more than once in the FROM clause of an UPDATE statement. A sample ambiguous update statement is:

UPDATE table1 SET col1 = 2 FROM table1 a INNER JOIN table1 b WHERE a.id = b.id2

It is not possible for the SQL engine to determine whether the instance "a" of table1 or the instance "b" of table1 should be updated.
