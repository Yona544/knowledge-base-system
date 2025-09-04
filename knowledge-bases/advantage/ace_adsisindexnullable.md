AdsIsIndexNullable




Advantage Database Server 12  

AdsIsIndexNullable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsIndexNullable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsIndexNullable Advantage Client Engine ace\_Adsisindexnullable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsIndexNullable  Advantage Client Engine |  |  |  |  |

Determines if the given index order is nullable.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsIndexNullable ( ADSHANDLE hIndex,  UNSIGNED16 \*pbNullable ); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest. |
| pbNullable (O) | Return True if it is a nullable index. |

Remarks

AdsIsNullable determines whether or not an index order was created on a nullable key. A nullable key is one that can evaluate to NULL.

Note AdsIsIndexNullable can only be called on indexes of ADS\_VFP tables.

Example

ulRetCode = AdsIsIndexNullable( hIndex, &usNullable );

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCreateIndex](ace_adscreateindex.htm)