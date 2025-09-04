---
title: Master Xbase Deleted Records
slug: master_xbase_deleted_records
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_xbase_deleted_records.htm
source: Advantage CHM
tags:
  - master
checksum: 206a541f93f471400171bd66219c1d10b49ae16d
---

# Master Xbase Deleted Records

Xbase Deleted Records

Xbase Deleted Records

Advantage Concepts

| Xbase Deleted Records  Advantage Concepts |  |  |  |  |

If a delete record operation is performed on a record in a DBF table, the record is not physically removed from the table. Nor is the record logically removed from the table. Depending on the "show deleted records" setting, it may still be possible to view the record. The record is instead "marked for deletion". Optionally, records marked for deletion can still be visible to the application. Records marked for deletion can also be "un-deleted", or "recalled" as it is referred to in Xbase terminology. Thus, the deletion status of a record is nothing more than a filter. If an application is written to allow records marked for deletion to be visible (which is the default), then the record deletion status is irrelevant. If an application is written to ignore records that are marked for deletion, then those records marked for deletion have effectively been filtered from visibility. If the Pack operation is performed on a table, then and only then will records marked for deletion be physically removed from the table.
