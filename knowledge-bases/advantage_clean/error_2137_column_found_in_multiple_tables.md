---
title: Error 2137 Column Found In Multiple Tables
slug: error_2137_column_found_in_multiple_tables
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2137_column_found_in_multiple_tables.htm
source: Advantage CHM
tags:
  - error
checksum: 51e782278611013feded93861049c663bf070590
---

# Error 2137 Column Found In Multiple Tables

2137 Column found in multiple tables

2137 Column found in multiple tables

Advantage Error Guide

| 2137 Column found in multiple tables  Advantage Error Guide |  |  |  |  |

Problem: A column name in an SQL statement was found in multiple tables and, thus, was not uniquely identifiable.

Solution: Use a table alias or table name with the column name to uniquely identify it. For example, "SELECT field FROM table1, table2" is not valid if "field" exists in both "table1" and "table2" because it is ambiguous. You must specifically identify which table to use. For example, "SELECT table1.field from table1, table2".
