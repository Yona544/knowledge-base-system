---
title: Error 3111 Unknown Identifier Found In The Record Filter Expression
slug: error_3111_unknown_identifier_found_in_the_record_filter_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3111_unknown_identifier_found_in_the_record_filter_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 19e425589e09440c3a6637bd59553dd8b5cba586
---

# Error 3111 Unknown Identifier Found In The Record Filter Expression

3111 Unknown identifier found in the record filter expression

3111 Unknown identifier found in the record filter expression

Advantage Error Guide

| 3111 Unknown identifier found in the record filter expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. An identifier within the record filter expression is unknown to the parser.

Solution: This error is usually caused by the use of memory variables within the record filter expression. Memory variables are not supported by the Advantage Expression Engine as the variables are visible only to the client. This error may also result from a misspelled field name or from a field name that does not exist in the current work area.
