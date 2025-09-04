---
title: Error 2153 Division By Zero
slug: error_2153_division_by_zero
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2153_division_by_zero.htm
source: Advantage CHM
tags:
  - error
checksum: e1d4db82da98e927c6c4522a033e294eba76ddb1
---

# Error 2153 Division By Zero

2153 Division by zero

2153 Division by zero

Advantage Error Guide

| 2153 Division by zero  Advantage Error Guide |  |  |  |  |

Problem: The SQL engine detected a division by zero error while executing the statement.

Solution: Modify the SQL statement so that it does not produce division by zero errors. If, for example, your statement is "SELECT 1.0 / value FROM mytable", you might want to add a WHERE clause of the form "WHERE value <> 0" to avoid division by zero.
