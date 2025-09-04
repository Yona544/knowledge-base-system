---
title: Error 3115 Invalid Field Type Found In The Record Filter Expression
slug: error_3115_invalid_field_type_found_in_the_record_filter_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3115_invalid_field_type_found_in_the_record_filter_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 5719c29c07233f1d27c3858dbe3537d3e2b46bfc
---

# Error 3115 Invalid Field Type Found In The Record Filter Expression

3115 Invalid field type found in the record filter expression

3115 Invalid field type found in the record filter expression

Advantage Error Guide

| 3115 Invalid field type found in the record filter expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. The record filter expression contained an invalid field type.

Solution: This error is most likely due to the use of a memo field within the record filter expression. Memo fields are not supported by the Advantage Expression Engine parser.
