AdsGetAOF




Advantage Database Server 12  

AdsGetAOF / AdsGetAOF100

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetAOF / AdsGetAOF100  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetAOF / AdsGetAOF100 Advantage Client Engine ace\_Adsgetaof Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetAOF / AdsGetAOF100  Advantage Client Engine |  |  |  |  |

Retrieve the AOF expression that was used in the call to AdsSetAOF or AdsSetAOF100.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetAOF ( ADSHANDLE hTable,             UNSIGNED8 \*pucFilter,             UNSIGNED16 \*pusLen ); |
| UNSIGNED32 | AdsGetAOF100( ADSHANDLE hTable,               UNSIGNED32 ulOptions,               VOID       \*pvFilter,               UNSIGNED32 \*pulLen ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table or cursor with an AOF. |
| pucFilter (O) | Return the ANSI/OEM encoded filter expression in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |
| ulOptions (I) | Options to determine how the filter expression should be returned. Available options are:    ADS\_ENCODE\_UTF8: Return the filter expression as UTF8 encoded Unicode character string. The size of a character is a single byte.    ADS\_ENCODE\_UTF16: Return the filter expression as UTF-16LE encoded Unicode character string. The size of a character is 2 bytes (16 bits).    If neither of the encoding option is specified, the filter expression is returned as code page encoded ANSI/OEM string. The size of a character is a single byte. |
| pvFilter (O) | Returns the filter expression in this buffer. The encoding of returned filter expression will be determined by the ulOptions. |
| pulLen (I/O) | Number of characters of given buffer on input, number of characters of returned data on output. The size of character depends on the encoding option specified by ulOptions. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_UNICODE\_CONVERSION | If the AOF has Unicode data and the ANSI/OEM code page string is the requested encoding type, this error will be returned when there are Unicode character that cannot be converted in to the code page encoded character. |

Remarks

Retrieves the AOF expression that was used in the call to AdsSetAOF or AdsSetAOF100. For more information, see [Advantage Optimized Filters](master_advantage_optimized_filters.htm).

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsgetaof_example)

See Also

[AdsSetAOF](ace_adssetaof.htm)

[AdsSetAOF100](ace_adssetaof.htm)

[AdsRefreshAOF](ace_adsrefreshaof.htm)

[AdsGetAOFOptLevel](ace_adsgetaofoptlevel.htm)

[AdsGetAOFOptLevel100](ace_adsgetaofoptlevel.htm)