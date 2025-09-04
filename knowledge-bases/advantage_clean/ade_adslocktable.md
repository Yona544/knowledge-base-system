---
title: Ade Adslocktable
slug: ade_adslocktable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adslocktable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 4250b08e85373aa45e564170802295c980be3f3a
---

# Ade Adslocktable

AdsLockTable

TAdsTable.AdsLockTable

Advantage TDataSet Descendant

| TAdsTable.AdsLockTable  Advantage TDataSet Descendant |  |  |  |  |

Attempts to lock the given table.

Syntax

function AdsLockTable : Boolean;

Description

A successful call to AdsLockTable prevents other applications from being able to update the table. It is a good idea to lock tables prior to creating indexes. Any record locks that have been obtained prior to calling AdsLockTable will be released. Note that if the Advantage Client Engine fails to lock the table (e.g., if another user has record locks), the Advantage Client Engine does not attempt to relock the records that it released.

Example

bSuccess := AdsTable1.AdsLockTable;

 

{. . .your code here. . .}

 

bIsLocked := AdsTable1.AdsIsTableLocked;

See Also

[AdsIsTableLocked](ade_adsistablelocked.md)

[AdsLockRecord](ade_adslockrecord.md)

[AdsUnlockTable](ade_adsunlocktable.md)
