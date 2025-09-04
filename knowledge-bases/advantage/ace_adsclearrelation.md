AdsClearRelation




Advantage Database Server 12  

AdsClearRelation

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsClearRelation  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsClearRelation Advantage Client Engine ace\_Adsclearrelation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsClearRelation  Advantage Client Engine |  |  |  |  |

Clears all relations for the given parent table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsClearRelation (ADSHANDLE hTableParent); |

Parameters

|  |  |
| --- | --- |
| hTableParent (I) | Handle of parent table. |

Remarks

This function clears relations set by [AdsSetRelation](ace_adssetrelation.htm) and [AdsSetScopedRelation](ace_adssetscopedrelation.htm). If this table is the child in another relation, that relation is not cleared.

Example

[Click Here](ace_examples.htm#adsclearrelationexample)

See Also

[AdsSetRelation](ace_adssetrelation.htm)

[AdsSetScopedRelation](ace_adssetscopedrelation.htm)