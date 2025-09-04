---
title: Error 3415 Invalid Field Type Found In Is Expression Valid Function Expression
slug: error_3415_invalid_field_type_found_in_is_expression_valid_function_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3415_invalid_field_type_found_in_is_expression_valid_function_expression.htm
source: Advantage CHM
tags:
  - error
checksum: aa0ab8b605af2306f4fa1ad24dbdf0493cd7ac70
---

# Error 3415 Invalid Field Type Found In Is Expression Valid Function Expression

3415 Invalid field type found in "is expression valid" function expression

3415 Invalid field type found in "is expression valid" function expression

Advantage Error Guide

| 3415 Invalid field type found in "is expression valid" function expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The "is expression valid" function expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the "is expression valid" function expression. Memo fields are not supported by the Advantage Expression Engine parser.
