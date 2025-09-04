---
title: Error 2227 Assignment Out Of Range In The Sql Script
slug: error_2227_assignment_out_of_range_in_the_sql_script
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2227_assignment_out_of_range_in_the_sql_script.htm
source: Advantage CHM
tags:
  - error
checksum: f81c5ca3f4cafbe69b2d718d77c7ff16f276e5ac
---

# Error 2227 Assignment Out Of Range In The Sql Script

2227 Assignment out of range in the SQL script

2227 Assignment out of range in the SQL script

Advantage Error Guide

| 2227 Assignment out of range in the SQL script  Advantage Error Guide |  |  |  |  |

Problem: The value assigned to a variable is out of the range supported by the type of the variable.

Solution: Check the error message for the location of the error in the script and ensure that that the value assigned to the variable is within the support range for the variable. Variables declared in an SQL script have the same range as the corresponding field type. See [ADT Field Types and Specifications](master_adt_field_types_and_specifications.md) or [DBF Field Types and Specifications](master_dbf_field_types_and_specifications.md) for field type specification details.
