---
title: Master Index Page Size
slug: master_index_page_size
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_index_page_size.htm
source: Advantage CHM
tags:
  - master
checksum: 6bdc43c9128e7f34da16c4f650c55050a1985d6b
---

# Master Index Page Size

Index Page Size

Index Page Size

Advantage Concepts

| Index Page Size  Advantage Concepts |  |  |  |  |

Advantage Proprietary Index files (ADIs) have a configurable page size, with a default of 512 bytes. There are some situations where it may be desirable to use larger page sizes.

- As a general rule, tables with over one million records per table may benefit from larger index page sizes. Filters and SQL queries that include most of the records in the table may run faster with increased index page sizes. However, searches for single records or small subsets of the table probably would not benefit from larger page sizes.

- Indexes with large keys may require larger page sizes. If the page size is not large enough, it may not be possible to create an index with longer keys. In addition, if the page size is too small, Advantage may not be able to balance the index properly, which could result in a 7022 error when updating the table.

Table Size

Information in Advantage Proprietary Index files (.ADIs) is stored with a uniform page size. By default, the page size is 512 bytes. Unless it is a custom or conditional index, each record in the associated table has a key in the index that "points" to the record. The benefits of indexes are that they allow fast lookup of records or a sequence of records as well as fast ordering of records. There is a downside too. The indexes must be maintained as records are appended, modified, and deleted. The cost of maintaining indexes, however, is relatively small especially when compared to the benefits they provide.

As an index file grows and is updated, the pages that represent a single index order can be physically disjoint within the file itself; it effectively becomes fragmented internally. In general, this does not cause problems because very few file reads are usually necessary to complete a given operation. For example, when seeking for a specific record, the server may read 4 index pages in a table that has 1 million records. An update operation, though, that modifies multiple fields that are in indexes may cause the server to read and update 10 to 20 index pages in the same size table.

An operation that reads a large percentage of the pages that make up an index can be hurt from a performance standpoint once an index becomes fragmented. This is because the cost of reading a 512-byte page generally incurs more overhead. Depending on various operating system settings, the OS will usually read more than the 512 bytes requested by an application. For example, the OS may read 8K of data in anticipation that the application will continue reading at the same file offset. This is referred to as spatial locality; applications tend to reference data at or near the last recently referenced data. Most operating systems will read more than the 512 bytes and will cache the information for future read requests. If a large number of index pages with no spatial locality are read, the operating system will spend most of its time reading unused data and managing the cache. The difference in what the operating system views as a page versus the index page size effectively creates an impedance mismatch that can hurt performance. When there is no temporal locality in access of the index pages, and the amount of data exceeds the operating system cache limit, then little or no benefit is derived from the operating system caching while the penalty is still paid for the management of the cache. The cost of every page read is largely determined by the latency of the hard disk.

If, however, the index page is "small" enough, the operating system may end up caching the entire index in memory even though it may be fragmented within the index file itself. In this case, there would be no degradation with the mismatch in page sizes.

As previously mentioned, the few index pages used in most operations is not affected by the page size differences. The primary exception to this is when the Advantage Database Server reads large portions of an index in logical order. One case is simply when reading through a table in index order. This is not a very critical case, though, because the amount of work involved in reading index pages is relatively small compared to the other processing involved (reading records and transferring them to the client). A more critical and obvious performance hit can be seen when setting [Advantage Optimized Filters](master_advantage_optimized_filters.md) either directly via a filter property on a table or indirectly through an SQL statement. For example, an SQL statement of the form "SELECT \* FROM employee WHERE lastname > A" would likely create an Advantage Optimized Filter that would end up reading almost the entire index (assuming an index existed on the lastname field). If the index file was large enough and was fragmented internally, then the server could take a much longer time than expected to resolve the query. This could happen if the table had several million records and the index was, for example, 20 megabytes in size. Note that if the WHERE clause were more restrictive (e.g., WHERE lastname = Jones), then only a few index pages would be read and there would be no performance degradation.

One solution to this problem is to reindex the table if the index files become fragmented. In a specific test case on a table with several million records, it was taking 32 seconds to fully resolve an Advantage Optimized Filter that read the entire index (a very nonrestrictive filter). After reindexing, it took 1.3 seconds to fully resolve the filter. The reindex operation lays out the index pages so that the physical and logical orders are identical. Thus, reading the index in logical order matches the physical disk layout and the operating system can read the pages extremely efficiently.

Another possible solution is to use larger index pages. Beginning with version 6.1 of the Advantage Database Server, it is possible to create Advantage Proprietary Index files (.ADIs) with page sizes greater than 512 either through the API AdsCreateIndex61 or through the use of the TAdsDataSet property AdsTableOptions.AdsIndexPageSize. Consider the specific case mentioned above where it took 32 seconds to fully resolve the Advantage Optimized Filter on a multi-million record table. With index pages 8192 bytes in size, it took 1.2 seconds to fully resolve the same filter both before and after reindexing. In addition, Seek operations were about 80% faster when using 8K pages versus 512 byte pages. Simple updates on average were unchanged; the benefit gained from the faster index traversal was offset by the added cost of updating the larger index page.

Using larger index pages, however, is not a cure-all. The operating system may be able to handle the larger page size more efficiently when reading and writing, but the Advantage Database Server has to perform more processing to manage the larger pages. In general, it is probably best to use the default page size of 512 bytes unless the smaller page size is specifically hurting your application performance. If the table is large enough, it may make sense to use larger index pages. You should test specifically with your own application in order to determine if it makes sense to use larger index pages.

When using local server with files across a network, the larger index pages will almost certainly be a hindrance. The cost of reading the larger pages across the network far outweigh any benefit that the network file server may gain from dealing with the larger pages.

Using large index pages on "smaller" tables can be more expensive as well. When dealing with smaller index files, the additional cost of maintaining the larger pages is the determining factor. Testing with tables having 100,000 records showed that update operations were about 5 times faster when using 512 byte pages versus 8K pages. Seek operations were about 4 times faster with the smaller page size.

Index Key Size

Index key size also has a relationship to index page size. It is necessary to be able to fit at least 2 keys per index page to be able to build the index. For optimal tree balancing, it is best if at least 3 keys can be guaranteed to fit in a page. With most applications, this is not an issue since most index keys are not very large. If, however, you build indexes with larger key sizes (e.g., on a very long character field or on some concatenated fields), then it may be necessary to use a larger page size.

Since a given index file uses the same page size for all index orders in that file, the required page size is effectively determined by the single largest key of all the indexes in the file. The key size for character fields is equal to the number of characters. So an index on a 50-byte character field will have 50 byte keys. For an index composed of concatenated fields, the key size is simply the sum of the individual field key sizes. The key size for all numeric (integer, double, money, currency, etc.), date, and timestamp field types is 8 bytes. Keys for time fields are 4 bytes, and keys for logical fields are 1 byte. Keys for character and raw fields are 1 byte for each character/byte in the field. The index management utility in Advantage Data Architect can be used to view the key size for any index if you are in doubt about its length.

If you are adding a new index order to an existing index file, then the key size of the new index is limited by the current page size. If, for example, the page size of the existing file is 1024 bytes, then the largest key size that can be added to that file is 498 bytes. Advantage will attempt to rebuild the index file with a larger index page size to accommodate the new index when it encounters this situation. For this to succeed, however, it must be able to gain exclusive access to the table, and the existing index orders cannot be custom (ADS\_CUSTOM) indexes. The alternative is to create the new index order in a different index file. This may be a good strategy for performance reasons. If a given table has indexes with widely varying key sizes, it may make sense to keep all the indexes with "smaller" key sizes in one index file with a page size of 512 or 1024 and build indexes with "larger" key sizes in an index file with a page size of 2048 or larger.

See [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.md) for the equations showing the correlation between key and page sizes.
