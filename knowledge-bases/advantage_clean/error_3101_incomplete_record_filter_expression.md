---
title: Error 3101 Incomplete Record Filter Expression
slug: error_3101_incomplete_record_filter_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3101_incomplete_record_filter_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 81471712225270a0eed23c32890018b9ad2cdfe2
---

# Error 3101 Incomplete Record Filter Expression

3101 Incomplete record filter expression

3101 Incomplete record filter expression

Advantage Error Guide

| 3101 Incomplete record filter expression  Advantage Error Guide |  |  |  |  |

An error occurred in the Advantage Expression Engine parser. The error was in the record filter expression.

Problem 1: The expression is invalid. The expression may be invalid due to an extra right paren(s) plus possible other invalid text following that parenthesis. The expression may also be invalid to an extra, illegal comma placed within the expression plus possible other invalid text following that comma.

Solution 1: Change any filters that use an invalid expression and re-set the filter using a valid expression.

Problem 2: The parse finished but the expression was incomplete.

Solution 2: If Solution 1 above does not solve the problem and the error persists, contact Advantage [Technical Support](master_technical_support_u_s__and_canada.md) and send in a small re-creation.
