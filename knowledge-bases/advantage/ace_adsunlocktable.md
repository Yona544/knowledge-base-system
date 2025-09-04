AdsUnlockTable




Advantage Database Server 12  

AdsUnlockTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsUnlockTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsUnlockTable Advantage Client Engine ace\_Adsunlocktable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsUnlockTable  Advantage Client Engine |  |  |  |  |

Releases all locks on the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsUnlockTable (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table. If a table lock is held, it is released. Otherwise, all record locks are released. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_TABLE\_NOT\_LOCKED | The table was not locked, so it could not be unlocked. |
| AE\_TABLE\_NOT\_SHARED | An unlock was attempted on a table opened exclusively. |

Remarks

AdsUnlockTable releases either all record locks on the table, or a table lock if one exists. If record locks are held and the table is in a transaction, the record locks will be released at the end of the transaction.

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.htm) for more details.

Note Releasing file locks while in a transaction is illegal.

Example

[Click Here](ace_examples.htm#adsunlocktableexample)

See Also

[AdsLockTable](ace_adslocktable.htm)

[AdsIsTableLocked](ace_adsistablelocked.htm)

[AdsLockRecord](ace_adslockrecord.htm)

[AdsGetAllLocks](ace_adsgetalllocks.htm)

[AdsUnlockRecord](ace_adsunlockrecord.htm)