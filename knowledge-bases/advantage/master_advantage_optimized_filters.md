Advantage Optimized Filters




Advantage Database Server 12  

Advantage Optimized Filters

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Advantage Optimized Filters  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Advantage Optimized Filters Advantage Concepts master\_Advantage\_optimized\_filters Advantage Concepts > Advantage Functionality > Advantage Optimized Filters / Dear Support Staff, |  |
| Advantage Optimized Filters  Advantage Concepts |  |  |  |  |

Advantage Optimized Filters (AOFs) provide high performance filter optimization for Advantage applications. AOFs speed filter processing by using index keys instead of table records. If a specified field has an index built on it, an AOF uses the index file rather than the table to process the filter. AOFs are used to increase performance of record filtering when directly opening a table for navigational use and setting a filter on that table, as well as used to increase the performance of filtering records in the WHERE clause of an SQL query. Reducing the amount of data that must be retrieved from the disk increases performance.

An AOF can be thought of as a query on the table. When an application sets an AOF on a table opened directly, or issues an SQL SELECT query with a WHERE clause, the Advantage Database Server will build an AOF to filter those records. The server uses indexes that have been opened for the given table to quickly determine which records are in the AOF. The actual AOF consists of an array of bits (in natural record number order) where each bit represents a single record. The bit for each record that passes the filter condition is turned on.

In general, AOFs are created by matching portions of the filter or WHERE clause expression with index key expressions. For example, if the field "lastname" is indexed, Advantage can quickly optimize the filter expression "lastname >= W .AND. lastname <= Wil". The Advantage Database Server will Seek to the appropriate location in the index and traverse the index pages and set bits in the AOF for records that pass the filter condition. When doing this, Advantage does not read the actual records but will read only the necessary index pages needed to resolve the filter.

AOFs are created when an SQL SELECT query has a WHERE clause or by one of the following methods when opening a table directly:

|  |  |
| --- | --- |
| · | Calling the AdsSetAOF function with the Advantage Client Engine API |

|  |  |
| --- | --- |
| · | By default, the Filter property in the TAdsTable and TAdsQuery components will create an Advantage Optimized Filter. To use traditional record filters with the Filter property rather than AOFs, set the AdsOptimizedFilters subproperty to False. |

|  |  |
| --- | --- |
| · | By default, all filters set will use AOFs with the Advantage CA-Visual Objects RDDs. Calling the Visual Objects function RDDInfo( \_SET\_OPTIMIZE ) or the command "Set Optimize OFF" provides the ability to disable the use of AOFs. |

AOFs are only optimized for DBF tables with CDX index files and with ADT tables with ADI index files. AOFs are not fully supported with DBF tables that use NTX indexes. If an AOF is built on a DBF table with an NTX index, the AOF will be non-optimized. Under certain circumstances, it may still be advantageous to use AOFs with DBF tables and NTX indexes. If multiple passes are to be made through the table with the AOF set (e.g., due to data displayed in a grid), the AOF will generally be faster because all records that do not pass the filter condition will be removed from the AOF during the first pass through the data, and they will not be read during subsequent passes.

Because the Advantage Database Server creates and uses AOFs, network traffic is eliminated when creating AOFs on the Advantage Database Server. With Advantage Local Server, however, network traffic is an issue when creating AOFs on tables that reside on network drives because the index data used to create the AOF must be transported across the network to the client where the Advantage Local Server will create the AOF bitmap. But AOFs with Advantage Local Server should still provide much better performance than when using traditional record filters because only those records that pass the filter condition will ever need to be read over to the client PC.

When using AOFs with the Advantage Database Server, there will be some increased resource usage on the server. This is especially true if non-optimized filters are created. For example, if the filter "lastname = Smith" is used and there is no index available on lastname, the filter will not be optimized. This means that every bit will be turned on initially. Therefore, the memory allocation will be approximately RecordCount / 8 bytes. The total memory allocation for a 1,000,000 record table will be approximately 125,000 bytes. As a developer, you should keep this in mind when using AOFs. The allocation is probably "small" for most server configurations, but if you have a very large number of users forcing allocations like this, the total may be prohibitive. The memory allocation for the array of bits is done in non-contiguous blocks on a demand basis, so if a huge table has only a few records that pass the filter condition, the actual amount of allocated memory is usually quite small.

[Differences Between AOFs and Traditional Record Filters](master_differences_between_aofs_and_traditional_record_filters.htm)

[AOF Optimization](master_aof_optimization.htm)

[AOF Relational Operators](master_aof_relational_operators.htm)

[AOF Performance Tips](master_aof_performance_tips.htm)