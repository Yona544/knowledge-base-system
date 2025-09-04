---
title: Ade Adscreateindex
slug: ade_adscreateindex
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adscreateindex.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8217e8f20a3caea27d882d9759c0e5ddebcdbe31
---

# Ade Adscreateindex

AdsCreateIndex

TAdsTable/TAdsQuery.AdsCreateIndex

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsCreateIndex  Advantage TDataSet Descendant |  |  |  |  |

Creates a new index order for the given table or cursor.

Syntax

type TAdsIndexOptions = ( optCOMPOUND, optUNIQUE, optDescending,

optCUSTOM );

 

procedure AdsCreateIndex( strFileName, strTagName, strExpression,

strCondition, strWhile : String; setIndexOptions :

TAdsIndexOptions );

Parameters

| strFileName | Name of file for new index order. If this is an empty string or if the base name is the same as the table and the table type is ttAdsCDX, ttAdsVFP, or ttAdsADT, a compound auto-open index file will be created/updated. If it is an empty string and the table type is ttAdsNTX, an ntx index file with the same base name as the table will be created. If no path is given, the index will be created in the same directory as the table. |
| strTagName | Desired alias (tag) name. If this is an empty string, it is expected to be a non-compound index file. If the table type is ttAdsADT, a compound index will be created where the tag name is equal to the base name of the pucFileName parameter. |
| strExpression | Index key expression. Can be a semicolon-delimited list of the fields or any valid expression. Valid Advantage expressions can consist of field names, literal values, supported operators, and supported functions. For information on operators and functions supported in Advantage expressions, see [Advantage Expression Engine](master_advantage_expression_engine.md). |
| strCondition | Optional conditional expression (empty string indicates no conditional expression). See [Conditional Indexes](master_adi_conditional_indexes.md) for more information. |
| strWhile | Optional while expression to use when building the index order (empty string indicates no while clause). This is a transient condition that stops the index build the first time it evaluates to False. Note that though there may be legitimate reasons to create indexes with a while expression, most filtering can be accomplished with the same or better performance by using AOFs. |
| setIndexOptions | An enumerated field for defining the options for index creation.  The options are:  optCOMPOUND: The user is indicating that he is creating an index order (tag) within a compound index file. Note that this option is always set when the table type is ttAdsADT.  optDESCENDING: Create a descending index order.  optUNIQUE: Create a unique index order.  optCANDIDATE: This creates a unique index order that prevents duplicate data. On ADT tables, it is the same as optUNIQUE. This can be used with Visual FoxPro tables (ADS\_VFP) to create an index that can be used as a primary key and in referential integrity relationships.  optCUSTOM: Create an empty index order. The user can add and remove keys via [AdsAddCustomKey](ade_adsaddcustomkey.md) and [AdsDeleteCustomKey](ade_adsdeletecustomkey.md).  optBINARY: Create a [binary index](master_binary_indexes.md). The index expression must have a logical result. This option cannot be combined with other options except for optCOMPOUND. |

Description

AdsCreateIndex creates an index order that maintains a list of sorted keys that references records in the table the order is based on by the index key expression. The index key expression and "for" and "while" expression can be any expression supported by the Advantage Expression Engine.

AdsCreateIndex will replace existing indexes of the same file name if one exists.

The UNIQUE property of indexes is very different between DBF and ADT table types. With DBF tables, an index order created with the UNIQUE property will only include records referenced by unique values. If two records result in the identical key value, only one of the records will be referenced by the index. The second is simply never added, and no error is reported. This is the traditional Xbase behavior of the UNIQUE property.

With ADTs, an index order created with the UNIQUE property enforces all records in the table to be referenced via a unique key. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be logged in the Advantage error log. That error log entry will indicate the record number, the tag name, and the index name associated with the non-unique index value. Up to fifty of these unique key violations will be logged before the index creation will be aborted. If any records are not unique, an error will be returned, and the index will not be usable. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either AdsCancelUpdate or AdsCloseTable must be called to cancel the update of the record. Note that AdsLookupKey may be used to predetermine that a key is unique.

When creating new index files for ADT tables, the [AdsIndexPageSize](ade_adsindexpagesize.md) property will be respected. When adding a new index order to an existing index file, the AdsIndexpageSize property is ignored, and the existing index page size is maintained. See [Index Page Size](master_index_page_size.md) for more information.

Important! Do NOT attempt to create a new index or tag of the same name as the current index or tag. Using the same name will cause the pre-existing index to be deleted. If the index was a tag, it will be deleted but not removed from the file and the new index will take its place. Reindex to remove deleted tags.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.md).

 

Note Subindexes obey all current filters, but do not obey scopes. Reindexing a subindex will create a complete index that is based on all records in the table, not a subindex. Care should be taken when using subindexes rather than traditional record filters or Advantage Optimized Filters (AOFs) to view a subset of table. Though there may be legitimate reasons to use subindexes, most filtering can be accomplished with the same or better performance by using Advantage Optimized Filters (AOFs).

 

Note The maximum index key length is 4082 bytes for ADI indexes, 240 bytes for CDX and IDX indexes, and 256 bytes for NTX indexes. See [Xbase File Format Specifications](master_xbase_file_format_specifications.md) and [Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.md) for more information. Also refer to [Index Page Size](master_index_page_size.md) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.md) for more information about the relationship between key sizes and index page sizes.

Example

{ Build a unique index in the AutoOpen index named Tag1. A row is in the index only }

{ if the EmpId field is greater than 50

{ Note the key expression 'LastName;DeptNum' is only valid for ADI indexes. }

{ For NTX or CDX indexes, the equivalent expression is 'LastName+DeptNum' }

 

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'EmpId > 50', '', [optUNIQUE] );

AdsTable1.IndexName := 'Tag1';

AdsTable1.First;

Using AdsCreateIndex with TAdsQuery

An index may be used with TAdsQuery after using TAdsQuery.ExecSQL or TAdsQuery.Open to obtain a result set. The index created with TAdsQuery.AdsCreateIndex is on the new result set which is temporary, not on the original source table(s) that was queried to build the result set.

An error 5019 will occur if the first parameter, strFileName, is left blank which indicates an index is being added to the auto-open index. Therefore, the first parameter, strFileName must not be blank and a new filename for the index must be specified. After calling AdsCreateIndex, the new index file is opened and ready for use. To specify an active index use the TAdsQuery.IndexName property.

For single table result sets, indexes that exist for the original table may be used after obtaining the result set. Therefore, it would not be necessary to use AdsCreateIndex on the result set if the index already exists for the original source table. If AdsCreateTable is used on a single table result set, tag names must be unique to the new temporary index as well as the auto-open index of the original source table.

Using AdsCreateIndex with Database Tables

When using AdsCreateIndex with database tables), the behavior of this API changes depending on the capacity of the user who opened the table.

If the user is the administrative user (ADSSYS), the newly created index becomes part of the database. It will be automatically available to all users accessing the table.

If the user is not the administrative user, the newly created index is temporary and it is automatically deleted when the table is closed. Since the index is temporary, the second parameter, pucFileName, cannot be NULL when calling this API. Otherwise a 5054 error will occur because the user does not have permission to add the index into the auto-open index file.

Example for single table result set:

procedure TForm1.Button1Click(Sender: TObject);

begin

//Get result set

AdsQuery1.SQL.Clear();

AdsQuery1.SQL.Add( 'SELECT \* FROM zipcode' );

AdsQuery1.Open();

 

//In this case an index tag name, city, exists in the source table's index. The auto-open index from source table is open and ready to use.

//If the index didn't already exist in the original source table's auto open index, AdsCreateIndex could be used to create a new temp index here (see joined result set

//example below)

AdsQuery1.IndexName := 'city';

 

//Use index

AdsQuery1.FindKey( [ 'Boise' ] );

end;

Example for joined result set:

procedure TForm1.Button2Click(Sender: TObject);

begin

//Get result set

AdsQuery1.SQL.Clear();

AdsQuery1.SQL.Add( 'SELECT company.company\_name, zipcode.city FROM company, zipcode WHERE company.zip\_id = zipcode.id' );

AdsQuery1.Open();

 

//Build temporary index

AdsQuery1.AdsCreateIndex( 'temp\_index', 'company', 'company\_name', '', '', [] );

 

//Activate new index

AdsQuery1.IndexName := 'company';

 

//Use index

AdsQuery1.FindKey( [ 'My Company Inc.' ] );

end;

See Also

[AdsCloseIndex](ade_adscloseindex.md)

[AdsOpenIndex](ade_adsopenindex.md)

[AddIndex](ade_addindex.md)

[AdsIndexPageSize](ade_adsindexpagesize.md)
