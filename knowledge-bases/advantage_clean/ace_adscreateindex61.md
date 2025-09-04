---
title: Ace Adscreateindex61
slug: ace_adscreateindex61
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscreateindex61.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: fe8186c480fad00a15ad45c4fcfc9e5ac47c8aca
---

# Ace Adscreateindex61

AdsCreateIndex61

AdsCreateIndex61

Advantage Client Engine

| AdsCreateIndex61  Advantage Client Engine |  |  |  |  |

Creates a new index order for the given table

Syntax

| UNSIGNED32 | AdsCreateIndex61 (ADSHANDLE hObj,  UNSIGNED8 \*pucFileName,  UNSIGNED8 \*pucTag,  UNSIGNED8 \*pucKeyExpr,  UNSIGNED8 \*pucCondition,  UNSIGNED8 \*pucWhile,  UNSIGNED32 ulOptions,  UNSIGNED32 ulPageSize,  ADSHANDLE \*phIndex); |

Parameters

| hObj (I) | Handle of table or cursor. This can be an index order handle (the master index) if building a subindex. |
| pucFileName (I) | Name of file for new index order. If this is NULL or if the base name is the same as the table and the table type is ADS\_CDX, ADS\_VFP or ADS\_ADT, then a compound AutoOpen index file for hTable will be created/updated. If it is NULL and the table type is ADS\_NTX, an NTX index file with the same base name as the table will be created. If no path is given, the index will be created in the same directory as the table. |
| pucTag (I) | Desired tag name. If NULL, then it is expected to be a non-compound index file. If the table type is ADS\_ADT, then a compound index will always be created. If the tag name is NULL and the table type is ADS\_ADT, the tag name will be the base name of the pucFileName parameter. |
| pucKeyExpr (I) | Index key expression. Can be any valid expression. Valid Advantage expressions can consist of field names, literal values, supported operators, and supported functions. For information on operators and functions supported in Advantage expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md). |
| pucCondition (I) | Optional conditional expression (NULL or empty string indicates no conditional expression). |
| pucWhile (I) | Optional while expression to use when building the index order (NULL or empty string indicates no while clause). This is a transient condition that stops the index build the first time it evaluates to False. Note that though there may be legitimate reasons to create indexes with a While expression, most filtering can be accomplished with the same or better performance by using Advantage Optimized Filters (AOFs). |
| ulOptions (I) | A bit field for defining the options for index creation. The options can be ORed together into the bit field. For example ADS\_COMPOUND | ADS\_UNIQUE. The options are:  ADS\_DEFAULT: If no options are needed, this constant (0) can be used.  ADS\_COMPOUND: Create an index order (tag) within a compound index file. Note that this option is always set when the table type is ADS\_ADT  ADS\_DESCENDING: Create a descending index order.  ADS\_UNIQUE: Create a unique index order.  ADS\_CANDIDATE: This creates a unique index order that prevents duplicate data. On ADT tables, it is the same as the ADS\_UNIQUE option. This can be used with Visual FoxPro tables (ADS\_VFP) to create an index that can be used as a primary key and in referential integrity relationships.  ADS\_CUSTOM: Create an empty index order. The user can add and remove keys via AdsAddCustomKey and AdsDeleteCustomKey.  ADS\_BINARY\_INDEX: Create a [binary index](master_binary_indexes.md). The index expression must have a logical result. This option cannot be combined with other options except for ADS\_COMPOUND. |
| ulPageSize (I) | The page size to use when creating new indexes for tables of type ADS\_ADT. It is ignored for tables of type ADS\_NTX, ADS\_VFP and ADS\_CDX. Valid parameters are ADS\_DEFAULT, or any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If ADS\_DEFAULT is given, then Advantage will compute a page size based on the key size to provide for optimal balancing (see [Index Page Size](master_index_page_size.md)). Note that this parameter is only used when creating a new index file. When this API is used to create additional index orders in an existing index file, then this parameter is ignored. Refer to [Index Page Size](master_index_page_size.md) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.md) for more information. |
| phIndex (O) | Return handle of new index order if successful. |

Remarks

AdsCreateIndex61 creates an index order list of sorted keys in the table the order is based on, referenced by the index key expression. The index key expression and "for" and "while" expression can be any expression supported by the Advantage Expression Engine.

AdsCreateIndex61 will replace existing indexes of the same filename if one exists.

The UNIQUE property of indexes is very different between DBF and ADT table types. With DBFs, an index order created with the UNIQUE property will only include records that are referenced by unique values. If two records result in the identical key value, then only one of the records will be referenced by the index. The second is simply never added, and no error is reported. This is the traditional Xbase behavior of the UNIQUE property.

With ADTs, an index order created with the UNIQUE property enforces all records in the table to be referenced via a unique key. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be logged in the Advantage error log. That error log entry will indicate the record number, the tag name, and the index name associated with the non-unique index value. Up to fifty of these unique key violations will be logged before the index creation will be aborted. If any records are not unique, an error will be returned, and the index will not be usable. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either the AdsCancelUpdate or AdsCloseTable API must be called to cancel the update of the record. Note that the AdsLookupKey API may be used to predetermine that a key is unique.

If you are using Visual FoxPro tables (table type ADS\_VFP), then you can use the ADS\_CANDIDATE option when creating the index. It provides the same unique behavior as the ADS\_UNIQUE option on ADT tables. With ADS\_ADT tables, the ADS\_CANDIDATE and ADS\_UNIQUE options are equivalent.

Subindexes are indexes built on the keys in another index, rather than all the records in a table. The index from which a subindex is created is usually a conditional index. This allows for a subset of the records in a table to be built into a new index.

Custom indexes can only be built on tables opened with the ADS\_CDX or ADS\_ADT option.

If a cursor handle is passed to this function, the index is considered to be a temporary index and is deleted when the cursor is closed.

Note Subindexes obey all current filters, but do not obey all scopes. Reindexing a subindex will create a complete index that is based on all records in the table, not a subindex. Care should be taken when using subindexes rather than traditional record filters or Advantage Optimized Filters (AOFs) to view a subset of table. Though there may be legitimate reasons to use subindexes, most filtering can be accomplished with the same or better performance by using Advantage Optimized Filters (AOFs).

 

Note The maximum index key length is 4082 bytes for ADI indexes, 240 bytes for CDX and IDX indexes, and 256 bytes for NTX indexes. See [Xbase File Format Specifications](master_xbase_file_format_specifications.md) and [Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.md) for more information. Also refer to [Index Page Size](master_index_page_size.md) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.md) for more information about the relationship between key sizes and index page sizes.

 

Important! Do NOT attempt to create a new index or tag of the same name as the current index or tag. Using the same name will cause the pre-existing index to be deleted. If the index was a tag, it will be deleted but not removed from the file and the new index will take its place. Reindex to remove deleted tags.

Using AdsCreateIndex61 with an SQL Result Set

An index may be used on an SQL result set. The index created with AdsCreateIndex61 is on the new result set that is temporary, not on the original source table/tables that were queried to build the result set.

An error 5019 will occur if the second parameter, pucFileName, is null which indicates an index is being added to the auto-open index. Therefore, the pucFileName must not be null - a new filename for the index must be specified. After calling AdsCreateIndex61, the new index file is open and ready for use.

For single table result sets, indexes that exist for the original table may be used after obtaining the result set. Therefore, it would not be necessary to use AdsCreateIndex61 on the result set if the index already exists for the original source table. If AdsCreateTable is used on a single table result set, tag names must be unique to the new temporary index as well as the auto-open index of the original source table.

Using AdsCreateIndex61 with Database Tables

When using AdsCreateIndex61 with database tables), the behavior of this API changes depending on the capabity of the user who opened the table.

If the user is the administrative user (ADSSYS), the newly created index becomes part of the database. It will be automatically available to all users accessing the table.

If the user is not the administrative user, the newly created index is temporary and it is automatically deleted when the table is closed. Since the index is temporary, the second parameter, pucFileName, cannot be NULL when calling this API. Otherwise a 5019 error will occur because the index cannot be added into the auto-open index file.

See Also

[AdsOpenIndex](ace_adsopenindex.md)

[AdsCloseIndex](ace_adscloseindex.md)

[AdsCreateIndex](ace_adscreateindex.md)

[AdsReindex](ace_adsreindex.md)

[AdsReindex61](ace_adsreindex61.md)

[AdsConnect60](ace_adsconnect60.md)

[AdsCreateFTSIndex](ace_adscreateftsindex.md)
