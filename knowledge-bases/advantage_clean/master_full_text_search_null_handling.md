---
title: Master Full Text Search Null Handling
slug: master_full_text_search_null_handling
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_full_text_search_null_handling.htm
source: Advantage CHM
tags:
  - master
checksum: 0ec54947aba2b3f4e5c5b108a359c7925cb09a88
---

# Master Full Text Search Null Handling

Full Text Search Null Handling

Full Text Search Null Handling

Advantage Concepts

| Full Text Search Null Handling  Advantage Concepts |  |  |  |  |

In general, a NULL value in an expression causes the expression to result in NULL. For example, the expression "lastname <> 'Smith'" returns NULL for records where lastname is NULL (and those record are not returned in an SQL result set with that condition).

The CONTAINS scalar function works similarly. CONTAINS(fieldname, search condition) returns NULL for records where the fieldname is NULL regardless of the condition.

The behavior of CONTAINS( \*, search condition ) is slightly different however. If any FTS-indexed field matches the search condition, the record passes the filter even if one of the fields contains a NULL value.
