AdsGetKeyLength




Advantage Database Server 12  

AdsGetKeyLength

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetKeyLength  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetKeyLength Advantage Client Engine ace\_Adsgetkeylength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetKeyLength  Advantage Client Engine |  |  |  |  |

Retrieves the key size in bytes of the given index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetKeyLength (ADSHANDLE hIndex,  UNSIGNED16 \*pusKeySize ); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of an index order. |
| pusKeySize (O) | Length in bytes of the index key. |

Remarks

Returns the number of bytes in each physical key in the index file. If the index key evaluates to a variable-length expression, this function will return zero for the length.

Example

None.

See Also

[AdsExtractKey](ace_adsextractkey.htm)

[AdsGetKeyType](ace_adsgetkeytype.htm)