---
title: Error 2134 Invalid Column Name
slug: error_2134_invalid_column_name
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2134_invalid_column_name.htm
source: Advantage CHM
tags:
  - error
checksum: cc84c541a7172366fe655cc01d4ea340f8eee86c
---

# Error 2134 Invalid Column Name

2134 Invalid column name

2134 Invalid column name

Advantage Error Guide

| 2134 Invalid column name  Advantage Error Guide |  |  |  |  |

Problem: The column name in a CREATE TABLE statement is not valid.

Solution: Verify that the column name is not too long for the table type. DBF tables are limited to 10 characters. Visual FoxPro (VFP) tables that are in a data dictionary are limited to 128 characters. ADT tables in SQL usage are limited to 128 characters.
