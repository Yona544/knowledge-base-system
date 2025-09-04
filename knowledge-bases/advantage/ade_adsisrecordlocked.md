AdsIsRecordLocked




Advantage Database Server 12  

TAdsTable.AdsIsRecordLocked

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsIsRecordLocked  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsIsRecordLocked Advantage TDataSet Descendant ade\_Adsisrecordlocked Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsIsRecordLocked  Advantage TDataSet Descendant |  |  |  |  |

Tests if the given record is locked by the current user.

Syntax

function AdsIsRecordLocked( ulRecNum : Longint ) : Boolean;

Parameter

|  |  |
| --- | --- |
| ulRecNum | Record number to test. If 0 (zero), then test current record. |

Description

AdsIsRecordLocked will return True for records that were explicitly or implicitly locked by the current user for this TAdsTable instance. If the table is locked by the current user, AdsIsRecordLocked will return False. If the record or table is locked by another user or by this user who is using a different TAdsTable instance, AdsIsRecordLocked will return False.

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

[AdsLockRecord](ade_adslockrecord.htm)

[AdsLockTable](ade_adslocktable.htm)

[AdsUnlockRecord](ade_adsunlockrecord.htm)