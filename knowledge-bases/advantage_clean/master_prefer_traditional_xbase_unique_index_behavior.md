---
title: Master Prefer Traditional Xbase Unique Index Behavior
slug: master_prefer_traditional_xbase_unique_index_behavior
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_prefer_traditional_xbase_unique_index_behavior.htm
source: Advantage CHM
tags:
  - master
checksum: 6a8aa984dae5a340147cb607b7f59de5b7374636
---

# Master Prefer Traditional Xbase Unique Index Behavior

Prefer Traditional Xbase Unique Index Behavior

Prefer Traditional Xbase Unique Index Behavior

Advantage Concepts

| Prefer Traditional Xbase Unique Index Behavior  Advantage Concepts |  |  |  |  |

An Xbase index order created with the "unique" property will only include records that are referenced by unique values. If two records result in the identical key) value, then only one of the records will be referenced by the index. The second is simply never added, and no error is reported. If the record (of the two with identical key values) referenced by the unique index is modified such that the key value changes, that index key will be removed from the index, but the other record with the identical key value will NOT be added to the unique index. Therefore, no key will be referencing the unique record in the index. Unique Xbase index orders do not guarantee uniqueness of the field(s) in the index orders key expression.

Unique indexes in the Advantage proprietary file format guarantee uniqueness of the field(s) in the index orders key expression. If the value(s) in the field(s) in an Advantage Proprietary unique index order change such that they are no longer unique, the update will fail.

If you do not want to guarantee uniqueness of field(s) in a table, and if the traditional Xbase behavior of the "unique" property in Xbase indexes is desirable to you, then you may want to use the Xbase file format.
