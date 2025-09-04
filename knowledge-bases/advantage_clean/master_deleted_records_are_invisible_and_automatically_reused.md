---
title: Master Deleted Records Are Invisible And Automatically Reused
slug: master_deleted_records_are_invisible_and_automatically_reused
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_deleted_records_are_invisible_and_automatically_reused.htm
source: Advantage CHM
tags:
  - master
checksum: 77c83c16fd6c4e6eac5fd400c0fee1637a9ab38f
---

# Master Deleted Records Are Invisible And Automatically Reused

Deleted Records are Invisible and Automatically Reused

Deleted Records are Invisible and Automatically Reused

Advantage Concepts

| Deleted Records are Invisible and Automatically Reused  Advantage Concepts |  |  |  |  |

If a delete record operation is performed on a record in an ADT table, the record is not physically removed from the table. The record is, however, logically removed from the table. Deleted records in an ADT table are not visible to the application. Deleted records cannot be "undeleted" or "recalled". The space used by records deleted from the table are marked for record reuse. That is, a subsequent append or insert operation will use space marked for reuse before using new space at the end of the table for a new record. Thus, the size of an ADT table will not increase after an append or insert operation if there is space marked for reuse in the table.

If you desire the delete record operation to delete records such that they are no longer visible to any application and you do not want space used by deleted records to bloat the size of your tables (as can happen with Xbase tables), you may want to use the [Advantage Proprietary Format](master_advantage_proprietary_format.md).
