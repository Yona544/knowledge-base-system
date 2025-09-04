---
title: Error 2133 Column On List Multiple Times
slug: error_2133_column_on_list_multiple_times
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2133_column_on_list_multiple_times.htm
source: Advantage CHM
tags:
  - error
checksum: 62ccca4c3fd95117409d3d58572927c7363511e4
---

# Error 2133 Column On List Multiple Times

2133 Column on list multiple times

2133 Column on list multiple times

Advantage Error Guide

| 2133 Column on list multiple times  Advantage Error Guide |  |  |  |  |

Problem: A column list in the SQL statement contained a column name multiple times. For example, "INSERT INTO mytable (field1, field1) VALUES (1, 2)" is not valid.

Solution: Verify that the column list names each field only once.
