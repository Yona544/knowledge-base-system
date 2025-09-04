---
title: Error 3310 Unknown Alias Name Used With Field Name In Index While Expression
slug: error_3310_unknown_alias_name_used_with_field_name_in_index_while_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3310_unknown_alias_name_used_with_field_name_in_index_while_expression.htm
source: Advantage CHM
tags:
  - error
checksum: df0b59cc64bf7f674dcc3119a779a5a007da44e1
---

# Error 3310 Unknown Alias Name Used With Field Name In Index While Expression

3310 Unknown alias name used with field name in index while expression

3310 Unknown alias name used with field name in index while expression

Advantage Error Guide

| 3310 Unknown alias name used with field name in index while expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. A field name within the expression was aliased by an unknown alias name.

Solution: Advantage only supports aliases for the current work area. If an alias to another work area is referenced, this error will result. Verify the alias name is spelled properly.
