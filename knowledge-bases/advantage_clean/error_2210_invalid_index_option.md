---
title: Error 2210 Invalid Index Option
slug: error_2210_invalid_index_option
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2210_invalid_index_option.htm
source: Advantage CHM
tags:
  - error
checksum: f3ea013e9a171e6f121c89803a0d92807c4023fb
---

# Error 2210 Invalid Index Option

2210 Invalid index option

2210 Invalid index option

Advantage Error Guide

| 2210 Invalid index option  Advantage Error Guide |  |  |  |  |

Problem: An option in a CREATE INDEX statement was not valid.

Solution: Verify that the options specified in the CREATE INDEX statement are valid. If you specified options for creating a full text search index, verify that the keyword CONTENT is provided. If the CONTENT keyword is provided, verify that the UNIQUE and DESC keywords are not specified.
