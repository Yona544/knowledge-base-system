---
title: Error 2222 Invalid Cursor Column Reference
slug: error_2222_invalid_cursor_column_reference
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2222_invalid_cursor_column_reference.htm
source: Advantage CHM
tags:
  - error
checksum: 6f7f6aabe88d819c890d0fea70f452aba460b6fa
---

# Error 2222 Invalid Cursor Column Reference

2222 Invalid cursor column reference

2222 Invalid cursor column reference

Advantage Error Guide

| 2222 Invalid cursor column reference  Advantage Error Guide |  |  |  |  |

Problem: A cursor column reference in an expression is not valid. The column name may not be valid or the data type of the column may not be valid for the expression.

Solution: Check the error message for the location of the error in the script. Check that the column is in the cursor. If the cursor is opened and closed with a different cursor definition, the column name must correspond to a column in the cursor that is currently open.
