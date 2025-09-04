---
title: Master Adi Conditional Indexes
slug: master_adi_conditional_indexes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_adi_conditional_indexes.htm
source: Advantage CHM
tags:
  - master
checksum: 28fd51d238c57d05c8fe3bbcccbdc7dbc6ce954d
---

# Master Adi Conditional Indexes

ADI Conditional Indexes

ADI Conditional Indexes

Advantage Concepts

| ADI Conditional Indexes  Advantage Concepts |  |  |  |  |

Conditional indexes are index orders that allow you to view only those data records that meet a pre-defined condition. Conditional indexes include only those records that satisfy a given filter expression. The conditional index expression may be any valid expression that evaluates to a logical value. Valid Advantage expressions can consist of field names, literal values, supported operators, and supported functions. For information on operators and functions supported in Advantage expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md). Conditional index expression text lengths are limited depending on which type of index is being built. The table below shows the maximum conditional index expression text length for each conditional index type.

| Index | Conditional Expression Length |
| ADI | 512 bytes\* |

\* For ADI indexes, the total length of the key expression text and conditional expression text combined must not exceed 512 characters, including an extra byte for each expression as a null terminator.

See Also

[Advantage Expression Engine](master_advantage_expression_engine.md)
