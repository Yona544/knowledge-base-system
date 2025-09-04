AdsLockTable




Advantage Database Server 12  

TAdsTable.AdsLockTable

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsLockTable  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsLockTable Advantage TDataSet Descendant ade\_Adslocktable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
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

[AdsIsTableLocked](ade_adsistablelocked.htm)

[AdsLockRecord](ade_adslockrecord.htm)

[AdsUnlockTable](ade_adsunlocktable.htm)