AdsGetIndexExpr




Advantage Database Server 12  

AdsGetIndexExpr

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsGetIndexExpr  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsGetIndexExpr Advantage Client Engine ace\_Adsgetindexexpr Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsGetIndexExpr  Advantage Client Engine |  |  |  |  |

Retrieves the index key expression of this index order.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsGetIndexExpr (ADSHANDLE hIndex,  UNSIGNED8 \*pucKeyExpr,  UNSIGNED16 \*pusLen); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest. |
| pucKeyExpr (O) | Returns the index order key expression in this buffer. |
| pusLen (I/O) | Length of given buffer on input, length of returned data on output. |

Remarks

The index expression returned by AdsGetIndexExpr is the expression that is evaluated against records in the table to generate index keys. This expression can evaluate to a numeric value, a string value, a date, or a logical.

Example

[Click Here](ace_examples.htm#adsgetindexexprexample)

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCreateIndex](ace_adscreateindex.htm)

[AdsIsExprValid](ace_adsisexprvalid.htm)