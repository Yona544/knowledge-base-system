AdsIsRecordLocked




Advantage Database Server 12  

AdsIsRecordLocked

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsRecordLocked  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsRecordLocked Advantage Client Engine ace\_Adsisrecordlocked Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsRecordLocked  Advantage Client Engine |  |  |  |  |

Tests if the given record is locked by the current user

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsRecordLocked (ADSHANDLE hTable,  UNSIGNED32 ulRec,  UNSIGNED16 \*pbLocked); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| ulRec (I) | Record number to test. If 0, then test current record. |
| pbLocked (O) | Return True (1) if locked, False (0) if not locked. |

Remarks

AdsIsRecordLocked will return True for records that were explicitly or implicitly locked by the current user. If the table is locked by the current user, AdsIsRecordLocked will return False. If the record or table is locked by another user or by the user that is using a different table handle, AdsIsRecordLocked will return False.

Note AdsIsRecordLocked only tests for record locks on the given table handle (hTable). It does not test for locks acquired on any other table handles even though they refer to the same physical file. It is very fast because it uses the client-side lock list associated with the table rather than making a server request.

Example

[Click Here](ace_examples.htm#adsisrecordlockedexample)

See Also

[AdsLockRecord](ace_adslockrecord.htm)

[AdsUnlockRecord](ace_adsunlockrecord.htm)

[AdsLockTable](ace_adslocktable.htm)