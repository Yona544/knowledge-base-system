---
title: Error 7095 The Full Text Search Condition Has An Unclosed Expression
slug: error_7095_the_full_text_search_condition_has_an_unclosed_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7095_the_full_text_search_condition_has_an_unclosed_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 3f1f60680ceafd934118a37aa9a79f60c874336a
---

# Error 7095 The Full Text Search Condition Has An Unclosed Expression

7095 The full text search condition has an unclosed expression

7095 The full text search condition has an unclosed expression

Advantage Error Guide

| 7095 The full text search condition has an unclosed expression  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition specified in a CONTAINS() function has an unclosed expression.

Solution: Verify that the parentheses are balanced in the search condition. For example, the search condition "medical and (doctor or nurse" is not valid because there is no closing parenthesis.
