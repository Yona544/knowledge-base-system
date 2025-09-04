---
title: Error 2167 Select Sub Query Returned More Than One Row
slug: error_2167_select_sub_query_returned_more_than_one_row
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2167_select_sub_query_returned_more_than_one_row.htm
source: Advantage CHM
tags:
  - error
checksum: b3f5d82862c5650e102579de5de97929e694646a
---

# Error 2167 Select Sub Query Returned More Than One Row

2167 SELECT sub-query returned more than one row

2167 SELECT sub-query returned more than one row

Advantage Error Guide

| 2167 SELECT sub-query returned more than one row  Advantage Error Guide |  |  |  |  |

Problem: A sub-query returned more than one row in a context where a single row was expected. For example, "SELECT \* FROM table1 WHERE table1.field1 = (SELECT table2.field1 FROM table2)" is not valid if table2 contains more than one row.

Solution: Adjust the WHERE clause on the sub-query so that it returns only a single row.
