---
title: Error 2232 Numeric Overflow
slug: error_2232_numeric_overflow
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2232_numeric_overflow.htm
source: Advantage CHM
tags:
  - error
checksum: 44496795f9e273c1f6592d093b3690fe3bfd4a35
---

# Error 2232 Numeric Overflow

2232 Numeric Overflow

2232 Numeric Overflow

Advantage Error Guide

| 2232 Numeric Overflow  Advantage Error Guide |  |  |  |  |

Problem: The evaluation of an exact numeric expression exceeds the predetermined precision. This is a run time error. In addition, subtraction and multiplication operations, the scale of the exact numeric expression is determined following the SQL standards guideline and the precision is capped at the maximum supported value (30). If the result of evaluating exceed the supported precision, this error is returned.

Solution: Cast one of the operands to the approximate numeric (i.e., Double).

See Also

[Exact Numeric vs Approximate Numeric](master_exact_numeric_vs_approximate_numeric.md)
