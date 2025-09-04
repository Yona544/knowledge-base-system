---
title: Master Replication And Deleted Records
slug: master_replication_and_deleted_records
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_replication_and_deleted_records.htm
source: Advantage CHM
tags:
  - master
checksum: 3d6fcbe719be98f6067459aa8a8bfdebb9b1fc9f
---

# Master Replication And Deleted Records

Replication and Deleted Records

Replication and Deleted Records

Advantage Concepts

| Replication and Deleted Records  Advantage Concepts |  |  |  |  |

It is possible for the physical order of records to be different in source and target ADT tables. This is primarily due to the record recycling algorithm. For example, if you append records in a transaction at the source and then roll back the transaction, the records will be recycled. Because the transaction was rolled back, none of the equivalent activity will occur at the target, thus it will not have the same recycled records. The next appended record will likely have a different physical record number at the source and target.

If you delete a DBF record, the SQL DELETE statement will be sent to the target to delete the same record there. If you recall (undelete) a DBF record, an UPDATE WITH RECALL statement will be sent to the target to recall the same record.  In this way replication will maintain the deleted status of DBF records as long as all updates to each table are replicated.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.md)
