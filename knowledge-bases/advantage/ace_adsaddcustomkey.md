AdsAddCustomKey




Advantage Database Server 12  

AdsAddCustomKey

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsAddCustomKey  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsAddCustomKey Advantage Client Engine ace\_Adsaddcustomkey Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsAddCustomKey  Advantage Client Engine |  |  |  |  |

Adds a key built on the current record to the custom index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsAddCustomKey (ADSHANDLE hIndex); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order that was created with the ADS\_CUSTOM option. |

Remarks

Custom indexes are empty when created and require keys to be explicitly added and removed. AdsAddCustomKey will add a key based on the current record to the custom index order. This key will be updated if the values in the record change.

Custom indexes can only be built on tables opened with the ADS\_CDX or ADS\_ADT option.

Note When the index is shared, adding a custom key will fail if the record is locked by another application. If the index is opened exclusively, custom keys can be added even when the record is locked by another application. To open an index exclusively, open the table exclusively or open the table in shared mode and create a custom index without closing it.

Example

[Click Here](ace_examples.htm#adsaddcustomkeyexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsIsIndexCustom](ace_adsisindexcustom.htm)

[AdsDeleteCustomKey](ace_adsdeletecustomkey.htm)

[AdsAtEOF](ace_adsateof.htm)