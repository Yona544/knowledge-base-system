AdsUnlockTable




Advantage Database Server 12  

TAdsTable.AdsUnlockTable

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsUnlockTable  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsUnlockTable Advantage TDataSet Descendant ade\_Adsunlocktable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
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

[AdsGetAllLocks](ade_adsgetalllocks.htm)

[AdsIsTableLocked](ade_adsistablelocked.htm)

[AdsLockRecord](ade_adslockrecord.htm)

[AdsLockTable](ade_adslocktable.htm)

[AdsUnlockRecord](ade_adsunlockrecord.htm)