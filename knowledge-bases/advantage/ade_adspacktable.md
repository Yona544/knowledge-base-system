AdsPackTable




Advantage Database Server 12  

TAdsTable.AdsPackTable

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsPackTable  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsPackTable Advantage TDataSet Descendant ade\_Adspacktable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsPackTable  Advantage TDataSet Descendant |  |  |  |  |

Removes deleted records from the given table and re-indexes the table.

Syntax

procedure AdsPackTable;

Description

AdsPackTable removes all deleted records from this table instance. Internal fragmentation in memo files will also be eliminated. The table is then re-indexed. If a progress callback function is available, it will be called during the reindexing. The indexes must be opened during the pack or they will become logically invalid. This operation requires exclusive access to the table, which is specified during the open.

Note that if encryption was ever enabled on the table, the table cannot be packed unless the encryption is enabled with the correct password.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsPackTable;

See Also

[AdsRegisterCallbackFunction](ade_adsregistercallbackfunction.htm)

[AdsZapTable](ade_adszaptable.htm)

[AdsEnableEncryption](ade_adsenableencryption.htm)

[AdsDecryptTable](ade_adsdecrypttable.htm)