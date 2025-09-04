---
title: Error 3315 Invalid Field Type Found In Index While Expression
slug: error_3315_invalid_field_type_found_in_index_while_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3315_invalid_field_type_found_in_index_while_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 8c26fdffe040aa6e0b43adbee9f0bfeab056dfb9
---

# Error 3315 Invalid Field Type Found In Index While Expression

3315 Invalid field type found in index while expression

3315 Invalid field type found in index while expression

Advantage Error Guide

| 3315 Invalid field type found in index while expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The index while expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the while expression. Memo fields are not supported by the Advantage Expression Engine parser.
