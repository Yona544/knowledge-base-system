---
title: Error 3410 Unknown Alias Name Used With Field Name In Is Expression Valid Function Expression
slug: error_3410_unknown_alias_name_used_with_field_name_in_is_expression_valid_function_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3410_unknown_alias_name_used_with_field_name_in_is_expression_valid_function_expression.htm
source: Advantage CHM
tags:
  - error
checksum: c20ac21b0a658d30f0f7952e9fdeaf367c33ac7c
---

# Error 3410 Unknown Alias Name Used With Field Name In Is Expression Valid Function Expression

3410 Unknown alias name used with field name in "is expression valid" function expression

3410 Unknown alias name used with field name in "is expression valid" function expression

Advantage Error Guide

| 3410 Unknown alias name used with field name in "is expression valid" function expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. A field name within the "is expression valid" function expression was aliased by an unknown alias name.

Solution: Advantage only supports aliases for the current work area. If an alias to another work area is referenced, this error will result. Verify the alias name is spelled properly.
