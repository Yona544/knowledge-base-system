---
title: Error 3011 Unknown Identifier Found In Index Key Expression
slug: error_3011_unknown_identifier_found_in_index_key_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3011_unknown_identifier_found_in_index_key_expression.htm
source: Advantage CHM
tags:
  - error
checksum: a7e269a2ca10aea88e97df3cdeca0c68b2694d87
---

# Error 3011 Unknown Identifier Found In Index Key Expression

3011 Unknown identifier found in index key expression

3011 Unknown identifier found in index key expression

Advantage Error Guide

| 3011 Unknown identifier found in index key expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. An identifier within the index key expression is unknown to the parser.

Solution: This error is usually caused by the use of memory variables within the key expression. Memory variables are not supported by the Advantage Expression Engine as the variables are visible only to the client. This error may also result from a misspelled field name or from a field name that does not exist in the current work area.
