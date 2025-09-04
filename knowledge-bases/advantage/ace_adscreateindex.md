AdsCreateIndex




Advantage Database Server 12  

AdsCreateIndex

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCreateIndex  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCreateIndex Advantage Client Engine ace\_Adscreateindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCreateIndex  Advantage Client Engine |  |  |  |  |

Creates a new index order for the given table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsCreateIndex (ADSHANDLE hObj,  UNSIGNED8 \*pucFileName,  UNSIGNED8 \*pucTag,  UNSIGNED8 \*pucKeyExpr,  UNSIGNED8 \*pucCondition,  UNSIGNED8 \*pucWhile,  UNSIGNED32 ulOptions,  ADSHANDLE \*phIndex); |
| UNSIGNED32 | AdsCreateIndex61 (ADSHANDLE hObj,  UNSIGNED8 \*pucFileName,  UNSIGNED8 \*pucTag,  UNSIGNED8 \*pucKeyExpr,  UNSIGNED8 \*pucCondition,  UNSIGNED8 \*pucWhile,  UNSIGNED32 ulOptions,  UNSIGNED32 ulPageSize,  ADSHANDLE \*phIndex); |
| UNSIGNED32 | AdsCreateIndex90 (ADSHANDLE hObj,  UNSIGNED8 \*pucFileName,  UNSIGNED8 \*pucTag,  UNSIGNED8 \*pucKeyExpr,  UNSIGNED8 \*pucCondition,  UNSIGNED8 \*pucWhile,  UNSIGNED32 ulOptions,  UNSIGNED32 ulPageSize,  UNSIGNED8 \*pucCollation,  ADSHANDLE \*phIndex); |

Parameters

|  |  |
| --- | --- |
| hObj (I) | Handle of table or cursor. This can be an index order handle (the master index) if building a subindex. |
| pucFileName (I) | Name of file for new index order. If this is NULL or if the base name is the same as the table and the table type is ADS\_CDX, ADS\_VFP or ADS\_ADT, then a compound AutoOpen index file for hTable will be created/updated. If it is NULL and the table type is ADS\_NTX, an NTX index file with the same base name as the table will be created. If no path is given, the index will be created in the same directory as the table. |
| pucTag (I) | Desired tag name. If NULL, then it is expected to be a non-compound index file. If the table type is ADS\_ADT, then a compound index will always be created. If the tag name is NULL and the table type is ADS\_ADT, the tag name will be the base name of the pucFileName parameter. |
| pucKeyExpr (I) | Index key expression. Can be any valid expression. Valid Advantage expressions can consist of field names, literal values, supported operators, and supported functions. For information on operators and functions supported in Advantage expressions, see [Advantage Expression Engine](master_advantage_expression_engine.htm). |
| pucCondition (I) | Optional conditional expression (NULL or empty string indicates no conditional expression). |
| pucWhile (I) | Optional while expression to use when building the index order (NULL or empty string indicates no while clause). This is a transient condition that stops the index build the first time it evaluates to False. Note that though there may be legitimate reasons to create indexes with a While expression, most filtering can be accomplished with the same or better performance by using Advantage Optimized Filters (AOFs). |
| ulOptions (I) | A bit field for defining the options for index creation. The options can be ORed together into the bit field. For example ADS\_COMPOUND | ADS\_UNIQUE. The options are:    ADS\_DEFAULT: If no options are needed, this constant (0) can be used.    ADS\_COMPOUND: Create an index order (tag) within a compound index file. Note that this option is always set when the table type is ADS\_ADT    ADS\_DESCENDING: Create a descending index order.    ADS\_UNIQUE: Create a unique index order.    ADS\_CANDIDATE: This creates a unique index order that prevents duplicate data. On ADT tables, it is the same as the ADS\_UNIQUE option. This can be used with Visual FoxPro tables (ADS\_VFP) to create an index that can be used as a primary key and in referential integrity relationships.    ADS\_CUSTOM: Create an empty index order. The user can add and remove keys via AdsAddCustomKey and AdsDeleteCustomKey.    ADS\_BINARY\_INDEX: Create a [binary index](master_binary_indexes.htm). The index expression must have a logical result. This option cannot be combined with other options except for ADS\_COMPOUND.    ADS\_UCHAR\_KEY\_SHORT: When creating keys for a Unicode character column, the maximum key length in bytes will be roughly 2 times the column's code unit length.    ADS\_UCHAR\_KEY\_LONG: When creating keys for a Unicode character column, the maximum key length in bytes will be roughly 4 times the column's code unit length.    ADS\_UCHAR\_KEY\_XLONG: When creating keys for a Unicode character column, the maximum key length in bytes will be roughly 5 times the column's code unit length.    ADS\_ONLINE: Instruct the server to allow other users to access and update the table while the new index is being built.  See [Online Table Maintenance](master_online_table_maintenance.htm) for more information. |
| ulPageSize (I) | The page size to use when creating new indexes for tables of type ADS\_ADT. It is ignored for tables of type ADS\_NTX, ADS\_VFP and ADS\_CDX. Valid parameters are ADS\_DEFAULT, or any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If ADS\_DEFAULT is given, then Advantage will compute a page size based on the key size to provide for optimal balancing (see [Index Page Size](master_index_page_size.htm)). Note that this parameter is only used when creating a new index file. When this API is used to create additional index orders in an existing index file, then this parameter is ignored. Refer to [Index Page Size](master_index_page_size.htm) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.htm) for more information. |
| pucCollation (I) | An optional collation language used for this index order. The collation may be specified for ANSI/OEM characters, Unicode characters or both. Unicode collation name must be pre-pended with a single colon character. If both ANSI/OEM collation and Unicode collation are to be specified, the Unicode collation must be specified after the ANSI/OEM collation. For example: Duden\_DE\_ADS\_CS\_AS\_1252:de\_DE. This parameter is optional. If it is not specified, the collation specified for the table will be used when creating the index. For ADS\_CDX and ADS\_NTX tables, the ANSI/OEM collation must not be specified in the parameter. |
| phIndex (O) | Return handle of new index order if successful. |

Remarks

AdsCreateIndex creates an index order list of sorted keys in the table the order is based on, referenced by the index key expression. The index key expression and "for" and "while" expression can be any expression supported by the Advantage Expression Engine.

AdsCreateIndex will replace existing indexes of the same filename if one exists.

The UNIQUE property of indexes is very different between DBF and ADT table types. With DBFs, an index order created with the UNIQUE property will only include records that are referenced by unique values. If two records result in the identical key value, then only one of the records will be referenced by the index. The second is simply never added, and no error is reported. This is the traditional Xbase behavior of the UNIQUE property.

With ADTs, an index order created with the UNIQUE property enforces all records in the table to be referenced via a unique key. When creating the index order, if a record is found that would cause a non-unique key to be placed in the index, an error will be logged in the Advantage error log. That error log entry will indicate the record number, the tag name, and the index name associated with the non-unique index value. Up to fifty of these unique key violations will be logged before the index creation will be aborted. If any records are not unique, an error will be returned, and the index will not be usable. If a unique index is successfully created, and a new record is inserted or updated in which the key produced from the record is not unique, an error will be returned and the record update will not be allowed. At that point, the record must be modified such that the key produced is unique. If the record change is not desired or possible, either the AdsCancelUpdate or AdsCloseTable API must be called to cancel the update of the record. Note that the AdsLookupKey API may be used to predetermine that a key is unique.

If you are using Visual FoxPro tables (table type ADS\_VFP), then you can use the ADS\_CANDIDATE option when creating the index. It provides the same unique behavior as the ADS\_UNIQUE option on ADT tables. With ADS\_ADT tables, the ADS\_CANDIDATE and ADS\_UNIQUE options are equivalent.

Subindexes are indexes built on the keys in another index, rather than all the records in a table. The index from which a subindex is created is usually a conditional index. This allows for a subset of the records in a table to be built into a new index.

Custom indexes can only be built on tables opened with the ADS\_CDX or ADS\_ADT option.

If a cursor handle is passed to this function, the index is considered to be a temporary index and is deleted when the cursor is closed.

Note Subindexes obey all current filters, but do not obey all scopes. Reindexing a subindex will create a complete index that is based on all records in the table, not a subindex. Care should be taken when using subindexes rather than traditional record filters or Advantage Optimized Filters (AOFs) to view a subset of table. Though there may be legitimate reasons to use subindexes, most filtering can be accomplished with the same or better performance by using Advantage Optimized Filters (AOFs).

 

Note The maximum index key length is 4082 bytes for ADI indexes, 240 bytes for CDX and IDX indexes, and 256 bytes for NTX indexes. See [Xbase File Format Specifications](master_xbase_file_format_specifications.htm) and [Advantage Proprietary File Format Specifications](master_advantage_proprietary_file_format_specifications.htm) for more information. Also refer to [Index Page Size](master_index_page_size.htm) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.htm) for more information about the relationship between key sizes and index page sizes.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

 

Important! Do NOT attempt to create a new index or tag of the same name as the current index or tag. Using the same name will cause the pre-existing index to be deleted. If the index was a tag, it will be deleted but not removed from the file and the new index will take its place. Reindex to remove deleted tags.

Using AdsCreateIndex with an SQL Result Set

An index may be used on an SQL result set. The index created with AdsCreateIndex is on the new result set that is temporary, not on the original source table/tables that were queried to build the result set.

An error 5019 will occur if the second parameter, pucFileName, is null which indicates an index is being added to the auto-open index. Therefore, the pucFileName must not be null - a new filename for the index must be specified. After calling AdsCreateIndex, the new index file is open and ready for use.

For single table result sets, indexes that exist for the original table may be used after obtaining the result set. Therefore, it would not be necessary to use AdsCreateIndex on the result set if the index already exists for the original source table. If AdsCreateTable is used on a single table result set, tag names must be unique to the new temporary index as well as the auto-open index of the original source table.

Using AdsCreateIndex with Database Tables

When using AdsCreateIndex with [database tables](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)), the behavior of this API changes depending on the capability of the user who opened the table.

If the user is the ADSSYS user, the newly created index becomes part of the database. It will be automatically available to all users accessing the table.

If the user is not the ADSSYS user, the newly created index is temporary and it is automatically deleted when the table is closed. Since the index is temporary, the second parameter, pucFileName, cannot be NULL when calling this API. Otherwise a 5019 error will occur because the index cannot be added into the auto-open index file.

 

AdsCreateIndex61 is the same as AdsCreateIndex except for the additional ulPageSize parameter, which allows you to specify the page size of the new index file.

 

AdsCreateIndex90 is the same as AdsCreateIndex61 except for the additional pucCollation parameter, which provides for the capability to create an index file on a specific [dynamic collation](master_collation_support.htm) that differs from the tables current collation.

When indexing Unicode character columns, one of the ADS\_UCHAR\_KEY\_???? options may be specified to modify the maximum key length for the Unicode character column. If none of the options are specified, the default maximum key length is roughly 3 times the column's code unit length. If the column contains values that would result in keys longer than the maximum key size, those keys will be truncated to the maximum length.

Indexing Unicode character data is not supported with NTX indexes.

Examples

Create NTX index order (the table type of hTable must be ADS\_NTX):

AdsCreateIndex( hTable, "x:\path\new.ntx", NULL,

"lastname+firstname", "lastname<'C'", NULL,

ADS\_DEFAULT, &hIndex );

Create IDX index order (the table type of hTable must be ADS\_CDX):

AdsCreateIndex( hTable, "x:\path\new.idx", NULL,

"lastname+firstname", "lastname<'C'", NULL

ADS\_DEFAULT, &hIndex );

Create ADI index order with the tag name of "new" (the table type of hTable must be ADS\_ADT):

AdsCreateIndex( hTable, "x:\path\new.adt", NULL,

"lastname+firstname", "lastname<'C'", NULL

ADS\_DEFAULT, &hIndex );

Create either IDX, NTX, or ADI with a tag named "myindex" depending on the driver type:

AdsCreateIndex( hTable, "myindex", NULL,

"lastname+firstname", NULL, NULL, ADS\_DEFAULT,

&hIndex );

Create a compound index order when using table type ADS\_CDX or ADS\_ADT:

AdsCreateIndex( hTable, "x:\path\new", "tag1",

"lastname+firstname", NULL, NULL, ADS\_COMPOUND,

&hIndex );

Create a descending compound AutoOpen (structural) index order when using table type ADS\_CDX or ADS\_ADT:

AdsCreateIndex( hTable, NULL, "tag2", "lastname+firstname",

NULL, NULL, ADS\_COMPOUND | ADS\_DESCENDING,

&hIndex );

Create a Subindex using a WHILE expression from a CDX index:

/\* Create a "normal" index on the lastname field \*/

AdsCreateIndex( hTable, NULL, "TAG1", "lastname",

NULL, NULL, ADS\_COMPOUND ,

&hIndex1 );

 

/\* Position to the first "Miller" in the lastname index \*/

AdsSeek ( hIndex1, "Miller", 6, ADS\_STRINGKEY,

ADS\_SOFTSEEK, &bFound );

 

/\*

\* Create a While Subindex that contains only the "Miller"s. The index is

\* built on the "DateOfHire" field. Since this index contains a while

\* expression, the creation of the index will start at the current record

\* instead of the top of the file. And since a controlling index was

\* specified in the first parameter, this will result in a subindex that

\* will read those records referenced by that controlling index. Thus,

\* the index will get created starting with the first "Miller" in the controlling

\* index and will contain all "Miller" records until it reaches a record in

\* the controlling index that is not "Miller". By using the following code,

\* the index creation will be fast because only the "Miller" records are

\* considered for the index. This index should probably be used as

\* a temporary index only due to the nature of While indexes and

\* Subindexes.

\*/

AdsCreateIndex( &hIndex1, "subIndex", "TAG1", "DateOfHire",

NULL, "lastname = \"Miller\"", ADS\_COMPOUND,

&hIndex2 );

 

/\*

\* Now use the new index to build another subindex, but limit the

\* keys to contain only those records where the first name is "John".

\* This type of operation might be useful if you need to build several

\* different indexes where only the "Miller" keys are to be considered

\* for the index.

\*/

AdsCreateIndex( &hIndex2, "subIndex", "TAG2", "DateOfHire",

"firstname = \"John\"", NULL, ADS\_COMPOUND,

&hIndex3 );

 

/

\* Care should be taken when using subindexes rather than

\* traditional record filters or Advantage Optimized Filters (AOFs)

\* to view a subset of table. Though there may be legitimate

\* reasons to use subindexes, most filtering can be accomplished

\* with the same or better performance by using AOFs.

\*/

 

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCloseIndex](ace_adscloseindex.htm)

[AdsReindex](ace_adsreindex.htm)

[AdsReindex61](ace_adsreindex61.htm)

[AdsConnect60](ace_adsconnect60.htm)

[AdsCreateFTSIndex](ace_adscreateftsindex.htm)

[Dynamic Collation Support](master_collation_support.htm)

[sp\_GetCollations](master_sp_getcollations.htm)