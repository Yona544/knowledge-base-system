---
title: Ade Adsunlockrecord
slug: ade_adsunlockrecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsunlockrecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: abd52acd6c7370525b7a0115f8dd831638e13e63
---

# Ade Adsunlockrecord

AdsUnlockRecord

TAdsTable.AdsUnlockRecord

Advantage TDataSet Descendant

| TAdsTable.AdsUnlockRecord  Advantage TDataSet Descendant |  |  |  |  |

Unlocks the given record.

Syntax

function AdsUnlockRecord( ulRecNum : Longint ) : Boolean;

Parameter

| ulRecNum | Record number to unlock. If 0 (zero), then unlock the current record. |

Description

AdsUnlockRecord releases the servers lock on the record and flushes any changes in the record to disk. Return value is for success.

Note Unlocking records while in a transaction is illegal.

Example

bSuccess := AdsTable1.AdsLockRecord( 25 );

bSuccess := AdsTable1.AdsLockRecord( 26 );

 

{. . .your code here. . .}

 

if ( AdsTable1.AdsIsRecordLocked( 25 )) AND (AdsTable1.AdsIsRecordLocked( 26 )) then

begin

AdsTable1.AdsUnlockRecord( 25 );

AdsTable1.AdsUnlockRecord( 26 );

end;

See Also

[AdsGetAllLocks](ade_adsgetalllocks.md)

[AdsIsRecordLocked](ade_adsisrecordlocked.md)

[AdsLockRecord](ade_adslockrecord.md)

[AdsLockTable](ade_adslocktable.md)

[AdsUnlockTable](ade_adsunlocktable.md)
