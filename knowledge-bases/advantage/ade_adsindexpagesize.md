AdsIndexPageSize




Advantage Database Server 12  

AdsTableOptions.AdsIndexPageSize

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsIndexPageSize  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsIndexPageSize Advantage TDataSet Descendant ade\_Adsindexpagesize Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsIndexPageSize  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Indicates the page size to use when creating new index files ([AdsCreateIndex](ade_adscreateindex.htm) and [AddIndex](ade_addindex.htm)) and when reindexing existing index files ([AdsReindex](ade_adsreindex.htm)).

Syntax

property AdsTableOptions.AdsIndexPageSize;

Description

When creating new index files or reindexing tables of type ADS\_ADT, it is possible to specify the index page size to use. The valid range is 512 to 8192. 0 can also be specified to allow Advantage to choose the page size based on the index key size. See [Index Page Size](master_index_page_size.htm) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.htm) for more information.

This property is populated with the index page size of the first index file when the table is opened. If you have multiple index files with different index page sizes, this means that they will all have the same page size as the first opened index after reindexing with the AdsReindex method. Note that the AdsReindex Advantage Client Engine API will maintain the index page size for each individual index file.