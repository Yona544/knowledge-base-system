---
title: Error 3015 Invalid Field Type Found In Index Key Expression
slug: error_3015_invalid_field_type_found_in_index_key_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3015_invalid_field_type_found_in_index_key_expression.htm
source: Advantage CHM
tags:
  - error
checksum: d147999d502335da02abd2e4dad4ed2e53dc60e5
---

# Error 3015 Invalid Field Type Found In Index Key Expression

3015 Invalid field type found in index key expression

3015 Invalid field type found in index key expression

Advantage Error Guide

| 3015 Invalid field type found in index key expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The index key expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the key expression. Memo fields are not supported by the Advantage Expression Engine parser.
