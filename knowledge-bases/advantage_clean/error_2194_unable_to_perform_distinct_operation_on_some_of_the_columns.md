---
title: Error 2194 Unable To Perform Distinct Operation On Some Of The Columns
slug: error_2194_unable_to_perform_distinct_operation_on_some_of_the_columns
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2194_unable_to_perform_distinct_operation_on_some_of_the_columns.htm
source: Advantage CHM
tags:
  - error
checksum: 6021b3b9e22d04fc33ac4f20023c178a1cfeaa52
---

# Error 2194 Unable To Perform Distinct Operation On Some Of The Columns

2194 Unable to perform DISTINCT operation on some of the columns

2194 Unable to perform DISTINCT operation on some of the columns

Advantage Error Guide

| 2194 Unable to perform DISTINCT operation on some of the columns  Advantage Error Guide |  |  |  |  |

Problem: The DISTINCT operation cannot be performed on some columns in the result set. DISTINCT operation will fail if the query contains any of the following column types in the result set: character or binary columns that are larger than 1 KB, or MEMO, BLOB, or VARCHAR columns.

Solution: Adjust the SELECT list so it does not include any offending column.
