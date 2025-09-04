AdsCreateIndex90




Advantage Database Server 12  

AdsCreateIndex90

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCreateIndex90  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCreateIndex90 Advantage Client Engine ace\_Adscreateindex90 Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCreateIndex90  Advantage Client Engine |  |  |  |  |

Creates a new index order for the given table.

Syntax

|  |  |
| --- | --- |
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
| ulOptions (I) | A bit field for defining the options for index creation. The options can be ORed together into the bit field. For example ADS\_COMPOUND | ADS\_UNIQUE. The options are:    ADS\_DEFAULT: If no options are needed, this constant (0) can be used.    ADS\_COMPOUND: Create an index order (tag) within a compound index file. Note that this option is always set when the table type is ADS\_ADT    ADS\_DESCENDING: Create a descending index order.    ADS\_UNIQUE: Create a unique index order.    ADS\_CANDIDATE: This creates a unique index order that prevents duplicate data. On ADT tables, it is the same as the ADS\_UNIQUE option. This can be used with Visual FoxPro tables (ADS\_VFP) to create an index that can be used as a primary key and in referential integrity relationships.    ADS\_CUSTOM: Create an empty index order. The user can add and remove keys via AdsAddCustomKey and AdsDeleteCustomKey.    ADS\_BINARY\_INDEX: Create a [binary index](master_binary_indexes.htm). The index expression must have a logical result. This option cannot be combined with other options except for ADS\_COMPOUND.    ADS\_UCHAR\_KEY\_SHORT: When creating keys for a Unicode character column, the maximum key length in bytes will be roughly 2 times the column's code unit length.    ADS\_UCHAR\_KEY\_LONG: When creating keys for a Unicode character column, the maximum key length in bytes will be roughly 4 times the column's code unit length.    ADS\_UCHAR\_KEY\_XLONG: When creating keys for a Unicode character column, the maximum key length in bytes will be roughly 5 times the column's code unit length. |
| ulPageSize (I) | The page size to use when creating new indexes for tables of type ADS\_ADT. It is ignored for tables of type ADS\_NTX, ADS\_VFP and ADS\_CDX. Valid parameters are ADS\_DEFAULT, or any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If ADS\_DEFAULT is given, then Advantage will compute a page size based on the key size to provide for optimal balancing (see [Index Page Size](master_index_page_size.htm)). Note that this parameter is only used when creating a new index file. When this API is used to create additional index orders in an existing index file, then this parameter is ignored. Refer to [Index Page Size](master_index_page_size.htm) and [Index Key Size and Page Size Relationships](master_index_key_size_and_page_size_relationships.htm) for more information. |
| pucCollation (I) | An optional collation language used for this index order. The collation may be specified for ANSI/OEM characters, Unicode characters or both. Unicode collation name must be pre-pended with a single colon character. If both ANSI/OEM collation and Unicode collation are to be specified, the Unicode collation must be specified after the ANSI/OEM collation. For example: Duden\_DE\_ADS\_CS\_AS\_1252:de\_DE. This parameter is optional. If it is not specified, the collation specified for the table will be used when creating the index. For ADS\_CDX and ADS\_NTX tables, the ANSI/OEM collation must not be specified in the parameter. |
| phIndex (O) | Return handle of new index order if successful. |

Remarks

AdsCreateIndex90 is the same as [AdsCreateIndex61](ace_adscreateindex61.htm) except for the additional pucCollation parameter, which provides for the capability to create an index file on a specific [dynamic collation](master_collation_support.htm) that differs from the tables current collation.

When indexing Unicode character columns, one of the ADS\_UCHAR\_KEY\_???? options may be specified to modify the maximum key length for the Unicode character column. If none of the options are specified, the default maximum key length is roughly 3 times the column's code unit length. If the column contains values that would result in keys longer than the maximum key size, those keys will be truncated to the maximum length.

Indexing Unicode character data is not supported with NTX indexes.

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCloseIndex](ace_adscloseindex.htm)

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsReindex](ace_adsreindex.htm)

[AdsReindex61](ace_adsreindex61.htm)

[AdsConnect60](ace_adsconnect60.htm)

[AdsCreateFTSIndex](ace_adscreateftsindex.htm)

[AdsCreateIndex61](ace_adscreateindex61.htm)

[Dynamic Collation Support](master_collation_support.htm)

[sp\_GetCollations](master_sp_getcollations.htm)