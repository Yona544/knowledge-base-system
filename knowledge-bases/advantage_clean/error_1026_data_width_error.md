---
title: Error 1026 Data Width Error
slug: error_1026_data_width_error
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_1026_data_width_error.htm
source: Advantage CHM
tags:
  - error
checksum: b64a116df1dad140cd6f2cba95f6de6e3f33baac
---

# Error 1026 Data Width Error

1026 Data Width Error

1026 Data Width Error

Advantage Error Guide

| 1026 Data Width Error  Advantage Error Guide |  |  |  |  |

Problem: When building an index, the initial evaluation of the key expression (on a blank record) produced a character value of zero length.

Solution: Make sure the key expression will produce a value of the same length for all records. Do not use functions such as TRIM() in the key expression. To restrict the length of the key values, use the LEFT() or PADR() functions.
