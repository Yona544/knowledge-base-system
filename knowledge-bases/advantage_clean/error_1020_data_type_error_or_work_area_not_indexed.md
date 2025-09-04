---
title: Error 1020 Data Type Error Or Work Area Not Indexed
slug: error_1020_data_type_error_or_work_area_not_indexed
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_1020_data_type_error_or_work_area_not_indexed.htm
source: Advantage CHM
tags:
  - error
checksum: fc0dab56b43560483d936f4ba0c7a598d7ff3cab
---

# Error 1020 Data Type Error Or Work Area Not Indexed

1020 Data Type Error or Work Area not Indexed

1020 Data Type Error or Work Area not Indexed

Advantage Error Guide

| 1020 Data Type Error or Work Area not Indexed  Advantage Error Guide |  |  |  |  |

Problem 1: An invalid data type was assigned to a field in a table.

Solution 1: Correct the program. If assigning a value to a field in a table from some variable, make sure the variable has been initialized (i.e., is not NIL).

Problem 2: An operation, such as a Seek, was performed in the work area, but there was no index active.

Solution 2: Make sure that an index has been made active before performing the operation.
