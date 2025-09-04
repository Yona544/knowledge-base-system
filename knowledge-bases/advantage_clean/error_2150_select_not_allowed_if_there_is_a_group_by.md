---
title: Error 2150 Select Not Allowed If There Is A Group By
slug: error_2150_select_not_allowed_if_there_is_a_group_by
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_2150_select_not_allowed_if_there_is_a_group_by.htm
source: Advantage CHM
tags:
  - error
checksum: 624be4c807b60a9df36a07aff6bcbe5d803313e1
---

# Error 2150 Select Not Allowed If There Is A Group By

2150 SELECT \* not allowed if there is a GROUP BY

2150 SELECT \* not allowed if there is a GROUP BY

Advantage Error Guide

| 2150 SELECT \* not allowed if there is a GROUP BY  Advantage Error Guide |  |  |  |  |

Problem: An SQL statement used the \* token in a SELECT list when a GROUP BY clause was specified.

Solution: You must specifically name the columns in the SELECT list when a GROUP BY clause is used. The wildcard \* token is not allowed in that context.
