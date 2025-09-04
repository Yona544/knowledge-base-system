---
title: Error 3411 Unknown Identifier Found In Is Expression Valid Function Expression
slug: error_3411_unknown_identifier_found_in_is_expression_valid_function_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3411_unknown_identifier_found_in_is_expression_valid_function_expression.htm
source: Advantage CHM
tags:
  - error
checksum: ec1623e238a4f9ba3b2196f8580190729712e594
---

# Error 3411 Unknown Identifier Found In Is Expression Valid Function Expression

3411 Unknown identifier found in "is expression valid" function expression

3411 Unknown identifier found in "is expression valid" function expression

Advantage Error Guide

| 3411 Unknown identifier found in "is expression valid" function expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. An identifier within the "is expression valid" function expression is unknown to the parser.

Solution: This error is usually caused by the use of memory variables within the "is expression valid" function expression. The Advantage Expression Engine does not support memory variables. The variables are visible only to the client. This error may also result from a misspelled field name or from a field name that does not exist in the current work area.
