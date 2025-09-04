---
title: Master Unpredictable Results With Tps
slug: master_unpredictable_results_with_tps
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_unpredictable_results_with_tps.htm
source: Advantage CHM
tags:
  - master
checksum: 4e10670b717b0277ce5b068d1e8d86557c609589
---

# Master Unpredictable Results With Tps

Unpredictable Results with TPS

Unpredictable Results with TPS

Advantage Concepts

| Unpredictable Results with TPS  Advantage Concepts |  |  |  |  |

Non-Advantage Applications Sharing Common DBF Data

Advantage TPS should only be used when only Advantage applications are accessing the data. This is to ensure that the Advantage Database Server maintains full file access and locking control.

If non-Advantage applications access this shared DBF table data, unpredictable results may occur. The "deleted" byte is used by the Advantage TPS to note the status of DBF table records within a transaction. A varied value could cause non-Advantage applications trouble in determining record deletion status. To avoid this problem, a one-byte character field with the name AXS\_TPS can be added to your tables. If this field exists, the Advantage TPS will use it to track record status rather than the "deleted" byte.

Also, while a record is being updated during a transaction, there can be multiple index keys referencing a single record. If a non-Advantage application is accessing the data, it could use the wrong index key for the record(s) in question or see the index as corrupt. The index is returned to a correct state upon completion of the transaction.

Unique ADI Indexes

During a single transaction, multiple occurrences of an identical key is possible. The repeated key is only visible to the user who added the key. The repeated key is removed when the transaction is committed or rolled back.

For an example of how the identical key is added to unique indexes, assume "Smith" is a unique last name and assume there is a unique index on lastname. If, within a transaction, "Smith" is changed to "Jones", then that index will no longer have any reference to a "Smith". Within the same transaction, the user changes the same record from "Jones" to "Smith". At this point, two "Smith" keys are visible to this user. When the transaction is committed or rolled back, only one key will exist.

Unique Xbase Indexes

Unique Xbase index updates during a transaction may not work perfectly with Advantage TPS when using CDX, IDX, or NTX indexes. However, similar undesirable update behavior can also result without Advantage TPS.

For an example of undesirable update behavior with Xbase unique indexes that exists with and without Advantage TPS, assume "Smith" is a non-unique last name located in record 69. Also, assume "Smith" is a key in a unique index, which references record 69. If "Smith" is changed to "Jones", then that index will no longer have any reference to a "Smith", although the last name "Smith" may still exist in the table.

There is one specific case, however, where an Xbase unique index update with Advantage TPS does not work the same as it does without Advantage TPS. Following the same example above, if during a transaction "Smith" is changed to "Jones" in record 69, then "Anderson" is changed to "Smith" in record 70, there will not be any reference to a "Smith" in the unique index when the transaction has been committed. Without Advantage TPS, the "Smith" (now in record 70) would exist in the Xbase unique index.
