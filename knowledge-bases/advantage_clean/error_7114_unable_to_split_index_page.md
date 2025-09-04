---
title: Error 7114 Unable To Split Index Page
slug: error_7114_unable_to_split_index_page
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7114_unable_to_split_index_page.htm
source: Advantage CHM
tags:
  - error
checksum: 76984404f46f429d9447242ce82fba1a359cd375
---

# Error 7114 Unable To Split Index Page

7114 Unable to split index page

7114 Unable to split index page

Advantage Error Guide

| 7114 Unable to split index page  Advantage Error Guide |  |  |  |  |

Problem: The current update operation required an index page split, but it was not possible to split the page.

Solution: This problem can occur if the key size is close (within a few bytes) of the maximum possible key size for the [index page size](master_index_page_size.md) and the key data cannot be compressed. If this error occurs with the ADT table type, rebuild the index with a larger page size.
