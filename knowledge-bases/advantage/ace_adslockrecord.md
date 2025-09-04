AdsLockRecord




Advantage Database Server 12  

AdsLockRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsLockRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsLockRecord Advantage Client Engine ace\_Adslockrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsLockRecord  Advantage Client Engine |  |  |  |  |

Attempts to lock the given record

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsLockRecord (ADSHANDLE hTable,  UNSIGNED32 ulRec); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| ulRec (I) | Record number to lock. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_LOCK\_FAILED | The attempted lock failed. The lock may be held by another user. |
| AE\_TABLE\_NOT\_SHARED | A lock was attempted on a table opened exclusively. |

Remarks

A record lock allows a user to update a shared file. If the table is already file locked or opened exclusively, this function returns AE\_SUCCESS. If a record lock is successful, the record is reread. If zero is sent from ulRec, the current record is locked. If the record number sent to this function is the number of records in the table + 1, no other users will be able to append records to the table.

Note AdsLockRecord does not perform multiple attempts to lock the record if the lock fails.

Example

[Click Here](ace_examples.htm#adslockrecordexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsLockTable](ace_adslocktable.htm)

[AdsUnlockRecord](ace_adsunlockrecord.htm)

[AdsIsRecordLocked](ace_adsisrecordlocked.htm)

[AdsGetAllLocks](ace_adsgetalllocks.htm)