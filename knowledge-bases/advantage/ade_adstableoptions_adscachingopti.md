AdsTableOptions.AdsCachingOption




Advantage Database Server 12  

AdsTableOptions.AdsCachingOption

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsCachingOption  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsCachingOption Advantage TDataSet Descendant ade\_AdsTableOptions.AdsCachingOpti Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsCachingOption  Advantage TDataSet Descendant |  |  |  |  |

Indicates the caching mode of the table.

Syntax

type TAdsTableCachingOption = ( tcNone, tcReads, tcWrites );

property AdsTableOptions.AdsCachingOption

Description

Caching mode to use.  tcNone is the default option and doesnt enable any caching.  tcReads enables caching of table data for reads only.  Updates to the table still get written to the disk.  tcWrites enables read and write caching.  Updates get written to the cache in memory and are only written to disk when the table is closed.  See [Table Data Caching](master_table_data_caching.htm) for more information.

See Also

[Table Data Caching](master_table_data_caching.htm)