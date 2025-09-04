---
title: Error 7103 The Full Text Search Condition Is Empty
slug: error_7103_the_full_text_search_condition_is_empty
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7103_the_full_text_search_condition_is_empty.htm
source: Advantage CHM
tags:
  - error
checksum: 439798164b4a377317ef512eaedd82261a91f8b0
---

# Error 7103 The Full Text Search Condition Is Empty

7103 The full text search condition is empty

7103 The full text search condition is empty

Advantage Error Guide

| 7103 The full text search condition is empty  Advantage Error Guide |  |  |  |  |

Problem: The full text search condition does not have any valid search words. It is possible, for example, to specify a search condition that contains only noise words. The full text search engine ignores noise words that are in the search condition. If the condition consists of nothing but noise words, or words that are shorter than the minimum word length, then the engine has nothing to search for.

Solution: Verify that the search condition consists of at least one non-noise word.
