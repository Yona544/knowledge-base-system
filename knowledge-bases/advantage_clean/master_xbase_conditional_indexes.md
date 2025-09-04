---
title: Master Xbase Conditional Indexes
slug: master_xbase_conditional_indexes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_xbase_conditional_indexes.htm
source: Advantage CHM
tags:
  - master
checksum: fa669c170e3137f50f41428f0152704816979837
---

# Master Xbase Conditional Indexes

Xbase Conditional Indexes

Xbase Conditional Indexes

Advantage Concepts

| Xbase Conditional Indexes  Advantage Concepts |  |  |  |  |

Conditional indexes are index orders that allow you to view only those data records that meet a pre-defined condition. Conditional indexes include only those records that satisfy a given filter expression. The conditional index expression may be any valid expression that evaluates to a logical value. Valid Advantage expressions can consist of field names, literal values, supported operators, and supported functions. For information on operators and functions supported in Advantage expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md). Conditional index expression text lengths are limited depending on which type of index is being built. The table below shows the maximum conditional index expression text length for each conditional index type.

| Index | Conditional Expression Length |
| NTX | 256 bytes |
| IDX | 512 bytes\* |
| CDX | 512 bytes\* |

\* For IDX and CDX indexes, the total length of the key expression text and conditional expression text combined must not exceed 512 characters, including an extra byte for each expression as a null terminator.

See Also

[Advantage Expression Engine](master_advantage_expression_engine.md)
