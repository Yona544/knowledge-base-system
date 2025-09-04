AdsLockTable




Advantage Database Server 12  

AdsLockTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsLockTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsLockTable Advantage Client Engine ace\_Adslocktable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsLockTable  Advantage Client Engine |  |  |  |  |

Attempts to lock the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsLockTable (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table |

Special Return Codes

|  |  |
| --- | --- |
| AE\_LOCK\_FAILED | The attempted lock failed. The lock may be held by another user. |
| AE\_TABLE\_NOT\_SHARED | A lock was attempted on a table opened exclusively. |

Remarks

A successful call to AdsLockTable prevents other applications from being able to update the table. It is recommended that you lock tables prior to creating indexes. Any record locks that have been obtained prior to calling AdsLockTable will be released. If the Advantage Client Engine fails to lock the table (e.g., if another user has record locks), then the Advantage Client Engine does not attempt to relock the records that it released.

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.htm) for more details.

Example

[Click Here](ace_examples.htm#adslocktableexample)

See Also

[AdsOpenTable](ace_adsopentable.htm)

[AdsIsTableLocked](ace_adsistablelocked.htm)

[AdsLockRecord](ace_adslockrecord.htm)

[AdsUnlockTable](ace_adsunlocktable.htm)