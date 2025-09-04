---
title: Error 3211 Unknown Identifier Found In Conditional Index Expression
slug: error_3211_unknown_identifier_found_in_conditional_index_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3211_unknown_identifier_found_in_conditional_index_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 8a9fc3ca4624f4a3d62110d04675aabf0fb20bd1
---

# Error 3211 Unknown Identifier Found In Conditional Index Expression

3211 Unknown identifier found in conditional index expression

3211 Unknown identifier found in conditional index expression

Advantage Error Guide

| 3211 Unknown identifier found in conditional index expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. An identifier within the conditional index expression is unknown to the parser.

Solution: This error is usually caused by the use of memory variables within the conditional index expression. Memory variables are not supported by the Advantage Expression Engine as the variables are visible only to the client. This error may also result from a misspelled field name or from a field name that does not exist in the current work area.
