---
title: Error 2231 Numeric Result Out Of Range
slug: error_2231_numeric_result_out_of_range
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2231_numeric_result_out_of_range.htm
source: Advantage CHM
tags:
  - error
checksum: 599c323adcdf633a96859d0d4f1a9d2352dfb4a0
---

# Error 2231 Numeric Result Out Of Range

2231 Numeric Result Out Of Range

2231 Numeric Result Out Of Range

Advantage Error Guide

| 2231 Numeric Result Out Of Range  Advantage Error Guide |  |  |  |  |

Problem: The result of an exact numeric expression exceeds the range of resultant data type. An example is multiplication of two exact numeric values with large-scale (digits after the decimal point) values. This error may be returned during query preparation or query evaluation. Another example will be when the result of an expression with integer operands exceed the range of a signed 32 bit integer value.

Solution: Cast one of the operands to the approximate numeric (i.e., Double) or to an exact numeric with larger range.

See Also

[Exact Numeric vs Approximate Numeric](master_exact_numeric_vs_approximate_numeric.md)
