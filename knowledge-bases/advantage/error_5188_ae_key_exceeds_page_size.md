5188 AE\_KEY\_EXCEEDS\_PAGE\_SIZE




Advantage Database Server 12  

5188 AE\_KEY\_EXCEEDS\_PAGE\_SIZE

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5188 AE\_KEY\_EXCEEDS\_PAGE\_SIZE  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5188 AE\_KEY\_EXCEEDS\_PAGE\_SIZE Advantage Error Guide error\_5188\_ae\_key\_exceeds\_page\_size Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5188 AE\_KEY\_EXCEEDS\_PAGE\_SIZE  Advantage Error Guide |  |  |  |  |

The index key size is too large for the page file size. If you are creating a new index order in an existing index file, Advantage will attempt to automatically rebuild the index with a large enough page size for the new index being built. If it cannot do this, it will be necessary to reindex the file with a larger page size. If you are creating an index order in a new index file, then you should either specify a larger page size or allow Advantage to compute the default page size.

See [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.htm) for the specific equations.