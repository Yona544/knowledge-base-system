---
title: Master Supported Aggregate Column Functions
slug: master_supported_aggregate_column_functions
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_supported_aggregate_column_functions.htm
source: Advantage CHM
tags:
  - master
checksum: beceb68a9261232b98334e67d99b4f42c5c093ce
---

# Master Supported Aggregate Column Functions

Supported Aggregate (column) Functions

Supported Aggregate (column) Functions

Advantage SQL Engine

| Supported Aggregate (column) Functions  Advantage SQL Engine |  |  |  |  |

expr = column name or SQL expression

| AVG( expr ) | Calculates the average of a set of values. |
| COUNT( [ ALL | DISTINCT ] expr ) | Returns the number of non-NULL column items that satisfy a querys search condition. The ALL keyword is the default action and the DISTINCT keyword returns the number of non-NULL and distinct column items. |
| COUNT(\*) | Returns the number of rows that satisfy a querys search condition. |
| MAX( expr ) | Returns the maximum of a set of values. |
| MIN( expr ) | Returns the minimum of a set of values. |
| SUM( expr ) | Totals the values in a set of numeric values. |
| GROUP\_CONCAT( [DISTINCT] expr [ORDER BY expr [DESC], ...] [SEPARATOR string\_literal] [MAX\_LENGTH integer] ) | Returns the non-NULL character values in the group concatenated into a single string value. The values in the string are separated using comma (,) if SEPARATOR is not specified. The maximum length of result is 1024 character if the MAX\_LENGTH is not specified. The MAX\_LENGTH can be up to 3200 characters. If the result is longer than the maximum length, the data truncation error will be returned. The ORDER BY clause can be used to sort the values in the result. The DISTINCT clause is used to remove duplicated values in the result. |

 

Note NULL values are ignored; The ALL keyword is only supported with the COUNT aggregate. The DISTINCT keyword is supported with the COUNT and GROUP\_CONCAT aggregates.

Examples

SELECT AVG(quota), AVG(sales) FROM salesinfo

SELECT AVG(100 \* (sales/quota)) FROM salesinfo

 

SELECT COUNT(empid) FROM employees

SELECT COUNT(ordernum) FROM orders WHERE amount > 1000

SELECT COUNT(\*) FROM orders WHERE amount > 1000

 

SELECT MIN(quota), MAX(quota) FROM salesinfo

SELECT MAX(100 \* (sales/quota)) FROM salesinfo

SELECT MIN(100 \* (sales/quota)) FROM salesinfo

 

SELECT SUM(quota), SUM(sales) FROM salesinfo

SELECT SUM(sales - quota) FROM salesinfo

 

SELECT Branch, GROUP\_CONCAT( lastname ) FROM employees GROUP BY Branch

 

SELECT

  Branch,

  GROUP\_CONCAT( lastname + ',' + Firstname SEPARATOR ';' )

FROM employees

GROUP BY Branch

 

SELECT

  GROUP\_CONCAT( DISTINCT language ORDER BY language )

FROM employees
