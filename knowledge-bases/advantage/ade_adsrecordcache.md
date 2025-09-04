AdsRecordCache




Advantage Database Server 12  

AdsTableOptions.AdsRecordCache

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsRecordCache  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsRecordCache Advantage TDataSet Descendant ade\_Adsrecordcache Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsRecordCache  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Indicates the level of read-ahead record caching Advantage uses for record movements.

Syntax

TAdsRecordCacheTypes = ( rcNone, rcStandard, rcAggressive );

 

property AdsTableOptions.AdsRecordCache;

Description

This property controls the read-ahead record caching performed by Advantage. The default value is rcStandard, which causes Advantage to use the default caching level. The default cache is the lesser of 10 records or the number of records that can fit in a burst of packets from the Advantage Database Server to the Advantage client. The default burst of packets can contain 8K bytes of data when using IPX for communication and about 22K when using IP. If the AdsRecordCache value is set at runtime, then the value of rcStandard will result in a cache of 10 records regardless of the record length and packet burst size. A value of rcNone specifies that Advantage will perform no read-ahead caching. A value of rcAggressive specifies that Advantage will read 100 records into the cache.

Aggressive caching may be useful for batch operations that read through large portions of a table in one direction with no editing. Each edit operation dumps the entire cache, therefore it is generally not a good idea to use rcAggressive for tables that will have a large number of edits made on them. If a batch operation is being used to skip through a large number of records and update each record, it is probably best to turn off read-ahead record caching.

If the [AdsCacheRecords](ade_adscacherecords.htm) method is called, it will override the design-time setting of this property. Both this property and the AdsCacheRecords method use the same Advantage Client Engine API.

Be aware that records may be cached on the client, and therefore, may not be read from the table. If you have problems where the client does not recognize changes in the table, call TTable.ReSync or [AdsRefreshRecord](ade_adsrefreshrecord.htm), which will force the cache to be purged.

Note This property has no effect when reading data in index order with the Advantage Local Server.

See Also

[AdsRefreshRecord](ade_adsrefreshrecord.htm)

[AdsCacheRecords](ade_adscacherecords.htm)

[Read-Ahead Record Caching](master_read_ahead_record_caching.htm)