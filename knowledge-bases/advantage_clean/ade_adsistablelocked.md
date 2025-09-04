---
title: Ade Adsistablelocked
slug: ade_adsistablelocked
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsistablelocked.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: ec43da26495c0217e13feb5a6b7e114135d28df8
---

# Ade Adsistablelocked

AdsIsTableLocked

TAdsTable.AdsIsTableLocked

Advantage TDataSet Descendant

| TAdsTable.AdsIsTableLocked  Advantage TDataSet Descendant |  |  |  |  |

Tests if the given table is locked by the current user.

Syntax

function AdsIsTableLocked : Boolean;

Description

AdsIsTableLocked will return True if the table is locked by the current user for this TAdsTable instance. If the table is locked by another user or by this user who is using a different TAdsTable instance, AdsIsTableLocked will return False. If the table is opened exclusively by the current user, this function will return False.

Example

bSuccess := AdsTable1.AdsLockTable;

 

{. . .your code here. . .}

 

bIsLocked := AdsTable1.AdsIsTableLocked;

if ( bIsLocked ) then

AdsTable1.AdsUnlockTable;

See Also

[AdsLockRecord](ade_adslockrecord.md)

[AdsLockTable](ade_adslocktable.md)

[AdsUnlockTable](ade_adsunlocktable.md)
