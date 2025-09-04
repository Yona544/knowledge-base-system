---
title: Error 3110 Unknown Alias Name Used With Field Name In The Record Filter Expression
slug: error_3110_unknown_alias_name_used_with_field_name_in_the_record_filter_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3110_unknown_alias_name_used_with_field_name_in_the_record_filter_expression.htm
source: Advantage CHM
tags:
  - error
checksum: c430cd12d43095e700111e30e3aab72949a72bca
---

# Error 3110 Unknown Alias Name Used With Field Name In The Record Filter Expression

3110 Unknown alias name used with field name in the record filter expression

3110 Unknown alias name used with field name in the record filter expression

Advantage Error Guide

| 3110 Unknown alias name used with field name in the record filter expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. A field name within the record filter expression was aliased by an unknown alias name.

Solution: Advantage only supports aliases for the current work area. If an alias to another work area is referenced, this error will result. Verify the alias name is spelled properly.
