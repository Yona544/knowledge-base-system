AdsLockRecord




Advantage Database Server 12  

TAdsTable.AdsLockRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsLockRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsLockRecord Advantage TDataSet Descendant ade\_Adslockrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsLockRecord  Advantage TDataSet Descendant |  |  |  |  |

Attempts to lock the given record.

Syntax

function AdsLockRecord( ulRecNum : Longint ) : Boolean;

Parameter

|  |  |
| --- | --- |
| ulRecNum | Record to be locked. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: Edit. See your Delphi documentation for more information about this native Delphi method.

Example

AdsTable1.FindKey( [Smith] );

AdsTable1.Edit;

AdsTable1.FieldByName( LastName ).AsString := Smith;

AdsTable1.Post;

Description

A record lock allows a user to update a shared file. If the table is already file locked or opened exclusively, this function returns success. If a record lock is successful, the record is reread. If 0 (zero) is sent from ulRecNum, the current record is locked. If the record number sent to this function is the number of records in the table + 1, no other users will be able to append records to the table.

Note This function does not perform multiple attempts to lock the record if the lock fails.

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

[AdsLockTable](ade_adslocktable.htm)

[AdsUnlockRecord](ade_adsunlockrecord.htm)