AdsDeleteCustomKey




Advantage Database Server 12  

AdsDeleteCustomKey

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDeleteCustomKey  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDeleteCustomKey Advantage Client Engine ace\_Adsdeletecustomkey Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDeleteCustomKey  Advantage Client Engine |  |  |  |  |

Removes the key built from the current record from the custom index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsDeleteCustomKey (ADSHANDLE hIndex); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order that was created with the ADS\_CUSTOM option. |

Remarks

AdsDeleteCustomKey will remove the key corresponding to the current record from the custom index order. If a key for this record was not added to the index, AdsDeleteCustomKey will return AE\_SUCCESS.

Note When the index is shared, deleting a custom key will fail if the record is locked by another application. If the index is opened exclusively, custom keys can be deleted even when the record is locked by another application. To open an index exclusively, open the table exclusively or open the table in shared mode and create a custom index without closing it.

Example

[Click Here](ace_examples.htm#adsdeletecustomkeyexample)

See Also

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsAddCustomKey](ace_adsaddcustomkey.htm)

[AdsIsIndexCustom](ace_adsisindexcustom.htm)

[AdsAtEOF](ace_adsateof.htm)