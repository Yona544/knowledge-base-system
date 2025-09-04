AdsIsExprValid




Advantage Database Server 12  

AdsIsExprValid

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsExprValid  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsExprValid Advantage Client Engine ace\_Adsisexprvalid Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsExprValid  Advantage Client Engine |  |  |  |  |

Determines if a filter or index expression is valid

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsExprValid (ADSHANDLE hTable,  UNSIGNED8 \*pucExpr,  UNSIGNED16 \*pbValid); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucExpr (I) | Expression to check. |
| pbValid (O) | Set to True if expression is valid. |

Remarks

AdsIsExprValid tests whether an expression can be handled by the Advantage Expression Engine. If the expression is not valid, an application can call AdsGetLastError to retrieve the specific error code that will indicate why the expression is not valid. If the table type is not ADS\_ADT and the expression contains the binary concatenation operator (e.g., "lastname;firstname") or data types that are specific to ADT tables, then pbValid will be set to False.

Example

[Click Here](ace_examples.htm#adsisexprvalidexample)

See Also

[AdsSetFilter](ace_adssetfilter.htm)

[AdsLocate](ace_adslocate.htm)

[AdsCreateIndex](ace_adscreateindex.htm)