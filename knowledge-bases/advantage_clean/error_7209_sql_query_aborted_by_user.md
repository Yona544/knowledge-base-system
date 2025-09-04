---
title: Error 7209 Sql Query Aborted By User
slug: error_7209_sql_query_aborted_by_user
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7209_sql_query_aborted_by_user.htm
source: Advantage CHM
tags:
  - error
checksum: b5b838029e6eedf01042fe86a9014a6451e4375b
---

# Error 7209 Sql Query Aborted By User

7209 SQL query aborted by user

7209 SQL query aborted by user

Advantage Error Guide

| 7209 SQL query aborted by user  Advantage Error Guide |  |  |  |  |

Problem: The SQL query was aborted by the user.

Solution: If using ADO and executing a query that can take quite a while to complete, set the Command.CommandTimeout property to a value greater than its default of 30 seconds. If using ADO.Net and executing a query that can take quite a while to complete, set the OleDbCommand.CommandTimeout property to a value greater than its default of 30 seconds.
