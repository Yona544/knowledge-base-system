AdsIsTableLocked




Advantage Database Server 12  

AdsIsTableLocked

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsTableLocked  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsTableLocked Advantage Client Engine ace\_Adsistablelocked Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsTableLocked  Advantage Client Engine |  |  |  |  |

Tests if the given table is locked by the current user

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsTableLocked (ADSHANDLE hTable,  UNSIGNED16 \*pbLocked); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table. |
| pbLocked (O) | Return True if locked, False if not locked. |

Remarks

AdsIsTableLocked will return True if the table is locked by the current user. If the table is locked by another user or by this user who is using a different table handle, AdsIsTableLocked will return False. If the table is opened exclusively by the current user, this function will return False.

Note AdsIsTableLocked only tests for a lock on the given table handle (hTable). It does not test for table locks acquired on other table handles even though they refer to the same physical file.

Example

[Click Here](ace_examples.htm#adsistablelockedexample)

See Also

[AdsLockTable](ace_adslocktable.htm)

[AdsUnlockTable](ace_adsunlocktable.htm)

[AdsLockRecord](ace_adslockrecord.htm)