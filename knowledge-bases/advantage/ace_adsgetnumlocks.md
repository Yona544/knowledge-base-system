AdsGetNumLocks




Advantage Database Server 12  

AdsGetNumLocks

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetNumLocks  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetNumLocks Advantage Client Engine ace\_Adsgetnumlocks Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetNumLocks  Advantage Client Engine |  |  |  |  |

Retrieves the total number of records locked by the current user on the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetNumLocks (ADSHANDLE hTable,  UNSIGNED16 \*pusNum); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pusNum (O) | Return number of locks. |

Remarks

AdsGetNumLocks returns zero in pulNum if the table is file locked. The number of locks returned includes implicit locks. The number does not include locks held by other users or other applications.

Example

[Click Here](ace_examples.htm#adsgetnumlocksexample)

See Also

[AdsGetAllLocks](ace_adsgetalllocks.htm)

[AdsLockRecord](ace_adslockrecord.htm)

[AdsUnlockRecord](ace_adsunlockrecord.htm)

[AdsIsRecordLocked](ace_adsisrecordlocked.htm)

[AdsLockTable](ace_adslocktable.htm)