AdsGetAOFOptLevel




Advantage Database Server 12  

AdsGetAOFOptLevel / AdsGetAOFOptLevel100

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetAOFOptLevel / AdsGetAOFOptLevel100  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetAOFOptLevel / AdsGetAOFOptLevel100 Advantage Client Engine ace\_Adsgetaofoptlevel Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetAOFOptLevel / AdsGetAOFOptLevel100  Advantage Client Engine |  |  |  |  |

Return the optimization level of this AOF

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetAOFOptLevel ( ADSHANDLE hTable,                     UNSIGNED16 \*pusOptLevel,                     UNSIGNED8 \*pucNonOpt,                     UNSIGNED16 \*pusLen ); |
| UNSIGNED32 | AdsGetAOFOptLevel100( ADSHANDLE hTable,                       UNSIGNED16 \*pusOptLevel,                       VOID       \*pvNonOpt,                       UNSIGNED32 \*pulExprLen,                       UNSIGNED32 ulOptions ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table or cursor with an AOF. |
| pusOptLevel (O) | Return the optimization level for the AOF that is on the given table. Values are ADS\_OPTIMIZED\_FULL, ADS\_OPTIMIZED\_PART, ADS\_OPTIMIZED\_NONE. |
| pucNonOpt (O) | Return the non-optimized portion of the filter expression using ANSI/OEM code page encoding in this buffer. This parameter can be NULL if only the optimization level is desired. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |
| pvNonOpt (O) | Return the non-optimized portion of the filter expression in this buffer. The encoding of returned expression will be determined by the ulOptions. This parameter can be NULL if only the optimization level is desired. |
| pulExprLen (I/O) | Number of characters of given buffer on input, number of characters of returned data on output. The size of character depends on the encoding option specified by ulOptions. |
| ulOptions (I) | Options to determine how the filter expression should be returned. Available options are:    ADS\_ENCODE\_UTF8: Return the filter expression as UTF8 encoded Unicode character string. The size of a character is a single byte.    ADS\_ENCODE\_UTF16: Return the filter expression as UTF-16LE encoded Unicode character string. The size of a character is 2 bytes (16 bits).    If neither of the encoding option is specified, the filter expression is returned as code page encoded ANSI/OEM string. The size of a character is a single byte. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_UNICODE\_CONVERSION | If the AOF has Unicode data and the ANSI/OEM code page string is the requested encoding type, this error will be returned when there are Unicode character that cannot be converted in to the code page encoded character. |

Remarks

AdsGetAOFOptLevel and AdsGetAOFOptLevel100 return the optimization level of the AOF expression associated with the given handle. It also returns the portion of the expression that could not be optimized. For example, if a table has a single index built on 'LASTNAME', the filter expression "LASTNAME = 'James' .and. FIRSTNAME = 'Bob'" will be partially optimized. AdsGetAOFOptLevel and AdsGetAOFOptLevel100 would return ADS\_OPTIMIZED\_PART for this expression, and the non-optimized portion would be "FIRSTNAME='Bob'".

Note that the optimization level returned is not affected by the resolve option (ADS\_RESOLVE\_IMMEDIATE or ADS\_RESOLVE\_DYNAMIC) that is passed to [AdsSetAOF](ace_adssetaof.htm).

For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.htm).

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsgetaofoptlevel_example)

See Also

[AdsSetAOF](ace_adssetaof.htm)

[AdsSetAOF100](ace_adssetaof.htm)

[AdsRefreshAOF](ace_adsrefreshaof.htm)

[AdsGetAOF](ace_adsgetaof.htm)

[AdsGetAOF100](ace_adsgetaof.htm)