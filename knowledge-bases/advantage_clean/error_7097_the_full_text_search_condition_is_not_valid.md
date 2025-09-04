---
title: Error 7097 The Full Text Search Condition Is Not Valid
slug: error_7097_the_full_text_search_condition_is_not_valid
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7097_the_full_text_search_condition_is_not_valid.htm
source: Advantage CHM
tags:
  - error
checksum: f1dc00fcefed36f5cd3c8e0007ae3176848a5b82
---

# Error 7097 The Full Text Search Condition Is Not Valid

7097 The full text search condition is not valid

7097 The full text search condition is not valid

Advantage Error Guide

| 7097 The full text search condition is not valid  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition specified in a CONTAINS() function has extraneous information at the end of the condition, or it does not have balanced parentheses.

Solution: Verify that the parentheses and logical operators are balanced. For example, the search condition "medical and doctor)" is not valid because it does not have an opening parenthesis.
