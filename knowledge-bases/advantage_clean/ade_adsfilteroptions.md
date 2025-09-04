---
title: Ade Adsfilteroptions
slug: ade_adsfilteroptions
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsfilteroptions.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 522c4f4790f2688d79c1c536ab53c5020155b9e3
---

# Ade Adsfilteroptions

AdsFilterOptions

AdsTableOptions.AdsFilterOptions

Advantage TDataSet Descendant

| AdsTableOptions.AdsFilterOptions  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.md)

When determining the record count, indicates whether to respect the filtering applied to the dataset. Filtering consists of all applicable filters, ranges, and scopes.

Syntax

type TAdsRespectFilters = ( IGNORE\_WHEN\_COUNTING, RESPECT\_WHEN\_COUNTING );

 

property AdsTableOptions.AdsFilterOptions;

Description

This setting affects whether filters, ranges, and scopes are respected or ignored using the following methods: [AdsGetKeyCount](ade_adsgetkeycount.md), [AdsGetKeyNum](ade_adsgetkeynum.md), [AdsGetRecordCount](ade_adsgetrecordcount.md), and [AdsGetRecordNum](ade_adsgetrecordnum.md). In addition, this setting affects whether filters are respected or ignored using the following methods: [AdsCopyTable](ade_adscopytable.md), [AdsCopyTableContents](ade_adscopytablecontents.md).

When using RESPECT\_WHEN\_COUNTING, this function will skip through every or many records in a table and could be extremely slow depending on how many records pass the filter, range, and scope. It is not recommended to use this function except on very small tables.

When using IGNORE\_WHEN\_COUNTING with [AdsCopyTable](ade_adscopytable.md), [AdsCopyTableContents](ade_adscopytablecontents.md), [AdsGetRecordCount](ade_adsgetrecordcount.md), and [AdsGetRecordNum](ade_adsgetrecordnum.md), the operations will occur much faster than if using RESPECT\_WHEN\_COUNTING. When using IGNORE\_WHEN\_COUNTING with [AdsGetKeyCount](ade_adsgetkeycount.md) and [AdsGetKeyNum](ade_adsgetkeynum.md), these operations may still be quite slow with large indexes because every or many keys in the index are literally counted.
