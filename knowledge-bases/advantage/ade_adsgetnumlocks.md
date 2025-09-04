AdsGetNumLocks




Advantage Database Server 12  

TAdsTable.AdsGetNumLocks

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetNumLocks  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetNumLocks Advantage TDataSet Descendant ade\_Adsgetnumlocks Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
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

[AdsGetAllLocks](ade_adsgetalllocks.htm)

[AdsIsRecordLocked](ade_adsisrecordlocked.htm)

[AdsLockRecord](ade_adslockrecord.htm)

[AdsLockTable](ade_adslocktable.htm)

[AdsUnlockRecord](ade_adsunlockrecord.htm)