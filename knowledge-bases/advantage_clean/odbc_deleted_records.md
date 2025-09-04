---
title: Odbc Deleted Records
slug: odbc_deleted_records
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: odbc_deleted_records.htm
source: Advantage CHM
tags:
  - odbc
checksum: 61577e47f21b0e2b71e63537f788218d5b719a8b
---

# Odbc Deleted Records

Deleted Records

Deleted Records

Advantage ODBC Driver

| Deleted Records  Advantage ODBC Driver |  |  |  |  |

When a record is deleted in a DBF table, it is not removed from the file, it is simply marked as deleted. These records marked for deletion can be viewed by client applications if the Show Deleted Rows checkbox is marked in the setup utility. Deleted rows can be recovered by a DBF utility or removed from the table by using [sp\_PackTable](master_sp_packtable.md).

When dealing with Advantage-proprietary ADT tables, deleted records are not visible to applications. The Show Deleted Rows checkbox has no effect when using Advantage-proprietary ADT tables, since deleted records are never visible. sp\_PackTable can be used, however, to remove deleted records from a table.
