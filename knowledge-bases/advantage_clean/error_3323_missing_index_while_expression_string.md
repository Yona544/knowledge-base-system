---
title: Error 3323 Missing Index While Expression String
slug: error_3323_missing_index_while_expression_string
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3323_missing_index_while_expression_string.htm
source: Advantage CHM
tags:
  - error
checksum: 9afca31bde32963cb1d24e94d4dc2bd67679e2b9
---

# Error 3323 Missing Index While Expression String

3323 Missing index while expression string

3323 Missing index while expression string

Advantage Error Guide

| 3323 Missing index while expression string  Advantage Error Guide |  |  |  |  |

Problem: The user attempted to build an index on the server containing a while clause, but the application does not have an Advantage header file included in the source code. The while expression string could get passed to the Advantage server.

Solution: Include an appropriate Advantage header file in the application.
