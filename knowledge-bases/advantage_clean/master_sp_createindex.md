---
title: Master Sp Createindex
slug: master_sp_createindex
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_createindex.htm
source: Advantage CHM
tags:
  - master
checksum: a7ff6af7234f1c8b951bbbce2ac98b08b3413c49
---

# Master Sp Createindex

sp\_CreateIndex

sp\_CreateIndex

Advantage SQL Engine

| sp\_CreateIndex  Advantage SQL Engine |  |  |  |  |

Creates a new index order for the given table.

Syntax

sp\_CreateIndex( TableName,CHARACTER,515,

               FileName,CHARACTER,515,

               TagName,CHARACTER,128,

               Expression,CHARACTER,510,

               Condition,CHARACTER,510,

               Options,INTEGER,

               PageSize,INTEGER );

 

sp\_CreateIndex90( TableName,CHARACTER,515,

                 FileName,CHARACTER,515,

                 TagName,CHARACTER,128,

                 Expression,CHARACTER,510,

                 Condition,CHARACTER,510,

                 Options,INTEGER,

                 PageSize,INTEGER,

                 Collation,CHARACTER,50 );

Parameters

| TableName (I) | Name of the table to create the index order on. This must be a relative path to the table on the server or a fully qualified UNC path. |
| FileName (I) | Name of file for new index order. If this is NULL or if the base name is the same as the table and the table type is ADS\_CDX, ADS\_VFP, or ADS\_ADT, then a compound AutoOpen index file for TableName will be created/updated. If it is NULL and the table type is ADS\_NTX, an NTX index file with the same base name as the table will be created. If no path is given, the index will be created in the same directory as the table. |
| TagName (I) | Desired tag name. If NULL, then it is expected to be a non-compound index file. If the table type is ADS\_ADT, then a compound index will always be created. If the tag name is NULL and the table type is ADS\_ADT, the tag name will be the base name of the FileName parameter. |
| Expression (I) | Index key expression. Can be any valid expression. Valid Advantage expressions can consist of field names, literal values, supported operators, and supported functions. For information on operators and functions supported in Advantage expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md). |
| Condition (I) | Optional conditional expression (NULL or empty string indicates no conditional expression). |
| Options (I) | A bit field for defining the options for index creation. The options can be ORed together into the bit field. For example ADS\_COMPOUND | ADS\_UNIQUE. The options (with the constants defined in ace.h) are:  ADS\_DEFAULT (0): If no options are needed, this constant can be used.  ADS\_UNIQUE (1): Create a unique index order.  ADS\_COMPOUND (2): Create an index order (tag) within a compound index file. Note that this option is always set when the table type is ADS\_ADT.  ADS\_CUSTOM (4): Create an empty index order. The user can add and remove keys via AdsAddCustomKey and AdsDeleteCustomKey.  ADS\_DESCENDING (8): Create a descending index order.  ADS\_CANDIDATE (2048): This creates a unique index order that prevents duplicate data. On ADT tables, it is the same as the ADS\_UNIQUE option. This can be used with Visual FoxPro tables (ADS\_VFP) to create an index that can be used as a primary key and in referential integrity relationships.  ADS\_BINARY\_INDEX (4096): Create a [binary index](master_binary_indexes.md). The index expression must have a logical result. This option cannot be combined with other options except for ADS\_COMPOUND.  ADS\_ONLINE (2097152):  Create the index online allowing other users to access or update the table during the build.  See [Online Table Maintenance](master_online_table_maintenance.md) for more information.  If you are not using a parameterized statement, you can pass the numeric values for these options in the statement directly. Two combine options, add the values together. For example, to create a binary compound index, pass the value 4098 (2+4096). |
| PageSize (I) | The page size to use when creating new indexes for tables of type ADS\_ADT. It is ignored for tables of type ADS\_NTX, ADS\_CDX, and ADS\_VFP. Valid parameters are 0, or any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If o is given, then the default page size of 512 bytes will be used. Note that this parameter is only used when creating a new index file. When this system procedure is used to create additional index orders in an existing index file, then this parameter is ignored. Refer to [Index Page Size](master_index_page_size.md) for more information. |
| Collation (I) | When using the procedure sp\_CreateIndex90, this parameter can be used to specify the name of a [dynamic collation](master_collation_support.md) that differs from the collation currently associated with the SQL statement. |

Remarks

sp\_CreateIndex creates an index order list of sorted keys in the table the order is based on, referenced by the index key expression. The index key expression and "for" expression can be any expression supported by the Advantage Expression Engine.

sp\_CreateIndex will replace existing indexes of the same filename if one exists.

The UNIQUE property of indexes is very different between DBF and ADT table types. With DBFs, an index order created with the UNIQUE property will only include records that are referenced by unique values. If two records result in the identical key value, then only one of the records will be referenced by the index. The second is simply never added, and no error is reported. This is the traditional Xbase behavior of the UNIQUE property.

With ADTs, an index order created with the UNIQUE property enforces all records in the table to be referenced via a unique key. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be logged in the Advantage error log. That error log entry will indicate the record number, the tag name, and the index name associated with the non-unique index value. Up to fifty of these unique key violations will be logged before the index creation will be aborted. If any records are not unique, an error will be returned, and the index will not be usable. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either the AdsCancelUpdate or AdsCloseTable API must be called to cancel the update of the record. Note that the AdsLookupKey API may be used to predetermine that a key is unique.

If you are using Visual FoxPro tables (table type ADS\_VFP), then you can use the ADS\_CANDIDATE option when creating the index. It provides the same unique behavior as the ADS\_UNIQUE option on ADT tables. With ADS\_ADT tables, the ADS\_CANDIDATE and ADS\_UNIQUE options are equivalent.

Subindexes are indexes built on the keys in another index, rather than all the records in a table. The index from which a subindex is created is usually a conditional index. This allows for a subset of the records in a table to be built into a new index. Custom indexes can only be built on tables opened with the ADS\_CDX or ADS\_ADT option.

Note Subindexes obey all current filters, but do not obey all scopes. Reindexing a subindex will create a complete index that is based on all records in the table, not a subindex. Care should be taken when using subindexes rather than traditional record filters or [Advantage Optimized Filters (AOFs)](master_advantage_optimized_filters.md) to view a subset of table. Though there may be legitimate reasons to use subindexes, most filtering can be accomplished with the same or better performance by using Advantage Optimized Filters.

 

Note The maximum index key length is 4082 bytes for ADI indexes, 240 bytes for CDX and IDX indexes, and 256 bytes for NTX indexes. See [Xbase File Format Specifications](master_xbase_file_format_specifications.md) and [Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.md) for more information. Also refer to [Index Page Size](master_index_page_size.md) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.md) for more information about the relationship between key sizes and index page sizes.

 

Note The maximum index key length for a NTX index is 256 characters and 240 characters for CDX, IDX or ADI indexes. See [Xbase File Format Specifications](master_xbase_file_format_specifications.md) and [Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.md) for more information.

 

Important! Do NOT attempt to create a new index or tag of the same name as the current index or tag. Using the same name will cause the pre-existing index to be deleted. If the index was a tag, it will be deleted but not removed from the file and the new index will take its place. Reindex to remove deleted tags.

Using sp\_CreateIndex with Database Tables

When using sp\_CreateIndex with database tables, the user creating the index must be an administrative user.

See Also

[sp\_ModifyIndexProperty](master_sp_modifyindexproperty.md)

[sp\_Reindex](master_sp_reindex.md)
