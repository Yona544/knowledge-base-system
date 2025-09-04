---
title: Ade Adsisrecordinaof
slug: ade_adsisrecordinaof
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisrecordinaof.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: be7374255664e6a1dabe1b5d5797b07b41d48b3c
---

# Ade Adsisrecordinaof

AdsIsRecordInAOF

TAdsTable.AdsIsRecordInAOF

Advantage TDataSet Descendant

| TAdsTable.AdsIsRecordInAOF  Advantage TDataSet Descendant |  |  |  |  |

Determines if a specific record is in an Advantage Optimized Filter (AOF).

Syntax

function AdsIsRecordInAOF( ulRecordNum: Longint ): Boolean;

Parameter

| ulRecordNumber | Record number to check. If this is 0, then the current record number is checked. |

Description

AdsIsRecordInAOF can be used to determine if an Advantage Optimized Filter (AOF) on the server contains a specific record. If the call is made while using [Advantage Local Server](master_advantage_local_server.md), the value returned by this API does not guarantee that the actual record value matches the AOF's view of that record. This is because another client could have updated the record and those changes would not be reflected in other clients' AOFs. Also, if an AOF is not fully optimized, it is possible for a record to be included in the AOF initially but not to pass the filter. Records that fit this description are dynamically removed from the filter as the records are read. A call to AdsIsRecordInAOF can indicate that a given record is in the AOF, but it is possible for that record to be filtered out when it is read. Therefore, this API is best used with fully optimized AOFs.

Example

chkboxInAOF.Checked := AdsTable1.AdsIsRecordInAOF( 6 );

See Also

[AdsSetAOF](ade_adssetaof.md)

[AdsGetAOFOptLevel](ade_adsgetaofoptlevel.md)

[AdsCustomizeAOF](ade_adscustomizeaof.md)
