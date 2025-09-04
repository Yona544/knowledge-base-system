---
title: Error 2149 Aggregate Function Not Allowed In This Context
slug: error_2149_aggregate_function_not_allowed_in_this_context
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2149_aggregate_function_not_allowed_in_this_context.htm
source: Advantage CHM
tags:
  - error
checksum: 93a45fd15935f2c8bd4f130084afb2206aed62f6
---

# Error 2149 Aggregate Function Not Allowed In This Context

2149 Aggregate function not allowed in this context

2149 Aggregate function not allowed in this context

Advantage Error Guide

| 2149 Aggregate function not allowed in this context  Advantage Error Guide |  |  |  |  |

Problem: An SQL statement used an aggregate function (SUM, AVG, MIN, MAX, COUNT) in an incorrect manner.

Solution: Do not use aggregate functions in column lists. For example, "INSERT INTO mytable (field) VALUES (MIN(field))" is not valid.
