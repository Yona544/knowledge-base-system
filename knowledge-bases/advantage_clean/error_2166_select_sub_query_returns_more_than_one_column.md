---
title: Error 2166 Select Sub Query Returns More Than One Column
slug: error_2166_select_sub_query_returns_more_than_one_column
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2166_select_sub_query_returns_more_than_one_column.htm
source: Advantage CHM
tags:
  - error
checksum: 6fa5f269d8e8e8c29716984609ea3df8d24bb54a
---

# Error 2166 Select Sub Query Returns More Than One Column

2166 SELECT sub-query returns more than one column

2166 SELECT sub-query returns more than one column

Advantage Error Guide

| 2166 SELECT sub-query returns more than one column  Advantage Error Guide |  |  |  |  |

Problem: A sub-query incorrectly specified more than one column in the SELECT list. For example, "SELECT field1, field2 FROM table1 WHERE field1 IN (SELECT \* FROM table2)" is not valid if table2 contains more than one field.

Solution: Change the sub-query so that it selects only a single column.
