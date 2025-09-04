---
title: Ade Append
slug: ade_append
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_append.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6b90bfb5ec879feb66d4502455acd28d2ada1a02
---

# Ade Append

Append

TAdsTable.Append

Advantage TDataSet Descendant

| TAdsTable.Append  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Adds a new, empty record to the dataset.

Syntax

procedure Append;

Description

Call Append to:

| 1. | Open a new, empty record in the dataset. |

| 2. | Set the current record to the new record. |

After a call to Append, an application can enable users to enter data in the fields of the record, and can then post those changes to the table using Post (or ApplyUpdates if cached updating is enabled). A newly appended record is posted to the table in one of three ways:

- For indexed tables, the record is inserted into the dataset in a position based on its index.

- For non-indexed DBF tables, the record is added to the end of the dataset.

- For non-indexed ADT tables, the record is either added to the end of the dataset or inserted into the position of a record that was previously deleted.
