---
title: Ade Insert
slug: ade_insert
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_insert.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4e1c019f729304331d12766a4d3be1ed318afe01
---

# Ade Insert

Insert

TAdsTable.Insert

Advantage TDataSet Descendant

| TAdsTable.Insert  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Inserts a new, empty record in the dataset.

Syntax

procedure Insert;

Description

Call Insert to do the following:

- Open a new, empty record in the dataset.

- Set the current record to the new record.

After a call to Insert, an application can enable users to enter data in the fields of the records, and can then post those changes to the table using Post. A newly inserted record is posted to the table in one of three ways:

- For indexed tables, the record is inserted into the dataset in a position based on its index.

- For non-indexed DBF tables, the record is added to the end of the dataset.

- For non-indexed ADT tables, the record is either added to the end of the dataset or inserted into the position of a record that was previously deleted.
