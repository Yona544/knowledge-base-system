AdsUnlockRecord




Advantage Database Server 12  

TAdsTable.AdsUnlockRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsUnlockRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsUnlockRecord Advantage TDataSet Descendant ade\_Adsunlockrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsUnlockRecord  Advantage TDataSet Descendant |  |  |  |  |

Unlocks the given record.

Syntax

function AdsUnlockRecord( ulRecNum : Longint ) : Boolean;

Parameter

|  |  |
| --- | --- |
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

[AdsGetAllLocks](ade_adsgetalllocks.htm)

[AdsIsRecordLocked](ade_adsisrecordlocked.htm)

[AdsLockRecord](ade_adslockrecord.htm)

[AdsLockTable](ade_adslocktable.htm)

[AdsUnlockTable](ade_adsunlocktable.htm)