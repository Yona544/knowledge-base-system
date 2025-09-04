---
title: Error 6012 Invalid Key Length
slug: error_6012_invalid_key_length
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6012_invalid_key_length.htm
source: Advantage CHM
tags:
  - error
checksum: 81f1ac30b34320f2dfaf13d91d086cf1c3df8284
---

# Error 6012 Invalid Key Length

6012 Invalid key length

6012 Invalid key length

Advantage Error Guide

| 6012 Invalid key length  Advantage Error Guide |  |  |  |  |

Problem: The key length of the stored index and the actual length when evaluating the key expression were different.

Solution: Make sure the key expression will produce a value of the same length for all records. Do not use functions such as TRIM() in the key expression. To restrict the length of the key values, use the LEFT() or PADR() functions. If a User-Defined Function (UDF) is used in the key expression, verify that the same function is available in all applications that use the index and that the function returns a value of the same length for all records.
