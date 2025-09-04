---
title: Ade Adschartype
slug: ade_adschartype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adschartype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 176f71c52052004448ce12237368a7fc53bb39ed
---

# Ade Adschartype

AdsCharType

AdsTableOptions.AdsCharType

Advantage TDataSet Descendant

| AdsTableOptions.AdsCharType  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.md)

Indicates the character set used to store the data within the table.

Syntax

type TAdsCharTypes = ( ANSI, OEM );

 

property AdsTableOptions.AdsCharType;

Description

Type of character set used to store data in the table. Options are ANSI and OEM. For compatibility with DOS-based CA-Clipper applications, OEM should be specified. The OEM setting has no effect on Advantage proprietary ADT tables, which always use the ANSI setting.

In addition to the ANSI and OEM values, this can also be set to one of the [dynamic collation](master_collation_support.md) languages such as GENERAL\_VFP\_CI\_AS\_1252.
