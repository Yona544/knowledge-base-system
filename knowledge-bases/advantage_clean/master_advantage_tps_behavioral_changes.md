---
title: Master Advantage Tps Behavioral Changes
slug: master_advantage_tps_behavioral_changes
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_advantage_tps_behavioral_changes.htm
source: Advantage CHM
tags:
  - master
checksum: f85b8c16a24b7db0db4d974d4e13a9969323f7f2
---

# Master Advantage Tps Behavioral Changes

Advantage TPS Behavioral Changes

Advantage TPS Behavioral Changes

Advantage Concepts

| Advantage TPS Behavioral Changes  Advantage Concepts |  |  |  |  |

File Closes

During a transaction, it is legal to close tables. If the table, memo file, and index files associated with the table were never modified, the files will be closed. If they were modified in any way, then the files will be cached closed. Cache closed means the file will not actually be closed until the transaction is committed or rolled back.

Some file close functionality is illegal when performed within a transaction, however. The illegal close functionality is: closing all tables, closing an index files, and closing all index files. If these close functions are used, a 5063, "The command is illegal within a transaction" error is generated.

Positioning to an Appended/Inserted Record

If you position directly to a record that is being appended/inserted by another application during a transaction using a "go to" or "go to bookmark" operation, the user will be positioned to one record past the end of file and the EOF flag will be set to True. This behavior exists because records appended/inserted during another transaction are "invisible" to all other users until that transaction is committed.

Explicit Unlocks

Explicit record and file unlocks are illegal during a transaction. Advantage must maintain all locks until the transaction has completed. Unlocks are not allowed during a transaction because corresponding updates to those records/files could not be made during the commit of a transaction if the lock(s) did not exist.
