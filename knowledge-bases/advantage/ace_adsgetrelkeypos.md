AdsGetRelKeyPos




Advantage Database Server 12  

AdsGetRelKeyPos

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetRelKeyPos  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetRelKeyPos Advantage Client Engine ace\_Adsgetrelkeypos Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetRelKeyPos  Advantage Client Engine |  |  |  |  |

Returns the relative position of the current record in the given index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetRelKeyPos (ADSHANDLE hIndex, DOUBLE \*pdPos); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order. |
| pdPos (O) | Return relative position. The value will be between 0.0 and 1.0 inclusive. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NOT\_FOUND | The desired index key was not found. It may not exist. |

Remarks

AdsGetRelKeyPos returns an estimation of the position in the current key in the indicated index order. The value returned will be between 0.0 and 1.0, inclusive. If there are scopes set on the index order, the position returned will be relative to the visible records.

Example

[Click Here](ace_examples.htm#adsgetrelkeyposexample)

See Also

[AdsSetRelKeyPos](ace_adssetrelkeypos.htm)

[AdsGetKeyNum](ace_adsgetkeynum.htm)

[AdsGetKeyCount](ace_adsgetkeycount.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)