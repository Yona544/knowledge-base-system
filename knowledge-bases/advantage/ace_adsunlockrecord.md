AdsUnlockRecord




Advantage Database Server 12  

AdsUnlockRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsUnlockRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsUnlockRecord Advantage Client Engine ace\_Adsunlockrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsUnlockRecord  Advantage Client Engine |  |  |  |  |

Unlocks the given record

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsUnlockRecord (ADSHANDLE hTable,  UNSIGNED32 ulRec); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| ulRec (I) | Record number to unlock. If zero, then unlock the current record. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_RECORD\_NOT\_LOCKED | The indicated record was not locked. |
| AE\_INVALID\_RECORD\_NUMBER | The record number given was not valid. |

Remarks

AdsUnlockRecord releases the servers lock on the record and flushes any changes in the record to disk.

Note Records cannot be unlocked on the server during transactions. Therefore, calls to AdsUnlockRecord during a transaction will cause the Advantage Client Engine to mark the record lock as "unlocked during transaction", and the Advantage Client Engine will release the lock at the end (commit or rollback) of the transaction.

Example

[Click Here](ace_examples.htm#adsunlockrecordexample)

See Also

[AdsLockRecord](ace_adslockrecord.htm)

[AdsIsRecordLocked](ace_adsisrecordlocked.htm)

[AdsLockTable](ace_adslocktable.htm)

[AdsGetAllLocks](ace_adsgetalllocks.htm)

[AdsUnlockTable](ace_adsunlocktable.htm)