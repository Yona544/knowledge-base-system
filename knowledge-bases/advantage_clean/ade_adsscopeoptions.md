---
title: Ade Adsscopeoptions
slug: ade_adsscopeoptions
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsscopeoptions.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 84495ecff75e2edff6649ea436022c8a9c22a5de
---

# Ade Adsscopeoptions

AdsScopeOptions

AdsTableOptions.AdsScopeOptions

Advantage TDataSet Descendant

| AdsTableOptions.AdsScopeOptions  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.md)

When determining the record count, key count, or key position, indicates whether to respect the scope/range applied to the data set.

Syntax

type TAdsRespectScopes = ( IGNORE\_SCOPES\_WHEN\_COUNTING,

RESPECT\_SCOPES\_WHEN\_COUNTING );

 

property AdsTableOptions.AdsScopeOptions;

Description

This setting specifies whether scopes/ranges are respected or ignored when using the following methods: [AdsGetKeyCount](ade_adsgetkeycount.md), [AdsGetKeyNum](ade_adsgetkeynum.md), and [AdsGetRecordCount](ade_adsgetrecordcount.md). Unlike the AdsFilterOptions property, the performance of methods affected by this setting is similar no matter which scope setting is specified.
