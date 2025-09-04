---
title: Ade Insertrecord
slug: ade_insertrecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_insertrecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: e15a3f9e98282ec00baca66566f9136e49f9c386
---

# Ade Insertrecord

InsertRecord

TAdsTable/TAdsQuery.InsertRecord

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.InsertRecord  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md) [TAdsQuery](ade_tadsquery.md)

Appends a new, populated record to the dataset and posts it to the table.

Syntax

procedure InsertRecord(const Values: array of const);

Description

Call InsertRecord to create a new, empty record in the dataset, populate it with the field values in Values, and post the values to the table.

The newly appended record becomes the current record.

Note Due to the way Xbase works, the Insert is identical to an AppendRecord with DBF tables.
