AdsReindexFTS




Advantage Database Server 12  

AdsReindexFTS

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsReindexFTS  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsReindexFTS Advantage Client Engine ace\_Adsreindexfts Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsReindexFTS  Advantage Client Engine |  |  |  |  |

Rebuilds index files that contain only full text search indexes.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsReindexFTS ( ADSHANDLE hTable,  UNSIGNED32 ulPageSize ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table. |
| ulPageSize (I) | The page size to use when reindexing tables of type ADS\_ADT. It is ignored for tables of type ADS\_CDX and ADS\_VFP. Valid parameters are ADS\_DEFAULT, or any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If ADS\_DEFAULT is given, then a default page size of 1024 bytes will be used. Refer to [Index Page Size](master_index_page_size.htm) for more information. Note that if the table is in an Advantage Data Dictionary, then only the administrator connection can be used to change the page size when reindexing a table. If a user connection is used to reindex a table in a data dictionary, ADS\_DEFAULT should be passed as the index page size. |

Remarks

This API rebuilds index files that contain only full text search (FTS) indexes. If an index file contains any non-FTS indexes, then it will not be rebuilt by a call to this API. Use [AdsReindex61](ace_adsreindex61.htm) to reindex all indexes on a table (including FTS indexes).

Note Calling AdsReindexFTS inside a transaction is illegal.

See Also

[AdsCreateFTSIndex](ace_adscreateftsindex.htm)

[AdsReindex61](ace_adsreindex61.htm)