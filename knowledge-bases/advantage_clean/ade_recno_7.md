---
title: Ade Recno 7
slug: ade_recno_7
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_recno_7.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 047c1e06f403099b7233ac2e50e444f6977036f1
---

# Ade Recno 7

RecNo

TAdsTable.RecNo

Advantage TDataSet Descendant

| TAdsTable.RecNo  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Indicates the current record in the dataset.

Syntax

property RecNo: Longint;

Description

Examine RecNo to determine the record number of the current record in the dataset. Applications might use this property with RecordCount to iterate through all the records in a dataset, though typically record iteration is handled with calls to First, Last, MoveBy, Next, and Prior.

Note By default RecNo will not return the sequential (logical) record number if an index or filter is set. This can be turned on using the [Sequenced](ade_sequenced.md) property.

 

Note Records deleted inside of a transaction that has not yet been committed will still be included in a record count.

See Also

[SequencedLevel](ade_sequencedlevel.md)
