---
title: Error 4004 Advantage Expression Engine Evaluator Stack Overflow
slug: error_4004_advantage_expression_engine_evaluator_stack_overflow
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_4004_advantage_expression_engine_evaluator_stack_overflow.htm
source: Advantage CHM
tags:
  - error
checksum: 4808c4c2035e7e7c7901a433fb573a9779539b72
---

# Error 4004 Advantage Expression Engine Evaluator Stack Overflow

4004 Advantage Expression Engine evaluator stack overflow

4004 Advantage Expression Engine evaluator stack overflow

Advantage Error Guide

| 4004 Advantage Expression Engine evaluator stack overflow  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine evaluator. The result of the parsed index key expression is too long to fit on the internal evaluator stack.

Solution: 4004 errors are typically caused by modifying a table's structure without deleting and re-building the index. 4004 errors are also caused by variable length index keys being created, often as a result of using a TRIM function in the index expression without using a PAD function.

Problem: A string literal specified in the Advantage Optimized Filter expression is too long.

Solution: 4004 error can be caused by a string literal value that is longer than 4KB. Such expression cannot be evaluated by the Advantage expression engine.
