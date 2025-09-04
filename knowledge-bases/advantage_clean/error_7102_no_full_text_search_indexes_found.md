---
title: Error 7102 No Full Text Search Indexes Found
slug: error_7102_no_full_text_search_indexes_found
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7102_no_full_text_search_indexes_found.htm
source: Advantage CHM
tags:
  - error
checksum: c763de7cb864fd142b68218a53e4d82ecc491f0d
---

# Error 7102 No Full Text Search Indexes Found

7102 No full text search indexes found

7102 No full text search indexes found

Advantage Error Guide

| 7102 No full text search indexes found  Advantage Error Guide |  |  |  |  |

Problem: Use of CONTAINS( \*, 'condition' ) requires at least one full text search index. The asterisk (\*) indicates that all fields that have full text search indexes are to be searched, but the table does not have any full text search indexes available or the user does not have read permissions to any of the columns that have full text search indexes.

Solution: Create at least one full text search index or specify a particular field to search in the CONTAINS condition. If using a data dictionary with permissions checking turned on, verify that the user has read permission to at least one column that has a full text search index. Note that specifying a specific field to search that does not have a full text search index forces a low level search of the data, which can be slow.
