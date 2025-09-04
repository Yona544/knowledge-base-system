AdsRefreshRecord




Advantage Database Server 12  

TAdsTable.AdsRefreshRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsRefreshRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsRefreshRecord Advantage TDataSet Descendant ade\_Adsrefreshrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsRefreshRecord  Advantage TDataSet Descendant |  |  |  |  |

Rereads the current record.

Syntax

procedure AdsRefreshRecord;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: Refresh. See your Delphi documentation for more information about this native Delphi method.

Description

Rereads the record from the server. This function should be used if it is likely that another concurrent user has updated the record this user is currently positioned on. When it is not possible for another user to update the record (the record is locked, the table is locked, or the table is opened exclusively) this function will do nothing. To cancel an update, use AdsCancelUpdate.

Example

AdsTable1.Refresh;

See Also

[AdsLockRecord](ade_adslockrecord.htm)