---
title: Ade Indexfiles
slug: ade_indexfiles
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_indexfiles.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 31390d804411c8ad603652f874bc7ffb78011fc9
---

# Ade Indexfiles

IndexFiles

TAdsTable.IndexFiles

Advantage TDataSet Descendant

| TAdsTable.IndexFiles  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.md)

Specifies one or more ADI, CDX, IDX, or NTX index, depending on table type, to be opened with the table.

Syntax

property IndexFiles: TStringList;

Description

Use IndexFiles to specify index files to make available for the table. An index file can contain multiple index orders. Each index order in an index file becomes available as a selection for the IndexName property which specifies the actual index to use at any given time.

When index files are added to the list of available indexes, the table component opens them. Insertions and modifications made to the table are maintained in the index files. When files are removed from the list, the table component closes them and they are no longer maintained.

Note At design time, use the Object Inspector to add or remove index file names for the IndexFiles property. At runtime you can add index file names to the property through the Add method of the TStringList, or delete index file names through the Delete method of the TStringList.
