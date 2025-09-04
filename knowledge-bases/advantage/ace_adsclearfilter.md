AdsClearFilter




Advantage Database Server 12  

AdsClearFilter

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsClearFilter  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsClearFilter Advantage Client Engine ace\_Adsclearfilter Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsClearFilter  Advantage Client Engine |  |  |  |  |

Clears the current filter expression in a given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsClearFilter (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. If there is a filter on the given table, remove it. If there is no filter, no action takes place. |

Special Return Codes

|  |  |
| --- | --- |
| AE\_NO\_FILTER | No filter can be cleared or retrieved because no filter was set. |

Remarks

AdsClearFilter will remove the current filter from the specified table, allowing records that previously had not passed the filter to become visible again.

Example

[Click Here](ace_examples.htm#adsclearfilterexample)

See Also

[AdsGetFilter](ace_adsgetfilter.htm)

[AdsSetFilter](ace_adssetfilter.htm)