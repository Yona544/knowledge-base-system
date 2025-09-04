---
title: Error 2212 Aggregate Cannot Be Nested
slug: error_2212_aggregate_cannot_be_nested
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2212_aggregate_cannot_be_nested.htm
source: Advantage CHM
tags:
  - error
checksum: a318aed8dcff43449f7ee386134366a250c6f86e
---

# Error 2212 Aggregate Cannot Be Nested

2212 Aggregate cannot be nested

2212 Aggregate cannot be nested

Advantage Error Guide

| 2212 Aggregate cannot be nested  Advantage Error Guide |  |  |  |  |

Problem: The expression for an aggregate function (MIN, MAX, SUM, AVG or COUNT) contains another aggregate function. For example: SUM( MIN( id )).

Solution: The nested aggregate is not a valid SQL expression.
