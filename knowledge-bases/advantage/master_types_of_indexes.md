Types of Indexes




Advantage Database Server 12  

Types of Indexes

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Types of Indexes  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Types of Indexes Advantage Concepts master\_Types\_of\_indexes Advantage Concepts > Advantage ISAM Concepts > Types of Indexes / Dear Support Staff, |  |
| Types of Indexes  Advantage Concepts |  |  |  |  |

Advantage supports several types of index files and index orders.

Single Order Index Files

A single order index file is an index file containing only one index order. Up to 15 index files can be opened per table.

Multiple Order (Compound) Index Files

A multiple order index file (also referred to as a compound index file) is an index file containing more than one index order. An individual index order within a multiple order index file is often referred to as a "tag." Multiple order index files are easier to maintain than single order index files because in a multiple order index file just the one index file needs to be opened when the table is opened. Whether an index order is contained in a single order index file or a multiple order index file has no impact on the functionality of the index order. Up to 50 index orders (tags) can be contained within a multiple order index file. Up to 15 index files can be opened per table.

Multi-segmented Index

A multi-segmented index is an individual index order that contains multiple fields and/or expressions within the index key expression. For example, an index created on "lastname", where "lastname" is a field in the table, would not be a multi-segmented index. But an index created on "lastname; firstname" (with ADI index files) or "lastname + firstname" (with DBF index files), would be a multi-segmented index. An index created on "lastname; str( ssn )" or "lastname + str( ssn )" is also an example of a multi-segmented index. Other terms that are sometimes used that mean the same thing as a multi-segmented index are multiple-field index, composite index, and composite key.

Auto-Open and Structural Index Files

An auto-open index file is an index file that is automatically opened when the associated table is opened. Therefore, an auto-open index file does not need to be explicitly opened when the table is opened. In order for an index file associated with a [free connection](javascript:hhpopuplink.TextPopup(popid_1658562324,FontFace,-1,-1,-1,-1)) to be an auto-open index file, it must contain the same base file name as the table and the index file must exist in the same directory as the table. Only the extensions of the files will be different. These auto-open indexes are also often referred to as structural indexes. All indexes associated with a [database connection](javascript:hhpopuplink.TextPopup(popid_773697001,FontFace,-1,-1,-1,-1)) are auto-open indexes and will be automatically opened when the table is opened. Just as auto-open index files are automatically opened, they are automatically closed when the table is closed, and cannot be closed while the table is open.

All multiple order index files associated with a [free connection](javascript:hhpopuplink.TextPopup(popid_1658562324,FontFace,-1,-1,-1,-1)) that do not have the same base file name as the corresponding table are considered non-auto-open ("non-structural") and will not be automatically opened when the table is opened. The application needs to specifically open the files or logical corruption will occur if any data is updated.

Conditional Indexes

Conditional indexes are index orders that allow you to view only those data records that meet a pre-defined condition. Conditional indexes include only those records which satisfy a given filter expression. The conditional indexs filter expression may be any valid expression that evaluates to a logical value. Valid Advantage expressions can consist of field names, literal values, supported operators, and supported functions. For information on operators and functions supported in Advantage expressions, see [Advantage Expression Engine](master_advantage_expression_engine.htm).

Conditional indexes are updated like normal indexes, with records added to or deleted from the index based on the conditional indexs filter expression. As the table is updated, only records that match the conditional indexs filter expression are added to the index. If a record changes and no longer matches the conditional indexs filter expression, the record is removed from the index.

While Indexes

While indexes are index orders created with a "while" clause. The while clause is a transient condition that stops the index build the first time it evaluates to False. This allows the creation of temporary views of data. When creating a While index, the index creation will begin with the current record rather than using the first record in the table (or first record in the controlling index order if creating a subindex).

Unlike Conditional indexes, where the conditional index expression is used to determine whether records inserted, updated, or deleted have a [key](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) that references that record, the While expression is not used when a record is inserted, updated, or deleted. Instead, While indexes get updated like any other "normal" index order. The While expression is only evaluated upon index creation. Therefore, While indexes are really only useful as temporary indexes that should be deleted when there temporary use has been fulfilled.

The While index expression is not stored in the index header. Thus, if a While index is reindexed, the While index will become a regular index that contains [keys](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) referencing all records in the table.

Care should be taken when using While indexes rather than traditional record filters or Advantage Optimized Filters (AOFs) to view a subset of table. Though there may be legitimate reasons to use While indexes, most filtering can be accomplished with the same or better performance by using AOFs.

Subindexes

Subindexes are index orders that are built based on another "controlling" index order, which is usually a conditional index. A subindex includes only the records contained in the controlling index upon which it is based. This allows the creation of temporary views of data.

Subindexes do not inherit any conditions from the controlling index upon which the subindex is based. If reindexed, the subindex becomes a regular index that is based on all records in the table; it will not be created based upon the currently active index.

Care should be taken when using subindexes rather than traditional record filters or Advantage Optimized Filters (AOFs) to view a subset of table. Though there may be legitimate reasons to use subindexes, most filtering can be accomplished with the same or better performance by using AOFs.

Note When creating a subindex, any [Index Scopes](master_index_scopes_ranges.htm) that exist on the controlling index will NOT be obeyed.

Custom Indexes

Custom indexes are index orders that are originally created "empty". That is, when originally created, the custom index will not reference any records in the table. References to individual records can be added or dropped as desired via Advantage client APIs. Custom indexes allow the developer to create a custom view of the table based on [keys](javascript:hhpopuplink.TextPopup(popid_44303104X,FontFace,-1,-1,-1,-1)) that have been added to the custom index order.

Unique Indexes

The unique property of index orders is very different depending on the Advantage table type being used. For information on unique indexes, see [ADI Unique Indexes](master_adi_unique_indexes.htm) or [Xbase Unique Indexes](master_xbase_unique_indexes.htm).

Binary Indexes

Binary indexes, first introduced in version 10.0, are very compact indexes based on index expressions with logical (Boolean) results. They can be used with ADT and DBF tables. See [Binary Indexes](master_binary_indexes.htm) for details.