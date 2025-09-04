AdsGetIndexHandleByExpr




Advantage Database Server 12  

AdsGetIndexHandleByExpr

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetIndexHandleByExpr  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetIndexHandleByExpr Advantage Client Engine ace\_Adsgetindexhandlebyexpr Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetIndexHandleByExpr  Advantage Client Engine |  |  |  |  |

Retrieves the index handle given the indexs expression

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetIndexHandleByExpr( ADSHANDLE hTbl,  UNSIGNED8\*pucExpr,  UNSIGNED32 ulDescending,  ADSHANDLE \*phIndex ) |

Parameters

|  |  |
| --- | --- |
| hTbl (I) | Handle of a table. |
| pucExpr (I) | Expression to retrieve index handle for. |
| ulDescending (I) | ADS\_ASCENDING or ADS\_DESCENDING. AdsGetIndexHandleByExpr will find the index with the expression that is of the same "scending" value. |
| phIndex (O) | Handle of an index order. |

Remarks

This function returns the index handle corresponding to the indicated index expression.

Example

[Click Here](ace_examples.htm#adsgetindexhandlebyexprexample)

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsGetIndexHandle](ace_adsgetindexhandle.htm)

[AdsGetIndexHandleByOrder](ace_adsgetindexhandlebyorder.htm)

[AdsGetIndexName](ace_adsgetindexname.htm)