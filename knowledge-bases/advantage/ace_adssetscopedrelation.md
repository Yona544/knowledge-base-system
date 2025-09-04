AdsSetScopedRelation




Advantage Database Server 12  

AdsSetScopedRelation

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsSetScopedRelation  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsSetScopedRelation Advantage Client Engine ace\_Adssetscopedrelation Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsSetScopedRelation  Advantage Client Engine |  |  |  |  |

Sets a relation that causes a scope to be set on the child with each parent movement

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsSetScopedRelation (ADSHANDLE hTableParent,  ADSHANDLE hIndexChild,  UNSIGNED8 \*pucExpr); |

Parameters

|  |  |
| --- | --- |
| hTableParent (I) | Handle of parent table in relation. |
| hIndexChild (I) | Handle of child index order (not child) in relation. |
| pucExpr (I) | Expression to use for the relation. |

Remarks

In addition to performing the same functionality as [AdsSetRelation](ace_adssetrelation.htm), AdsSetScopedRelation sets a scope on the child table with each movement of the parent table. The high and low value of the scope will be the same and will be the key from the current parent record. Movement in the child table using the child tables handle will ignore relations. Movement using the child index order will obey the scope set by the relation.

Note Any existing scope set with [AdsSetScope](ace_adssetscope.htm) on the child table will be cleared by AdsSetScoped Relation. Scopes set by a relation are not cleared by calling [AdsClearRelation](ace_adsclearrelation.htm).

Example

[Click Here](ace_examples.htm#adssetscopedrelationexample)

See Also

[AdsClearScope](ace_adsclearscope.htm)

[AdsSetRelation](ace_adssetrelation.htm)

[AdsClearRelation](ace_adsclearrelation.htm)