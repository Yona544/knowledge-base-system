---
title: Ade Adsgetnumlocks
slug: ade_adsgetnumlocks
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsgetnumlocks.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 726e055d31da85bb8e07e4c0b2f71dcc10a89bc6
---

# Ade Adsgetnumlocks

AdsGetNumLocks

TAdsTable.AdsGetNumLocks

Advantage TDataSet Descendant

| TAdsTable.AdsGetNumLocks  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the total number of records locked by the current user on the given table.

Syntax

function AdsGetNumLocks : Longint;

Description

AdsGetNumLocks returns 0 (zero) if the table is file locked. The number of locks returned includes implicit locks. The number does not include locks held by other users or other applications.

Example

AdsTable1.Edit;

lLockCount := AdsTable1.AdsGetNumLocks;

{ lLockCount equals 1 because any record in Edit state is locked }

See Also

[AdsGetAllLocks](ade_adsgetalllocks.md)

[AdsIsRecordLocked](ade_adsisrecordlocked.md)

[AdsLockRecord](ade_adslockrecord.md)

[AdsLockTable](ade_adslocktable.md)

[AdsUnlockRecord](ade_adsunlockrecord.md)
