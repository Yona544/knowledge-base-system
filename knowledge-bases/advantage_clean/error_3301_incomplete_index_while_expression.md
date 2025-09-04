---
title: Error 3301 Incomplete Index While Expression
slug: error_3301_incomplete_index_while_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3301_incomplete_index_while_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 4c06c60ac3a926755bf853c96e6015a66bbe97d7
---

# Error 3301 Incomplete Index While Expression

3301 Incomplete index while expression

3301 Incomplete index while expression

Advantage Error Guide

| 3301 Incomplete index while expression  Advantage Error Guide |  |  |  |  |

An error occurred in the Advantage Expression Engine parser. The error was in the index While expression.

Problem 1: The expression is invalid. The expression may be invalid due to an extra right paren(s) plus possible other invalid text following that parenthesis. The expression may also be invalid to an extra, illegal comma placed within the expression plus possible other invalid text following that comma.

Solution 1: Delete any indexes that have an invalid expression and rebuild the index with a valid index expression.

Problem 2: The parse finished but the expression was incomplete.

Solution 2: If Solution 1 above does not solve the problem and the error persists, contact Advantage [Technical Support](master_technical_support_u_s__and_canada.md) and send in a small re-creation.
