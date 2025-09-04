AdsFreshRecordCount




Advantage Database Server 12  

AdsTableOptions.AdsFreshRecordCount

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsFreshRecordCount  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsFreshRecordCount Advantage TDataSet Descendant ade\_Adsfreshrecordcount Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsFreshRecordCount  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Specifies if [RecordCount](ade_recordcount.htm) and the Advantage extended method [AdsGetRecordCount](ade_adsgetrecordcount.htm) are to read the table header for an up-to-date record count each time they are called.

Syntax

property AdsTableOptions.AdsFreshRecordCount;

Description

[RecordCount](ade_recordcount.htm) and the Advantage extended method [AdsGetRecordCount](ade_adsgetrecordcount.htm) will not always contact the Advantage Database Server to read the table header and return the up-to-date record count. For performance reasons, the record count stored in client cache is often returned, which in a multi-user environment may not be up-to-date. To guarantee that an up-to-date record count is retrieved from the Advantage Database Server, set the AdsFreshRecordCount property to True. Note that if other applications are appending records to a table, even if AdsFreshRecordCount is set to True, there is no guarantee that the record count will be accurate because it is possible for another application to append a record immediately after the record count is retrieved. To guarantee an accurate count, an application must either lock the table or open it exclusively.

Note For the best performance, False is the default and suggested value for the AdsFreshRecordCount property. Only set AdsFreshRecordCount to True if you, or a data-aware component, always require and up-to-date record count. If an up-to-date record count is only needed in a particular instance, and not throughout your application, make a direct call to the Advantage Client Engine API AdsGetRecordCount. By calling the Advantage Client Engine API AdsGetRecordCount you can force one call in your application to retrieve a fresh record count, while the value of AdsFreshRecordCount is left at False, and all other record count calls in your application utilize the RecordCount property.

 

Note Records deleted inside of a transaction that has not yet been committed will still be included in a record count.