AdsIsIndexCandidate




Advantage Database Server 12  

AdsIsIndexCandidate

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsIndexCandidate  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsIndexCandidate Advantage Client Engine ace\_Adsisindexcandidate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsIndexCandidate  Advantage Client Engine |  |  |  |  |

Determines if the given index order is a candidate index.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsIndexCandidate ( ADSHANDLE hIndex,  UNSIGNED16 \*pbCandidate ); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest. |
| pbCandidate (O) | Return True if it is a candidate index. |

Remarks

AdsIsIndexCandidate returns whether or not an index order was created with the ADS\_CANDIDATE option.

Note AdsIsIndexCandidate can only be called on indexes of ADS\_ADT or ADS\_VFP tables.

Example

ulRetCode = AdsIsIndexCandidate( hIndex, &usCandidate );

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsIsIndexUnique](ace_adsisindexunique.htm)