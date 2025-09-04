AdsGetAllLocks




Advantage Database Server 12  

TAdsTable.AdsGetAllLocks

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetAllLocks  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetAllLocks Advantage TDataSet Descendant ade\_Adsgetalllocks Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetAllLocks  Advantage TDataSet Descendant |  |  |  |  |

Returns an array of records locked by the current user for the given table.

Syntax

function AdsGetAllLocks( aulLocks : Array of Longint ) : Word;

Parameter

|  |  |
| --- | --- |
| aulLocks | Return record locks in the given array. |

Description

After a successful call to AdsGetAllLocks, the return value will contain the record numbers of all records locked for the given Table. It does not include record locks by other applications or from separate table handles to the same table in the same application. The locks returned will include both implicit and explicit locks.

Example

var

IntegerArray : array[0..10] of integer;

 

begin

AdsTable1.Edit;

lLockCount := AdsTable1.AdsGetNumLocks;

{ lLockCount equals 1 because any record in Edit state is locked }

 

lLockCount := AdsTable1.AdsGetAllLocks( IntegerArray );

{ lLockcount equals 1 and IntegerArray[0] equals record 27 }

end;

See Also

[AdsGetNumLocks](ade_adsgetnumlocks.htm)

[AdsIsRecordLocked](ade_adsisrecordlocked.htm)

[AdsLockRecord](ade_adslockrecord.htm)