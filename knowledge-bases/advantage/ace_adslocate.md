AdsLocate




Advantage Database Server 12  

AdsLocate

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsLocate  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsLocate Advantage Client Engine ace\_Adslocate Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsLocate  Advantage Client Engine |  |  |  |  |

Performs a sequential search for a record that matches the given expression

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsLocate (ADSHANDLE hTable,  UNSIGNED8 \*pucExpr,  UNSIGNED16 bForward,  UNSIGNED16 \*pbFound); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |
| pucExpr (I) | Expression that defines desired records. |
| bForward (I) | If True, then search forward. If False, search backward. |
| pbFound (O) | Return True (1) if record found. |

Remarks

AdsLocate performs an exhaustive search of the table for records that meet the given expression. The expression given must evaluate to True or False. AdsLocate and AdsContinue do respect any filters set on the table, therefore, for best performance set a filter before calling this function. If the bForward parameter is True, the search is performed from the top of the table. Subsequent calls to [AdsContinue](ace_adscontinue.htm) search in the same direction as the AdsLocate call.

If there is an existing index order, it is much more efficient to perform an indexed seek using [AdsSeek](ace_adsseek.htm) than to perform an AdsLocate. If there is not an existing index order, it would be faster to call [AdsSetFilter](ace_adssetfilter.htm) and use [AdsSkip](ace_adsskip.htm) to step through the records because the server performs the filtering.

Example

[Click Here](ace_examples.htm#adslocateexample)

See Also

[AdsIsFound](ace_adsisfound.htm)

[AdsContinue](ace_adscontinue.htm)

[AdsSeek](ace_adsseek.htm)