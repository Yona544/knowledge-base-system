---
title: Master Deleted
slug: master_deleted
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_deleted.htm
source: Advantage CHM
tags:
  - master
checksum: 773f78f2d2e55e945fc373b1cafaa6e460757dac
---

# Master Deleted

DELETED()

DELETED()

Advantage Concepts

| DELETED()  Advantage Concepts |  |  |  |  |

[Scalar](master_supported_scalar_functions.md) function that returns the deleted status of the current record.

| Supported in SQL: | Yes |
| Supported in Navigational: | Yes |

Syntax

DELETED( [<tablealias>] ) à lDeleted

Return Values

DELETED() returns true (.T.) if the current record is marked for deletion; otherwise, it returns false (.F.).

Remarks

DELETED() is a database function that determines if the current record in the table is marked for deletion. Since each table has a current record, each table has its own DELETED() value.

In SQL usage, the DELETED() scalar function accepts an optional table alias that can be used when the table reference is ambiguous (e.g., in the case of a join where multiple tables are involved).

See Also

[sp\_PackTable](master_sp_packtable.md)

[sp\_PackTableOnline](master_sp_packtableonline.md)

Advantage TDataSet Descendant

[AdsDeleteRecord](ade_adsdeleterecord.md)

[AdsPackTable](ade_adspacktable.md)

[AdsRecallRecord](ade_adsrecallrecord.md)

[AdsIsRecordDeleted](ade_adsisrecorddeleted.md)

[TAdsSettings.ShowDeleted](ade_showdeleted.md)

Advantage Client Engine API

[AdsDeleteRecord](ace_adsdeleterecord.md)

[AdsShowDeleted](ace_adsshowdeleted.md)

[AdsPackTable](ace_adspacktable.md)

[AdsRecallRecord](ace_adsrecallallrecords.md)

[AdsIsRecordDeleted](ace_adsisrecorddeleted.md)
