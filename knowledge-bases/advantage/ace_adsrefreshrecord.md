AdsRefreshRecord




Advantage Database Server 12  

AdsRefreshRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsRefreshRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsRefreshRecord Advantage Client Engine ace\_Adsrefreshrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsRefreshRecord  Advantage Client Engine |  |  |  |  |

Rereads the current record and invalidates the client's read-ahead record cache.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsRefreshRecord (ADSHANDLE hTable) |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |

Remarks

AdsRefreshRecord will force all records that are currently stored in the client's read-ahead record cache to be purged. This function is useful if it is likely that another user has updated the current record stored in the read-ahead cache, and you wish your application to see the new data that was updated in this record. When it is not possible for another user to have updated the current record (because the record is locked, the table is locked, or the table is opened exclusively), AdsRefreshRecord will do nothing. If the record to be refreshed has been modified by the user calling the AdsRefreshRecord API but has not yet been flushed to the server, AdsRefreshRecord will fail and return the error AE\_PENDING\_UPDATE. To cancel the pending update, use [AdsCancelUpdate](ace_adscancelupdate.htm).

Example

[Click Here](ace_examples.htm#adsrefreshrecordexample)

See Also

[AdsCancelUpdate](ace_adscancelupdate.htm)

[AdsLockRecord](ace_adslockrecord.htm)