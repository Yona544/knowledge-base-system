---
title: Error 3515 Invalid Field Type Found In Expression
slug: error_3515_invalid_field_type_found_in_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3515_invalid_field_type_found_in_expression.htm
source: Advantage CHM
tags:
  - error
checksum: bfaadf2741d2be1617fa934aeaa52e800989387e
---

# Error 3515 Invalid Field Type Found In Expression

3515 Invalid field type found in expression

3515 Invalid field type found in expression

Advantage Error Guide

| 3515 Invalid field type found in expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the expression. Memo fields are not supported by the Advantage Expression Engine parser.
