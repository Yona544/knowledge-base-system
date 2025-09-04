---
title: Error 4104 Advantage Expression Engine Evaluator Stack Overflow
slug: error_4104_advantage_expression_engine_evaluator_stack_overflow
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_4104_advantage_expression_engine_evaluator_stack_overflow.htm
source: Advantage CHM
tags:
  - error
checksum: 972fa76e0d4bc1780ca0edb41642f3ea122657d3
---

# Error 4104 Advantage Expression Engine Evaluator Stack Overflow

4104 Advantage Expression Engine evaluator stack overflow

4104 Advantage Expression Engine evaluator stack overflow

Advantage Error Guide

| 4104 Advantage Expression Engine evaluator stack overflow  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine evaluator. The result of the parsed record filter expression is too long to fit on the internal evaluator stack.

Solution: Verify that the expression result does not exceed 4196 bytes. If you are using a CONTAINS() (full text search) condition, verify that the search condition does not exceed 4196 characters.
