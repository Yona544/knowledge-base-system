---
title: Dotnet Adsextendedreader Createindex
slug: dotnet_adsextendedreader_createindex
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_createindex.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 59cddaf3ae5d27d1f9b6d9af8e5ab9822cf8241a
---

# Dotnet Adsextendedreader Createindex

AdsExtendedReader.CreateIndex

AdsExtendedReader.CreateIndex

Advantage .NET Data Provider

| AdsExtendedReader.CreateIndex  Advantage .NET Data Provider |  |  |  |  |

Creates a new index order for the given table.

 

public void CreateIndex{ string strIndexName, string );

public void CreateIndex( string strIndexName, string strExpr,

string strCondition );

public void CreateIndex( string strIndexName, string strExpr,

IndexOptions eOptions );

public void CreateIndex( string strFileName, string strIndexName,

string strExpr, IndexOptions );

public void CreateIndex( string strFileName, string strIndexName,

string strExpr, IndexOptions eOptions,

string strCondition );

Parameters

| strFileName (I) | Name of file for new index order. If this is NULL or if the base name is the same as the table and the TableType is CDX, VFP or ADT, then a compound AutoOpen index file will be created/updated. If no file name is given and the TableType is NTX, an NTX index file with the same base name as the table will be created. If no path is given, the index will be created in the same directory as the table. |
| strIndexName (I) | Desired index name. If NULL, then it is expected to be a non-compound index file. If the TableType is ADT, then a compound index will always be created. If the strIndexName is NULL and the TableType is ADT, the index name will be the base name of the strFileName parameter. |
| strExpr (I) | Index key expression. Can be any valid expression. Valid Advantage expressions can consist of field names, literal values, supported operators, and supported functions. For information on operators and functions supported in Advantage expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md). |
| strCondition (I) | Optional conditional expression (null or empty string indicates no conditional expression). |
| eOptions (I) | A bit field of the [IndexOptions](dotnet_adsextendedreader_indexoptions.md) enumerations for defining the options for index creation. The options can be ORed together into the bit field. For example AdsExtendedReader.IndexOptions.Compound | AdsExtendedReader.IndexOptions.Unique.  The options are: Default: If no options are needed, this constant (0) can be used. Compound: Create an index order (tag) within a compound index file. Note that this option is always set when the TableType is ADT. Descending: Create a descending index order. Unique: Create a unique index order. Candidate: Create a candidate index (for VFP tables). Binary: Create a [binary index](master_binary_indexes.md). |

Remarks

CreateIndex creates an index order list of sorted keys in the table the order is based on, referenced by the index key expression. The index key expression and "for" and "while" expression can be any expression supported by the Advantage Expression Engine.

CreateIndex will replace existing indexes of the same filename if one exists.

The IndexOptions.Unique property of indexes is very different between DBF and ADT table types. With DBFs, an index order created with the Unique property will only include records that are referenced by unique values. If two records result in the identical key value, then only one of the records will be referenced by the index. The second is simply never added, and no error is reported. This is the traditional Xbase behavior of the Unique property.

With ADTs, an index order created with the Unique property enforces all records in the table to be referenced via a unique key. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be logged in the Advantage error log. That error log entry will indicate the record number, the tag name, and the index name associated with the non-unique index value. Up to fifty of these unique key violations will be logged before the index creation will be aborted. If any records are not unique, an error will be returned, and the index will not be usable. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, [Close](dotnet_adsdatareader_close.md) must be called to cancel the update of the record.

If you are using Visual FoxPro tables (table type VFP), then you can use the candidate option when creating the index. It provides the same unique behavior as the unique option on ADT tables. With ADS\_ADT tables, the candidate and unique options are equivalent.

Custom indexes can only be built on tables opened with the CDX or ADT [TableType](dotnet_adsextendedreader_tabletype.md).

If the connection is a cursor connection, the index is considered to be a temporary index and is deleted when the connection is closed.

Note The maximum index key length for a NTX index is 256 characters and 240 characters for CDX, IDX or ADI indexes. See Xbase File Format Specifications and Advantage Proprietary File Format Specifications for more information.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see Callback Functionality.

 

Important! Do NOT attempt to create a new index or tag of the same name as the current index or tag. Using the same name will cause the pre-existing index to be deleted. If the index was a tag, it will be deleted but not removed from the file and the new index will take its place. [Reindex](dotnet_adsextendedreader_reindex.md) to remove deleted tags.

Using CreateIndex with an SQL Result Set

An index may be used on an SQL result set. The index created with CreateIndex is on the new result set that is temporary, not on the original source table/tables that were queried to build the result set.

An exception will be thrown if strFileName is null, which indicates an index is being added to the auto-open index. Therefore, strFileName must specify a new filename for the index. After calling CreateIndex, the new index file is open and ready for use.

For single table result sets, indexes that exist for the original table may be used after obtaining the result set. Therefore, it would not be necessary to use CreateIndex on the result set if the index already exists for the original source table. If CreateTable is used on a single table result set, tag names must be unique to the new temporary index as well as the auto-open index of the original source table.

Using CreateIndex with Database Tables

When using CreateIndex with database tables, the behavior of this API changes depending on the capability of the user who opened the table.

If the user is the administrative user (ADSSYS), the newly created index becomes part of the database. It will be automatically available to all users accessing the table.

If the user is not the administrative user, the newly created index is temporary and it is automatically deleted when the table is closed. Since the index is temporary, strFileName, cannot be NULL when calling this API. Otherwise a 5019 error will occur because the index cannot be added into the auto-open index file.

See Also

[Progress](dotnet_adsextendedreader_progress.md)

[ProgressMessage](dotnet_adsextendedreader_progressmessage.md)

[Cancel](dotnet_adsextendedreader_cancel.md)

[DeleteIndex](dotnet_adsextendedreader_deleteindex.md)
