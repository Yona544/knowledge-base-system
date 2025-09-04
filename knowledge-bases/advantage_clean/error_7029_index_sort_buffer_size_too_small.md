---
title: Error 7029 Index Sort Buffer Size Too Small
slug: error_7029_index_sort_buffer_size_too_small
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7029_index_sort_buffer_size_too_small.htm
source: Advantage CHM
tags:
  - error
checksum: e88f1ace891e854655e5385d0001ea2a8111fed2
---

# Error 7029 Index Sort Buffer Size Too Small

7029 Index Sort Buffer Size too small

7029 Index Sort Buffer Size too small

Advantage Error Guide

| 7029 Index Sort Buffer Size too small  Advantage Error Guide |  |  |  |  |

Problem: The Index Sort Buffer Size is not large enough for an index to be built on the server.

Solution: Restart/reload the Advantage server with a larger Index Sort Buffer Size. The Index Sort Buffer Size configuration key word is SORT\_BUFFER. The default sort buffer size is 8192 Kbytes. The range for this setting is 1 to 65535 Kbytes. The equation for calculating the minimum Index Sort Buffer Size is located in an Index Sort Buffer Size entry in the Advantage knowledge base. Search for SORT\_BUFFER.
