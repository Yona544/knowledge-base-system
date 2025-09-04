---
title: Error 7038 Invalid Record Number
slug: error_7038_invalid_record_number
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7038_invalid_record_number.htm
source: Advantage CHM
tags:
  - error
checksum: d7bd990d6b0a39b337174d20994bb934fcee0c43
---

# Error 7038 Invalid Record Number

7038 Invalid record number

7038 Invalid record number

Advantage Error Guide

| 7038 Invalid record number  Advantage Error Guide |  |  |  |  |

Problem: Attempted to read a record and the record number is greater than the number of records in the file. This error often results from using an index that contains more keys than the table has records. This can occur if a Pack or Zap is performed on the table when the index file(s) was closed.

Solution: Reposition to a valid record number. Reindex the index(es) that contain more keys than the table has records.
