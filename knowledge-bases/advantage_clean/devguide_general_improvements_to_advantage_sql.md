---
title: Devguide General Improvements To Advantage Sql
slug: devguide_general_improvements_to_advantage_sql
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_general_improvements_to_advantage_sql.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 2ba0303d242141abcd4e66b0b24dfa0c7dd597e0
---

# Devguide General Improvements To Advantage Sql

General Improvements to Advantage SQL

     General Improvements to Advantage SQL

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| General Improvements to Advantage SQL  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The support for SQL in Advantage 7 is excellent, and in this release it gets even better. For starters, Advantage 8.1 now supports both FULL and RIGHT OUTER joins. Additional improvements include permitting the use of subqueries anywhere an expression is permitted, permitting aliased column names in HAVING clauses, the use of TOP X in subqueries, and the introduction of an escape character in LIKE conditions.

Advantage SQL scripts can now also return a cursor. Specifically, if SELECT is the last statement in a SQL script, that script will return the records fetched by that SELECT statement.
