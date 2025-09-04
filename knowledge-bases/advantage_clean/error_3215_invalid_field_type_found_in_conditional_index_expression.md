---
title: Error 3215 Invalid Field Type Found In Conditional Index Expression
slug: error_3215_invalid_field_type_found_in_conditional_index_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3215_invalid_field_type_found_in_conditional_index_expression.htm
source: Advantage CHM
tags:
  - error
checksum: d923d891c4addb235cdf6c52bd85e1ecc0d829f3
---

# Error 3215 Invalid Field Type Found In Conditional Index Expression

3215 Invalid field type found in conditional index expression

3215 Invalid field type found in conditional index expression

Advantage Error Guide

| 3215 Invalid field type found in conditional index expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The conditional index expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the conditional index expression. Memo fields are not supported by the Advantage Expression Engine parser.
