---
title: Error 3210 Unknown Alias Name Used With Field Name In Conditional Index Expression
slug: error_3210_unknown_alias_name_used_with_field_name_in_conditional_index_expression
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_3210_unknown_alias_name_used_with_field_name_in_conditional_index_expression.htm
source: Advantage CHM
tags:
  - error
checksum: 5f052ad6687ee7e61733fce7a961787ba193577c
---

# Error 3210 Unknown Alias Name Used With Field Name In Conditional Index Expression

3210 Unknown alias name used with field name in conditional index expression

3210 Unknown alias name used with field name in conditional index expression

Advantage Error Guide

| 3210 Unknown alias name used with field name in conditional index expression  Advantage Error Guide |  |  |  |  |

Problem: An error occurred in the Advantage Expression Engine parser. A field name within the conditional index expression was aliased by an unknown alias name.

Solution: Advantage only supports aliases for the current work area. If an alias to another work area is referenced, this error will result. Verify the alias name is spelled properly.
