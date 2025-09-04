AdsReindex




Advantage Database Server 12  

TAdsTable.AdsReindex

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsReindex  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsReindex Advantage TDataSet Descendant ade\_Adsreindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsReindex  Advantage TDataSet Descendant |  |  |  |  |

Rebuilds all open indexes associated with the given table.

Syntax

procedure AdsReindex;

Description

AdsReindex requires exclusive use of the open indexes. A reindex will rebuild all keys in all open index orders for the table. It is unlikely that reindexing will be necessary if only Advantage applications are using data. If other applications not using Advantage are using data, however, there is a possibility for index corruption to occur. Reindexing occurs automatically when calls are made to [AdsPackTable](ade_adspacktable.htm) and [AdsZapTable](ade_adszaptable.htm).

When reindexing ADT tables, the [AdsIndexPageSize](ade_adsindexpagesize.htm) property will be respected. See [Index Page Size](master_index_page_size.htm) for more information. Note that if the table is in an Advantage Data Dictionary, then only the administrator connection can be used to change the page size when reindexing a table.

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

 

Note Calling AdsReindex inside a transaction is illegal.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsReindex;

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsOpenIndex](ade_adsopenindex.htm)

[AdsRegisterProgressCallback](ade_adsregisterprogresscallback.htm)

[AdsIndexPageSize](ade_adsindexpagesize.htm)