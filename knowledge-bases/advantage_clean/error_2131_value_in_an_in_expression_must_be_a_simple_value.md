---
title: Error 2131 Value In An In Expression Must Be A Simple Value
slug: error_2131_value_in_an_in_expression_must_be_a_simple_value
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2131_value_in_an_in_expression_must_be_a_simple_value.htm
source: Advantage CHM
tags:
  - error
checksum: 5cc7d1caafe4456de35bf69c797df88312ad4c53
---

# Error 2131 Value In An In Expression Must Be A Simple Value

2131 Value in an IN expression must be a simple value

2131 Value in an IN expression must be a simple value

Advantage Error Guide

| 2131 Value in an IN expression must be a simple value  Advantage Error Guide |  |  |  |  |

Problem: The IN clause in the SQL statement contains an invalid value. For example, "SELECT \* FROM mytable WHERE field IN (2\*3)" is not valid.

Solution: The values in the IN clause must be simple constants, parameters, or the USER literal.
