AdsSetIndexDirection




Advantage Database Server 12  

AdsSetIndexDirection

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetIndexDirection  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetIndexDirection Advantage Client Engine ace\_Adssetindexdirection Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetIndexDirection  Advantage Client Engine |  |  |  |  |

Reverses the DESCEND flag on an index.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetIndexDirection( ADSHANDLE hIndex,  UNSIGNED16 usReverseDirection ); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order. |
| usReverseDirection (I) | If FALSE (0) the original state of the DESCEND flag is restored. If TRUE (1) the DESCEND flag is flipped for the index. |

Remarks

The DESCEND flag of the index is flipped when usReverseDirection is TRUE. The index is then traversed in the opposite direction. Any scopes on the index must be reset because the top and bottom key have been reversed.

This option is not supported for ADS\_NTX indexes.

Example

ulRetCode = AdsSetIndexDirection( hIndex2, 1 );

See Also

[AdsSkip](ace_adsskip.htm)

[AdsGetRecordCount](ace_adsgetrecordcount.htm)

[AdsGetRecordNum](ace_adsgetrecordnum.htm)

[AdsGotoBottom](ace_adsgotobottom.htm)

[AdsGotoRecord](ace_adsgotorecord.htm)

[AdsGotoTop](ace_adsgototop.htm)

[AdsAtBOF](ace_adsatbof.htm)

AdsAtEOF