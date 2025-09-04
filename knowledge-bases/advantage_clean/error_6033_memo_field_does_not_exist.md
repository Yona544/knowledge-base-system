---
title: Error 6033 Memo Field Does Not Exist
slug: error_6033_memo_field_does_not_exist
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6033_memo_field_does_not_exist.htm
source: Advantage CHM
tags:
  - error
checksum: f895c2fd0b164ab894909167b64c0c3f4712bc5c
---

# Error 6033 Memo Field Does Not Exist

6033 Memo field does not exist

6033 Memo field does not exist

Advantage Error Guide

| 6033 Memo field does not exist  Advantage Error Guide |  |  |  |  |

Problem: A memo field name specified in an operation does not exist. Currently, functions that specify a memo field name are AX\_BLOB2File() and AX\_File2BLOB().

Solution: Make sure the specified memo field exists in the table that is being used before attempting an operation requiring that memo field.
