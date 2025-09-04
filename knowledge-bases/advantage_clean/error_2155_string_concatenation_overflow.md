---
title: Error 2155 String Concatenation Overflow
slug: error_2155_string_concatenation_overflow
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2155_string_concatenation_overflow.htm
source: Advantage CHM
tags:
  - error
checksum: c9d2c47ee51571a99f81f450a003f06a9b86b61f
---

# Error 2155 String Concatenation Overflow

2155 String concatenation overflow

2155 String concatenation overflow

Advantage Error Guide

| 2155 String concatenation overflow  Advantage Error Guide |  |  |  |  |

Problem: The result of a string concatenation (with the + operator or the CONCAT scalar function) exceeded a computed expression length. In versions 7.0 and earlier, the result of these concatenations was limited to 1024 characters. This limitation has been removed. In 7.0 and later release, this error can occur if the SQL statement contains the expression ? + strExpr where ? is a parameter and its value is set to a string longer than 1024 characters.

Solution: Adjust the SQL statement to avoid exceeding the maximum literal length, or use a cast function to explicitly specify the precision of the character string parameter. For example: Cast( ? AS SQL\_VARCHAR( 2048)).
