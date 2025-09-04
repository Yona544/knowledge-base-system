AdsSeek




Advantage Database Server 12  

AdsSeek

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSeek  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSeek Advantage Client Engine ace\_Adsseek Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSeek  Advantage Client Engine |  |  |  |  |

Performs an indexed search on the given table using the given index order. Scopes and filters are respected.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSeek (ADSHANDLE hIndex,  UNSIGNED8 \*pucKey,  UNSIGNED16 usKeyLen,  UNSIGNED16 usDataType,  UNSIGNED16 usSeekType,  UNSIGNED16 \*pbFound); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order. |
| pucKey (I) | Search key (not necessarily a null terminated string). |
| usKeyLen (I) | Length of search key. |
| usDataType (I) | Indicates type of data given in pucKey. ADS\_RAWKEY indicates the key is given exactly as needed for seek. No conversion is performed. ADS\_STRINGKEY indicates the data is in a character string and numeric, date, and ANSI/OEM conversions will be performed as necessary. ADS\_DOUBLEKEY indicates that the data is a pointer to an 8-byte floating-point value. ADS\_WSTRINGKEY indicates that the data is a pointer to a UTF16 encoded string and the usKeyLen is the number of bytes (not the number of characters) in the string. |
| usSeekType (I) | Indicates if hard or soft seek is performed. Options are ADS\_SOFTSEEK, ADS\_HARDSEEK, or ADS\_SEEKGT. Use of soft seek allows a record to be found with the next higher key value if the given key does not exist. |
| pbFound (O) | Return True if record found. |

Remarks

AdsSeek provides the fastest way for the Advantage Database Server to locate a record. The pucKey parameter is used by the Advantage Client Engine to build a seekable index key for the server to seek through the indicated index for a matching key. The Advantage Client Engine converts pucKey according to the usDataType parameter. If usDataType is ADS\_STRINGKEY or ADS\_WSTRINGKEY, the Advantage Client Engine converts pucKey from a character string to a seek key. When ADS\_DOUBLEKEY is specified, the Advantage Client Engine converts pucKey from a double to a key. ADS\_DOUBLEKEY can be used for numeric seeks or date seeks. If using ADS\_DOUBLEKEY for date seeks, the numeric value should represent a Julian date. Be sure to send usKeyLen of 8 if ADS\_DOUBLEKEY is indicated. If ADS\_RAWKEY is indicated, the Advantage Client Engine tries to seek on the exact data that the caller passes to the function. ADS\_RAWKEY is generally only useful when used in conjunction with the AdsBuildRawKey function unless you know the exact format of the index key.

To seek for records using indexes built on date, time, or timestamp fields, it is simplest to pass the seek key as a string (ADS\_STRINGKEY). The date should be formatted according the current date mask ([AdsSetDateFormat](ace_adssetdateformat.htm)). For example, to seek on a date index, an application might pass "2/25/1997" as the seek key. To seek on a timestamp index, the seek key could be "2/25/1997 3:25pm". An application can use a double (ADS\_DOUBLEKEY) to seek on date and time indexes; the value for a date index must be passed as a Julian date, and the value for a time index must be passed as milliseconds since midnight.

By sending ADS\_SOFTSEEK for the usSeekType parameter, the Advantage Client Engine will perform a "soft" seek, which means that if the desired key is not found in the index, the table will be positioned at the first key logically greater than the seek key. On an ADS\_HARDSEEK, if the desired key is not found, the table is positioned at EOF. When ADS\_SEEKGT is indicated, a "soft" seek will be performed on the key that is the next possible index key after the key sent in the pucKey parameter. If ADS\_SEEKGT is used and any key is found, pbFound returns True.

On a seek that is successful, the pbFound parameter passed back will be True. If the seek fails, pbFound will be false. On a "soft" seek, the pbFound flag will be True when the specified key is found. If the specified key is not found on a "soft" seek, the pbFound flag will be False. The length of the search key (usKeyLen) defines the length of the key matching performed during the seek operation. For example, a seek key of "A" will find the first record whose index key starts with "A", and the found flag will be set to True if it finds such a record regardless of whether it is a "soft" seek or not. A zero length search key is defined to match all index keys and will go to the same record as would a call to [AdsGotoTop](ace_adsgototop.htm) with the index handle hIndex.

Example

[Click Here](ace_examples.htm#adsseekexample)

See Also

[AdsSkip](ace_adsskip.htm)

[AdsClearScope](ace_adsclearscope.htm)

[AdsGetScope](ace_adsgetscope.htm)

[AdsSetScope](ace_adssetscope.htm)

[AdsIsFound](ace_adsisfound.htm)

[AdsAtEOF](ace_adsateof.htm)

[AdsLookupKey](ace_adslookupkey.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)