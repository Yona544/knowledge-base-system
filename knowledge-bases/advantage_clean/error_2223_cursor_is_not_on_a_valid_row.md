---
title: Error 2223 Cursor Is Not On A Valid Row
slug: error_2223_cursor_is_not_on_a_valid_row
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2223_cursor_is_not_on_a_valid_row.htm
source: Advantage CHM
tags:
  - error
checksum: 0b8b6f81c23b0298c79ec785aae0d3c8b3b2a742
---

# Error 2223 Cursor Is Not On A Valid Row

2223 Cursor is not on a valid row

2223 Cursor is not on a valid row

Advantage Error Guide

| 2223 Cursor is not on a valid row  Advantage Error Guide |  |  |  |  |

Problem: Data from the column could not be read because the cursor is not on a valid row. The row pointer is either before the first row or after the last row in the cursor.

Solution: Check the error message for the location of the error in the script. Verify that FETCH is called on the cursor before reading the column data and that the result from the FETCH statement is checked before trying to access the data.
