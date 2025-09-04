AdsCreateFTSIndex




Advantage Database Server 12  

AdsCreateFTSIndex

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsCreateFTSIndex  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsCreateFTSIndex Advantage Client Engine ace\_Adscreateftsindex Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsCreateFTSIndex  Advantage Client Engine |  |  |  |  |

Creates a new full text search index.

Syntax

UNSIGNED32 AdsCreateFTSIndex

(

ADSHANDLE hTable,

UNSIGNED8 \*pucFileName,

UNSIGNED8 \*pucTag,

UNSIGNED8 \*pucField,

UNSIGNED32 ulPageSize,

UNSIGNED32 ulMinWordLen,

UNSIGNED32 ulMaxWordLen,

UNSIGNED16 usUseDefaultDelim,

VOID \*pvDelimiters,

UNSIGNED16 usUseDefaultNoise,

VOID \*pvNoiseWords,

UNSIGNED16 usUseDefaultDrop,

VOID \*pvDropChars,

UNSIGNED16 usUseDefaultConditionals,

VOID \*pvConditionalChars,

UNSIGNED8 \*pucCollation,

UNSIGNED8 \*pucReserved,

UNSIGNED32 ulOptions

);

Parameters

For detailed descriptions of how the various parameters affect full text search indexes, see the Index Options section of [Full Text Search](master_full_text_search_index_options_fts.htm).

|  |  |
| --- | --- |
| hTable (I) | Handle of the table on which to create the full text search index. |
| pucFileName (I) | Name of file for new index order. If this is NULL or if the base name is the same as the table, then a compound AutoOpen index file for hTable will be created/updated. If no path is given, the index will be created in the same directory as the table. |
| pucTag (I) | Name of the new index tag. |
| pucField (I) | The field on which the full text search index is to be created. The allowed field types include character, cicharacter, memo, binary, image, raw, and varchar. |
| ulPageSize (I) | The page size to use when creating new indexes for tables of type ADS\_ADT. It is ignored for tables of type ADS\_CDX and ADS\_VFP. Valid parameters are ADS\_DEFAULT, or any numeric value in the range ADS\_MIN\_ADI\_PAGESIZE to ADS\_MAX\_ADI\_PAGESIZE. If ADS\_DEFAULT is given, then a page size of 1024 bytes will be used. Note that this parameter is only used when creating a new index file. When this API is used to create additional index orders in an existing index file, then this parameter is ignored. See [Index Page Size](master_index_page_size.htm) for more information. |
| ulMinWordLen (I) | The minimum word length to store in the index. Words shorter than this length will not be in the index. |
| ulMaxWordLen (I) | The maximum word length to store in the index. Words that are longer than this will be stored in the index in a truncated form. Searches for words longer than the maximum length will require some post-processing of the data. See the description of this option in [Full Text Search](master_full_text_search_index_options_fts.htm). |
| usUseDefaultDelim (I) | If non-zero (TRUE), the default delimiters will be used as part of the delimiter set. |
| pvDelimiters (I) | Optional null terminated string of delimiter characters. If usUseDefaultDelim is TRUE, then these delimiters will be used in addition to the default delimiters. This parameter can be NULL or an empty string.The string may be encoded using code page encoding, UTF8 encoding or UTF16 encoding depending on the option bits specified in ulOptions parameter. |
| usUseDefaultNoise (I) | If non-zero (TRUE), use the default noise word list. |
| pvNoiseWords (I) | Optional null terminated string of space-delimited noise words. If usUseDefaultNoise is TRUE, then these noise words will be used in addition to the default noise words. This parameter can be NULL or an empty string. The string may be encoded using code page encoding, UTF8 encoding or UTF16 encoding depending on the option bits specified in ulOptions parameter. |
| usUseDefaultDrop (I) | If non-zero (TRUE), use default drop characters. |
| pvDropChars (I) | Optional null terminated string of drop characters. If usUseDefaultDrop is TRUE, then these drop characters will be used in addition to the default drop characters. This parameter can be NULL or an empty string. The string may be encoded using code page encoding, UTF8 encoding or UTF16 encoding depending on the option bits specified in ulOptions parameter. |
| usUseDefaultConditionals (I) | If non-zero (TRUE), use default conditional drop characters. |
| pvConditionalChars (I) | Optional null terminated string of conditional drop characters. If usUseDefaultConditionals is TRUE, then these conditional drop characters will be used in addition to the default conditional drop characters. This parameter can be NULL or an empty string. The string may be encoded using code page encoding, UTF8 encoding or UTF16 encoding depending on the option bits specified in ulOptions parameter. |
| pucCollation (I) | An optional collation language used when creating index. This parameter is optional for ADS\_ADT and ADS\_VFP tables, but must be NULL or empty for ADS\_CDX tables. This allows the index to be created with a collation different from the one currently active on the table. See [dynamic collation support](master_collation_support.htm). |
| pucReserved (I) | Reserved for future use. Pass NULL for this value. |
| ulOptions (I) | A bit field for defining the options for full text search index creation. The options can be ORed together into the bit field. See [Full Text Search](master_full_text_search_index_options_fts.htm) for details on the options. The options are:  ADS\_DEFAULT: If no options are needed, this constant (0) can be used.  ADS\_COMPOUND: Create an index order (tag) within a compound index file. Note that this option is set automatically when the table type is ADS\_ADT.  ADS\_FTS\_FIXED: Create an FTS index that is not maintained by Advantage.  ADS\_FTS\_CASE\_SENSITIVE: Create a case-sensitive FTS index. This options is ignored when the field contains Unicode data. FTS index created on Unicode field types is always case insensitive and diacritical insensitive.  ADS\_FTS\_KEEP\_SCORE: Track word counts in the index for the SCORE() scalar function.  ADS\_FTS\_PROTECT\_NUMBERS: Do not treat commas and periods as delimiters when they appear in numbers (digits 0-9).  ADS\_FTS\_ENCODE\_UTF8: The string supplied to pvDelimiters, pvNoiseWords, pvDropChars, and pvConditionalChars are encoded in UTF8.  ADS\_FTS\_ENCODE\_UTF16: The string supplied to pvDelimiters, pvNoiseWords, pvDropChars, and pvConditionalChars are encoded in UTF16.  If neither ADS\_FTS\_ENCODE\_UTF8 nor ADS\_FTS\_ENCODE\_UTF16 is specified, the pvDelimiters, pvNoiseWords, pvDropChars, and pvConditionalChars are expected to be encoded using the current system code page.  ADS\_ONLINE: Instruct the server to allow other users to access and update the table while the new index is being built.  See [Online Table Maintenance](master_online_table_maintenance.htm) for more information. |

Remarks

This API is only valid for table types ADS\_ADT, ADS\_VFP, and ADS\_CDX. Full text search indexes cannot be created on tables of type ADS\_NTX.

This API does not return the handle of the newly created index to the caller. It is possible to retrieve the index handle, however, FTS index handles cannot be used with most APIs. For example, it is not possible to use them for table positioning via AdsGotoTop, AdsSkip, etc. FTS indexes are used automatically when the CONTAINS() scalar function is used in filters and SQL WHERE clauses.

For a full description of FTS indexes, see [Full Text Search](master_full_text_search_index_options_fts.htm).

Notes on Unicode FTS Index

FTS index created on Unicode field contains only the primary weight of the key so FTS search on Unicode data is always case insensitive and diacritical difference insensitive. This affects both filter and AOF operations.

The delimiters, drop characters, and conditional drop characters, when specified, are normalized to NFC (Normalization Form Canonical Composition) before being used to tokenize the words from the text. And the text being tokenized is also normalized to NFC form before being tokenized. If the text stored in the table is already in NFC form, then no transformation is needed before tokenization and it can result in slightly improvement in performance.

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsReindexFTS](ace_adsreindexfts.htm)

[AdsGetNumFTSIndexes](ace_adsgetnumftsindexes.htm)

[AdsGetFTSIndexes](ace_adsgetftsindexes.htm)

[AdsGetFTSIndexInfo](ace_adsgetftsindexinfo.htm)

[AdsIsIndexFTS](ace_adsisindexfts.htm)