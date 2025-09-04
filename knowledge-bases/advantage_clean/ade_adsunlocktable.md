---
title: Ade Adsunlocktable
slug: ade_adsunlocktable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsunlocktable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 0f545d15b6172e5466c31b51ced9468089769af8
---

# Ade Adsunlocktable

AdsUnlockTable

TAdsTable.AdsUnlockTable

Advantage TDataSet Descendant

| TAdsTable.AdsUnlockTable  Advantage TDataSet Descendant |  |  |  |  |

Releases all locks on the given table.

Syntax

procedure AdsUnlockTable;

Description

AdsUnlockTable releases either all record locks on the table, or a table lock if one exists.

Note Unlocking tables while in a transaction is illegal.

Example

bSuccess := AdsTable1.AdsLockTable;

 

{. . .your code here. . .}

 

bIsLocked := AdsTable1.AdsIsTableLocked;

if ( bIsLocked ) then

AdsTable1.AdsUnlockTable;

See Also

[AdsGetAllLocks](ade_adsgetalllocks.md)

[AdsIsTableLocked](ade_adsistablelocked.md)

[AdsLockRecord](ade_adslockrecord.md)

[AdsLockTable](ade_adslocktable.md)

[AdsUnlockRecord](ade_adsunlockrecord.md)
