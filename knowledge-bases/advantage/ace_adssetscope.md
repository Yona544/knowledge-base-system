AdsSetScope




Advantage Database Server 12  

AdsSetScope

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetScope  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetScope Advantage Client Engine ace\_Adssetscope Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetScope  Advantage Client Engine |  |  |  |  |

Sets a scope for the given index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetScope (ADSHANDLE hIndex,  UNSIGNED16 usScopeOption,  UNSIGNED8 \*pucScope,  UNSIGNED16 usScopeLen  UNSIGNED16 usDataType); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order. |
| usScopeOption (I) | Indicates which scope value to set. Options are ADS\_TOP and ADS\_BOTTOM. |
| pucScope (I) | Scope value to set. |
| usScopeLen (I) | Length of scope value. |
| usDataType (I) | Indicates type of data given in pucKey. ADS\_RAWKEY indicates that the key is given exactly as needed for seek. No conversion is performed. ADS\_STRINGKEY indicates the data is in a character string (numeric date, and ANSI/OEM conversions performed as necessary. ADS\_DOUBLEKEY indicates that the data is a pointer to an 8-byte floating-point value. ADS\_WSTRINGKEY indicates that the data is a pointer to a UTF16 encoded string and the usKeyLen is the number of bytes (not the number of characters) in the string. |

Remarks

AdsSetScope sets a scope for the index to limit the number of records visible. For example, setting a ADS\_TOP scope of "M" on a index on a character field will make an [AdsGotoTop](ace_adsgototop.htm) call on this index go to the first key greater than or equal to "M". An ADS\_BOTTOM scope will make the indicated value the last one visible in the index order. For example, if AdsSetScope is called with ADS\_BOTTOM and "Smith" on a lastname index, the last Smith on an [AdsGotoBottom](ace_adsgotobottom.htm) call will be the current record. Set the scope for top and bottom to the same value to view only those records with the given scope value from the index.

It is not necessary to have both top and bottom scopes set at the same time. The Advantage Client Engine does not check that the ADS\_TOP and ADS\_BOTTOM scopes are not mutually exclusive. When setting scopes on descending indexes, the ADS\_TOP scope will be set at the logical top of the index (largest key) and the ADS\_BOTTOM is at the logical bottom (smallest key).

To set a scope using indexes built on date, time, or timestamp fields, it is simplest to pass the scope value as a string (ADS\_STRINGKEY). The date should be formatted according the current date mask ([AdsSetDateFormat](ace_adssetdateformat.htm)). For example, to set a scope on a date index, an application might pass "2/25/1997" as the value. To set a scope on a timestamp index, the value could be "2/25/1997 3:25pm". An application can use a double (ADS\_DOUBLEKEY) to set a scope on date and time indexes; the value for a date index must be passed as a Julian date, and the value for a time index must be passed as milliseconds since midnight.

Note To perform a prefix scope on a Unicode column (NCHAR or NVARCHAR), for example, searching for rows with the column having prefix of "A", AdsBuildRawKey100 with the ADS\_GET\_PRIMARY\_WEIGHT\_LENGTH option must be used to retrieve the raw binary key of the prefix to use in the AdsSetScope.

Note If both a narrow scope and a narrow filter (narrow meaning that very few records match the scope or filter conditions) are being used on the same table, poor performance may result. Since knowledge of scopes is only on the client, and filters are handled on the server, the filtering of records on the server may unnecessarily traverse well beyond the bounds of a scope, causing poor performance. If this condition is expected, it is recommended to use either a scope or a filter, but not both.

Example

[Click Here](ace_examples.htm#adssetscopeexample)

See Also

[AdsClearScope](ace_adsclearscope.htm)

[AdsGetScope](ace_adsgetscope.htm)

[AdsSeek](ace_adsseek.htm)

[AdsSkip](ace_adsskip.htm)

[AdsGotoTop](ace_adsgototop.htm)

[AdsGotoBottom](ace_adsgotobottom.htm)

[AdsClearAllScopes](ace_adsclearallscopes.htm)

[AdsInitRawKey](ace_adsinitrawkey.htm)

[AdsBuildRawKey](ace_adsbuildrawkey.htm)

[AdsBuildRawKey100](ace_adsbuildrawkey.htm)