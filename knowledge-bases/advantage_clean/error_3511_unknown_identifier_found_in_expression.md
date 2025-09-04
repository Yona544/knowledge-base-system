---
title: Error 3511 Unknown Identifier Found In Expression
slug: error_3511_unknown_identifier_found_in_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3511_unknown_identifier_found_in_expression.htm
source: Advantage CHM
tags:
  - error
checksum: ac4a73edbb9918caac8e358532552074402359cb
---

# Error 3511 Unknown Identifier Found In Expression

3511 Unknown identifier found in expression

3511 Unknown identifier found in expression

Advantage Error Guide

| 3511 Unknown identifier found in expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. An identifier within the expression is unknown to the parser.

Solution: This error is usually caused by the use of memory variables within the expression. Memory variables are not supported by the Advantage Expression Engine as the variables are visible only to the client. This error may also result from a misspelled field name or from a field name that does not exist in the current work area.
