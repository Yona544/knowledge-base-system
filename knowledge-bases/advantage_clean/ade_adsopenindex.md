---
title: Ade Adsopenindex
slug: ade_adsopenindex
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsopenindex.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0ae51035cb6cc2441ef009fc71ae992f3634285d
---

# Ade Adsopenindex

AdsOpenIndex

TAdsTable.AdsOpenIndex

Advantage TDataSet Descendant

| TAdsTable.AdsOpenIndex  Advantage TDataSet Descendant |  |  |  |  |

Opens an index file and associates all index orders in it with the given table.

Syntax

procedure AdsOpenIndex( strIndexName : String );

Parameter

| strIndexName | Filename of index to open. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.md) for more information. The suggested native Delphi method to use instead is: OpenIndexFile. See your Delphi documentation for more information about this native Delphi method.

Description

AdsOpenIndex opens all handles of index orders in the index file. If the index file is NOT a compound index (CDX or ADI), it will have only one index order. If the index file is a compound CDX or ADI index, multiple index orders may be opened.

Example

AdsTable1.OpenIndexFile( x:\path\file.ext );

AdsTable1.CloseIndexFile( file );

See Also

[AdsCreateIndex](ade_adscreateindex.md)

[AdsGetAllIndexes](ade_adsgetallindexes.md)

[AdsGetIndexHandle](ade_adsgetindexhandle.md)
