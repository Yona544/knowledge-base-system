---
title: Error 3010 Unknown Alias Name Used With Field Name In Index Key Expression
slug: error_3010_unknown_alias_name_used_with_field_name_in_index_key_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3010_unknown_alias_name_used_with_field_name_in_index_key_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 9a460e94e99d841a6c9f832a007cd045e075c087
---

# Error 3010 Unknown Alias Name Used With Field Name In Index Key Expression

3010 Unknown alias name used with field name in index key expression

3010 Unknown alias name used with field name in index key expression

Advantage Error Guide

| 3010 Unknown alias name used with field name in index key expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. A field name within the key expression was aliased by an unknown alias name.

Solution: Advantage only supports aliases for the current work area. If an alias to another work area is referenced, this error will result. Verify the alias name is spelled properly.
