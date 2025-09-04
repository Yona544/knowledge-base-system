---
title: Ade Record Locking Modes Pessimistic Vs Optimistic
slug: ade_record_locking_modes_pessimistic_vs_optimistic_
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_record_locking_modes_pessimistic_vs_optimistic_.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8dcd55b0e4aa98be5357dab7242cc13231643520
---

# Ade Record Locking Modes Pessimistic Vs Optimistic

Record Locking Modes (pessimistic vs. optimistic)

Record Locking Modes (pessimistic vs. optimistic)

Advantage TDataSet Descendant

| Record Locking Modes (pessimistic vs. optimistic)  Advantage TDataSet Descendant |  |  |  |  |

If you are converting an application that previously used a different database, and that database used optimistic locking, you may want to configure your Advantage-enabled application to use optimistic locking as well.

When using pessimistic locking, records in a table will be locked when you put the dataset into edit state. The records will remain locked until you either cancel the update or post your changes.

When using optimistic locking, records in a table will be refreshed when you put the dataset into edit state, but will not be locked. Records will not be locked until you attempt to post your changes. At this point the record in question will be locked and compared to the record retrieved when the dataset was put into edit state. If some other user has modified the record, an error will be returned. If the record has not been modified, the post operation will continue.

Note that often even if your application was written using a database that supported optimistic record locking, you do not need to use optimistic locking with Advantage. Many applications will run as expected even though they are now using pessimistic record locking (which is the default and recommended Advantage record locking mode).

The [AdsTableOptions.AdsRecordLockingMode](ade_adsrecordlockingmode.md) property can be used to specify what record locking mode you would like the dataset to use.
