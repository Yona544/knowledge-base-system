---
title: Error 2216 Unexpected End Of The Sql Script
slug: error_2216_unexpected_end_of_the_sql_script
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2216_unexpected_end_of_the_sql_script.htm
source: Advantage CHM
tags:
  - error
checksum: 483ccace1dc48920892da64e9f422b0208e54fd6
---

# Error 2216 Unexpected End Of The Sql Script

2216 Unexpected end of the SQL script

2216 Unexpected end of the SQL script

Advantage Error Guide

| 2216 Unexpected end of the SQL script  Advantage Error Guide |  |  |  |  |

Problem: The SQL script cannot be parsed correctly because the expected block ending token was not found.

Solution: Make sure the script is written correctly. Verify that all control statements, such as IF, WHILE, and TRY statements, have corresponding END [xxx] tokens to denote the end of the control statement.
