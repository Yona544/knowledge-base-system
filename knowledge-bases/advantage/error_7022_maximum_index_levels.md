7022 Maximum index levels




Advantage Database Server 12  

7022 Maximum index levels

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7022 Maximum index levels  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7022 Maximum index levels Advantage Error Guide error\_7022\_maximum\_index\_levels Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7022 Maximum index levels  Advantage Error Guide |  |  |  |  |

Problem: The current index is unbalanced. This problem is most likely to occur when using very long index keys and new keys are being added to the index. This error could also occur if the index is corrupt.

Solution: Reindex the file. The reindexed file will be built using the minimum number of levels. This will speed up all future operations using the index. If this does not resolve the problem, reindex with a larger page size (see [Index Page Size](master_index_page_size.htm), or see the API AdsReindex61 in the Advantage Client Engine Help or the method AdsIndexPageSize in the Advantage TDataSet Descendant Help). With a larger index page size, more keys will be stored in each page and will thus reduce the number of levels required. For specific equations showing the correlation between key and page size, see [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.htm).