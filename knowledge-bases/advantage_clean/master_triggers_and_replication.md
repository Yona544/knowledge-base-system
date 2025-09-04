---
title: Master Triggers And Replication
slug: master_triggers_and_replication
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_triggers_and_replication.htm
source: Advantage CHM
tags:
  - master
checksum: f514a0423b8e54b0754f5ba02f5978b7de38585e
---

# Master Triggers And Replication

Triggers and Replication

Triggers and Replication

Advantage Concepts

| Triggers and Replication  Advantage Concepts |  |  |  |  |

When a replication update is performed at the target database, the only trigger type that will be executed is the CONFLICT trigger. The reason for this is because triggers can write different data to the record than is provided in the original update. If the trigger at the target were fired, it would be using different data than was available at the source. Replication will distribute that actual data that is written at the source to the target.

To address replication conflicts, the CONFLICT trigger type is available. When a record update is performed on a replicated table, Advantage computes a CRC of the original record. When the update is transmitted to the target, the target record CRC is also computed (if a CONFLICT trigger is available). The CRC that is computed includes all memo and BLOB data in the record. It does not include the physical record number or the contents of ROWVERSION and MODTIME fields.

If the CRC of the original source record does not match the current target record and a CONFLICT trigger exists, then the CONFLICT trigger will be fired. The developer must choose what actions to perform in the CONFLICT trigger. For example, the trigger could store the information in a separate error log or write the data to the table anyway.

If there is no CONFLICT trigger at the target, then the CRC is not computed at the target and the record update will occur.

Note Conflict detection is not currently possible when using a vertical filter. The CRC is computed on the entire record. If the source and target table structures are not identical, the CRC values will always be different, which means that the conflict trigger will always fire even if the original replicated fields matched at source and target. Therefore, if you are using conflict triggers, it is unlikely that you can use vertical filters unless the table structures are the same and the filtered fields have static values that are the same at source and target.

See Also

[Replication Behind the Scenes](master_how_replication_works_internally.md)

[Trigger Types (BEFORE, INSTEAD OF, AFTER, and CONFLICT)](master_trigger_types_before_instead_of_and_after_.md)
