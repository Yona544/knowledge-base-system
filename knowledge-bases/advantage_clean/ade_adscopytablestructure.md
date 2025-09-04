---
title: Ade Adscopytablestructure
slug: ade_adscopytablestructure
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscopytablestructure.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ea521b3b9ceccef9b3fc5e6aa09b79d18b22284e
---

# Ade Adscopytablestructure

AdsCopyTableStructure

TAdsTable/TAdsQuery.AdsCopyTableStructure

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsCopyTableStructure  Advantage TDataSet Descendant |  |  |  |  |

Creates a new table with the same structure as the given dataset.

Syntax

procedure AdsCopyTableStructure( strFileName : String );

Parameter

| strFileName | File to create with the current dataset structure. |

Description

The table created does not contain records, but has field structure identical to the original table. Indexes are not copied by AdsCopyTableStructure. The empty table must be opened in a separate table instance.

Example

AdsTable1.TableName := x:\data\employee.adt;

AdsTable1.Active := TRUE;

AdsTable1.AdsCopyTableStructure( x:\data\empty employee file.adt );

See Also

[AdsCopyTable](ade_adscopytable.md)

[AdsCopyTableContents](ade_adscopytablecontents.md)

[AdsConvertTable](ade_adsconverttable.md)
