---
title: Ade Adsgetkeynum
slug: ade_adsgetkeynum
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetkeynum.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 13ef10829c51e2ad246d71511d92eb6cc3480c7c
---

# Ade Adsgetkeynum

AdsGetKeyNum

TAdsTable/TAdsQuery.AdsGetKeyNum

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsGetKeyNum  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the logical key number of the current record with respect to the active index.

Syntax

function AdsGetKeyNum : Longint;

Description

The first record in the index is logical record 1.

If AdsTableOptions.AdsFilterOptions is IGNORE\_WHEN\_COUNTING and AdsTableOptions.AdsScopeOptions is either RESPECT\_SCOPES\_WHEN COUNTING or IGNORE\_SCOPES\_WHEN\_COUNTING, this function should return fairly quickly and provide good performance if the active index is not large. If the active index is large, this function could take some time to complete because index keys are literally counted until the current key is reached.

If AdsTableOptions.AdsFilterOptions is RESPECT\_WHEN\_COUNTING, all records referenced by keys in the index that pass the filter and/or scope/range are skipped through and counted until the current key is reached. Thus, with large indexes where many records pass the filter and/or keys pass the scope/range, this function can be very slow.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', '', '', [] );

AdsTable1.IndexName := 'Tag1';

 

AdsTable1.FindNearest( ['C'] );

lKeyCount := AdsTable1.AdsGetKeyNum;

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.md)
