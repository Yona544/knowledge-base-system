AdsIsIndexCustom




Advantage Database Server 12  

AdsIsIndexCustom

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsIndexCustom  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsIndexCustom Advantage Client Engine ace\_Adsisindexcustom Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsIndexCustom  Advantage Client Engine |  |  |  |  |

Determines if the given index order was built as a custom index.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsIndexCustom (ADSHANDLE hIndex,  UNSIGNED16 \*pbCustom); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest. |
| pbCustom (O) | Return True if it is a custom index order. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_INVALID\_INDEX\_TYPE | NTX indexes cannot be custom. |

Remarks

A custom index is built without keys. Keys are added to the custom index explicitly by calls to [AdsAddCustomKey](ace_adsaddcustomkey.htm) and [AdsDeleteCustomKey](ace_adsdeletecustomkey.htm). This allows a user to build a very small and specific index.

Custom indexes can only be built on tables opened with the ADS\_CDX or ADS\_ADT option.

Example

[Click Here](ace_examples.htm#adsisindexcustomexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsAddCustomKey](ace_adsaddcustomkey.htm)

[AdsDeleteCustomKey](ace_adsdeletecustomkey.htm)