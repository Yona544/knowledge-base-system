AdsCacheRecords




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsCacheRecords

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsCacheRecords  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsCacheRecords Advantage TDataSet Descendant ade\_Adscacherecords Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsCacheRecords  Advantage TDataSet Descendant |  |  |  |  |

Sets the number of records to read into the cache on applicable record movement operations.

Syntax

procedure AdsCacheRecords ( usRecords : WORD );

Parameter

|  |  |
| --- | --- |
| usRecords | The number of records to read into the cache by movement operations that use record caching. |

Description

Whenever you perform a Next/Prior operation after performing any other movement operation in your application, the next N records will be read and transferred to the client rather than just a single record. This allows the next N - 1 subsequent skip operations to be performed locally. Thus, the next record will be retrieved from client memory, rather than having to be read over the network from the server. The default number of records that is read and cached on the client is the lesser of 10 or the number of records that can fit in a burst of packets from the Advantage Database Server to the Advantage client. The default burst of packets can contain 8K bytes of data when using IPX for communication and about 22K when using IP.

A usRecords value of 0 (or 1) effectively turns read-ahead record caching off. Testing has shown that, in most cases, read-ahead values greater than 100 records are not beneficial. Also, any editing of data causes the cache to be dumped. Therefore, it is probably detrimental to use a large cache size if an edit is to be made on most records. If a batch operation is being used to skip through a large number of records and update each record, it is probably best to turn off read-ahead record caching.

Be aware that records may be cached on the client, and therefore, may not be read from the table. If you have problems where the client does not recognize changes in the table, call TTable.ReSync or TAdsTable.[AdsRefreshRecord](ade_adsrefreshrecord.htm), which will force the cache to be purged.

If your application calls this method, it will override the AdsTableOptions.[AdsRecordCache](ade_adsrecordcache.htm) design-time setting.

Note This method has no effect when reading data in index order with the [Advantage Local Server](master_advantage_local_server.htm).

 

Note Because this method requires an active table handle, it must be called in the dataset's AfterOpen event. The AfterOpen event is not called by TDataSet until after the TAdsDataSet has already initialized its internal buffers and read the default number of cached records. This can produce unexpected results if you are trying to modify the record caching in the AfterOpen event. This method has been depreciated and should be replaced by using the [AdsTableOptions.AdsRecordCache](ade_adsrecordcache.htm) property in all new applications.

Example

AdsTable1.Active := TRUE;

{ disable record caching for this TAdsTable instance }

AdsTable1.AdsCacheRecords( 0 ) ;

{ since the TDBGrid linked to this table contains 14 rows, read-ahead at least 14 for efficiency }

AdsTable1.AdsCacheRecords( 14 );

See Also

[AdsRefreshRecord](ade_adsrefreshrecord.htm)

[AdsRecordCache](ade_adsrecordcache.htm)

[Read-Ahead Record Caching](master_read_ahead_record_caching.htm)