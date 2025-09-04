AdsExtendedReader.Reindex




Advantage Database Server 12  

AdsExtendedReader.Reindex

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.Reindex  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.Reindex Advantage .NET Data Provider dotnet\_Adsextendedreader\_reindex Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.Reindex / Dear Support Staff, |  |
| AdsExtendedReader.Reindex  Advantage .NET Data Provider |  |  |  |  |

Rebuilds all open indexes.

public void Reindex();

public void Reindex( int iPageSize );

Remarks

Reindex requires exclusive use of the open indexes. A reindex will rebuild all keys in all open index orders for the table. It is unlikely that reindexing will be necessary if only Advantage applications are using data. If other applications not using Advantage are using data, however, there is a possibility for index corruption to occur. Reindexing occurs automatically when calls are made to [PackTable](dotnet_adsextendedreader_packtable.htm) and [ZapTable](dotnet_adsextendedreader_zaptable.htm). Calling Reindex on a CDX or ADI index that contains a custom index order will results in all keys being removed from the custom index order.

IPageSize is the page size to use when reindexing tables of type ADT. It is ignored for tables of [TableType](dotnet_adsextendedreader_tabletype.htm) NTX, VFP, and CDX. Valid values are any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If no size is given, then the default page size of 512 bytes will be used. Refer to [Index Page Size](master_index_page_size.htm) for more information. Note that if the table is in an Advantage Data Dictionary, then only the administrator connection can be used to change the page size when reindexing a table.

Note Calling Reindex inside a transaction is illegal.

 

Note Reindex operates only on tables. The use of a cursors with Reindex is illegal and will result in an exception.

See Also

[OpenIndex](dotnet_adsextendedreader_openindex.htm)

[CreateIndex](dotnet_adsextendedreader_createindex.htm)

[Progress](dotnet_adsextendedreader_progress.htm)

[ProgressMessage](dotnet_adsextendedreader_progressmessage.htm)

[Cancel](dotnet_adsextendedreader_cancel.htm)