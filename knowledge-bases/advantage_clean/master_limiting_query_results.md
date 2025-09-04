---
title: Master Limiting Query Results
slug: master_limiting_query_results
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_limiting_query_results.htm
source: Advantage CHM
tags:
  - master
checksum: 3c448ce1899485248fbd5248c764f3af836c99f5
---

# Master Limiting Query Results

Limiting Query Results

Limiting Query Results

Advantage SQL Engine

| Limiting Query Results  Advantage SQL Engine |  |  |  |  |

To explicitly limit the number of rows in query result set use a TOP clause.  Including TOP  x PERCENT will retrieve specified percentage of rows in the result set starting from the beginning.  Including TOP x will retrieve the specified number of rows in the result set starting at the first record.  When using TOP x a starting offset can be included using the START AT clause.

The following query will return the first 10 employees:

SELECT TOP 10 \* FROM emp

To return the next 10 employees in the table the following query would be used:

SELECT TOP 10 START AT 11 \* FROM emp

The START AT value must be greater than 0 and the TOP X value must be greater than or equal to 0.

Unless an ORDER BY clause is included the server will stop processing the query once it has determined the number of rows necessary for the result set.  If an ORDER BY clause is specified the server must populate the entire cursor in order to determine the order of the records.  The usage of TOP x and TOP x PERCENT syntax will force all queries to return static cursors.

See Also

[SELECT](master_select.md)
