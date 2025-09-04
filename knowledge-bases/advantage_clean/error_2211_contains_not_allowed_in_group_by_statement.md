---
title: Error 2211 Contains Not Allowed In Group By Statement
slug: error_2211_contains_not_allowed_in_group_by_statement
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2211_contains_not_allowed_in_group_by_statement.htm
source: Advantage CHM
tags:
  - error
checksum: 420cfff1577b8cc6cfbdb452b50880d98b397d77
---

# Error 2211 Contains Not Allowed In Group By Statement

2211 CONTAINS(\*) not allowed in GROUP BY statement

2211 CONTAINS(\*) not allowed in GROUP BY statement

Advantage Error Guide

| 2211 CONTAINS(\*) not allowed in GROUP BY statement  Advantage Error Guide |  |  |  |  |

Problem: A SELECT statement with a GROUP BY clause contained the scalar function CONTAINS with the "all columns" wild card (\*) as the first parameter.

Solution: When appearing in a statement with a GROUP BY clause, the CONTAINS scalar function can only be of the form where the first parameter is an explicit field name. It cannot use the \* (all columns) operator.
