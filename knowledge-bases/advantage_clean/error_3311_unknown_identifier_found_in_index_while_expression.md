---
title: Error 3311 Unknown Identifier Found In Index While Expression
slug: error_3311_unknown_identifier_found_in_index_while_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3311_unknown_identifier_found_in_index_while_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 9b6a80ff64e29c38954039dd2458b60075436c95
---

# Error 3311 Unknown Identifier Found In Index While Expression

3311 Unknown identifier found in index while expression

3311 Unknown identifier found in index while expression

Advantage Error Guide

| 3311 Unknown identifier found in index while expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. An identifier within the while expression is unknown to the parser.

Solution: This error is usually caused by the use of memory variables within the while expression. Memory variables are not supported by the Advantage Expression Engine as the variables are visible only to the client. This error may also result from a misspelled field name or from a field name that does not exist in the current work area.
