AdsIsTableLocked




Advantage Database Server 12  

TAdsTable.AdsIsTableLocked

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsIsTableLocked  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsIsTableLocked Advantage TDataSet Descendant ade\_Adsistablelocked Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
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

[AdsLockRecord](ade_adslockrecord.htm)

[AdsLockTable](ade_adslocktable.htm)

[AdsUnlockTable](ade_adsunlocktable.htm)