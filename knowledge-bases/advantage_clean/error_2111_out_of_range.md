---
title: Error 2111 Out Of Range
slug: error_2111_out_of_range
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2111_out_of_range.htm
source: Advantage CHM
tags:
  - error
checksum: ad5a36a9fe654d265bae177518190093fcb947a1
---

# Error 2111 Out Of Range

2111 Out of range

2111 Out of range

Advantage Error Guide

| 2111 Out of range  Advantage Error Guide |  |  |  |  |

Problem: A data conversion within the SQL engine exceeded the range of the target value. For example, a parameter value stored as a double may have exceeded a short integer field range. Or there is data corruption in the tables used by the SQL query.

Solutions:

| 1. | Verify that the statement is using compatible data types. |

| 2. | Verify that there is no corruption in the tables used by the SQL query, especially that there is no corruption in the date, time, or timestamp columns in the tables. |
