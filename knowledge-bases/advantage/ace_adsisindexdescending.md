AdsIsIndexDescending




Advantage Database Server 12  

AdsIsIndexDescending

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsIndexDescending  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsIndexDescending Advantage Client Engine ace\_Adsisindexdescending Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsIndexDescending  Advantage Client Engine |  |  |  |  |

Determines if the given index order is descending.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsIndexDescending (ADSHANDLE hIndex,  UNSIGNED16 \*pbDescending); |

Parameters

|  |  |
| --- | --- |
| hIndex (I) | Handle of index order of interest. |
| pbDescending (O) | Return True if index order is descending. |

Remarks

Descending index keys are sorted from largest to smallest. The default is an ascending index. An [AdsGotoTop](ace_adsgototop.htm) call on a descending order will position at the largest key in the index. An AdsGotoBottom call will position at the smallest key in the index order.

Example

[Click Here](ace_examples.htm#adsisindexdescendingexample)

See Also

[AdsOpenIndex](ace_adsopenindex.htm)

[AdsCreateIndex](ace_adscreateindex.htm)