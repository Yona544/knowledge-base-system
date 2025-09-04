---
title: Error 7096 The Full Text Search Condition Is Missing A Phrase Or Word
slug: error_7096_the_full_text_search_condition_is_missing_a_phrase_or_word
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7096_the_full_text_search_condition_is_missing_a_phrase_or_word.htm
source: Advantage CHM
tags:
  - error
checksum: 0d8823a11304f284c3bbb8c86800583466e9e7a6
---

# Error 7096 The Full Text Search Condition Is Missing A Phrase Or Word

7096 The full text search condition is missing a phrase or word

7096 The full text search condition is missing a phrase or word

Advantage Error Guide

| 7096 The full text search condition is missing a phrase or word  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition specified in a CONTAINS() function is not formed correctly. It is missing an expected search word or sub-expression.

Solution: Verify that the search condition is not empty and that logical operators are balanced with search words. For example, the search condition "medical and or doctor" is not valid because a search word or condition is expected after the logical operator "and".
