---
title: Error 7053 Varchar Fields Are Not Supported With This Operation
slug: error_7053_varchar_fields_are_not_supported_with_this_operation
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7053_varchar_fields_are_not_supported_with_this_operation.htm
source: Advantage CHM
tags:
  - error
checksum: aef5d7870f93f74a91c41b6bd9ccaeda7f3343e4
---

# Error 7053 Varchar Fields Are Not Supported With This Operation

7053 VarChar fields are not supported with this operation

7053 VarChar fields are not supported with this operation

Advantage Error Guide

| 7053 VarChar fields are not supported with this operation  Advantage Error Guide |  |  |  |  |

Problem: A Copy To, Append From, Copy Table, Copy Table Contents, or Memo Pack operation was attempted but the table contained at least one VarChar field (a.k.a. weakly-typed VariField). The Copy To, Append From, Copy Table, Copy Table Contents, and Memo Pack operations cannot handle VarChar fields.

Solution: Specify tables that do not contain VarChar fields before attempting the Copy To, Append From, Copy Table, Copy Table Contents, or Memo Pack operations. This error will result if a pack operation is performed on an encrypted table. To perform the pack operation, first decrypt the table. Once finished, the table may be encrypted again.
