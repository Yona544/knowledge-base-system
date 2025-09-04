---
title: Error 2130 Insert Value Was Not Valid
slug: error_2130_insert_value_was_not_valid
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2130_insert_value_was_not_valid.htm
source: Advantage CHM
tags:
  - error
checksum: b8ef15158c25ee7d5e001b0cfffcaafc0debedf4
---

# Error 2130 Insert Value Was Not Valid

2130 Insert value was not valid

2130 Insert value was not valid

Advantage Error Guide

| 2130 Insert value was not valid  Advantage Error Guide |  |  |  |  |

Problem: A value in the INSERT value list was not valid. For example, "INSERT INTO mytable (field) VALUES ( sum(field2) )" is not valid.

Solution: The values in the INSERT list cannot be aggregate functions or logical expressions such as "3 < 4".
