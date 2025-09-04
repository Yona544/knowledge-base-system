---
title: Master Aof Relational Operators
slug: master_aof_relational_operators
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_aof_relational_operators.htm
source: Advantage CHM
tags:
  - master
checksum: 05b89dc5220ff6eb2fe10f78baad843578c0321a
---

# Master Aof Relational Operators

AOF Relational Operators

AOF Relational Operators

Advantage Concepts

| AOF Relational Operators  Advantage Concepts |  |  |  |  |

Advantage Optimized Filters support the following relational operators. See [Expression Engine Operators](master_expression_engine_operators.md) for details.

| Operator | Description |
| = | Equal to |
| == | Strict equality for string comparison |
| < | Less than |
| <= | Less than or equal to |
| > | Greater than |
| >= | Greater than or equal to |
| #, !=, <> | Not equal to |
| $ | String containment |

For the string containment operator ($) to be optimized, it must have the field name on the left side of the operator just as with the other operators. For example, the filter expression "x $ lastname", which will find all records that have the character x in the field "lastname", will not be optimized. The containment operator can be used to efficiently find all records that have one of a set of specific characters in a specific location. For example, if the index "SUBSTR(category, 3, 1)" existed, then the filter expression "SUBSTR(category, 3, 1) $ aAbB" would be fully optimized and would find all records that have either an A, a, B, or b in the third character of field "category". It can also be used for longer substrings, but it would generally be more efficient to use several simple expressions joined with the logical .OR. operator.
