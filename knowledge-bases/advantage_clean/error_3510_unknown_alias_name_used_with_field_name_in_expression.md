---
title: Error 3510 Unknown Alias Name Used With Field Name In Expression
slug: error_3510_unknown_alias_name_used_with_field_name_in_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3510_unknown_alias_name_used_with_field_name_in_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 0ebff160ee621418038f82b19ca12559367f882e
---

# Error 3510 Unknown Alias Name Used With Field Name In Expression

3510 Unknown alias name used with field name in expression

3510 Unknown alias name used with field name in expression

Advantage Error Guide

| 3510 Unknown alias name used with field name in expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. A field name within the expression was aliased by an unknown alias name.

Solution: Advantage only supports aliases for the current work area. If an alias to another work area is referenced, this error will result. Verify the alias name is spelled properly.
