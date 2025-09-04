AdsClearAllScopes




Advantage Database Server 12  

AdsClearAllScopes

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsClearAllScopes  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsClearAllScopes Advantage Client Engine ace\_Adsclearallscopes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsClearAllScopes  Advantage Client Engine |  |  |  |  |

Clears scopes on all indexes open for the given table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsClearAllScopes (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of table or cursor. |

Remarks

This function will clear both top and bottom scopes for all index orders open for this table.

Example

[Click Here](ace_examples.htm#adsclearallscopesexample)

See Also

[AdsSetScope](ace_adssetscope.htm)

[AdsClearScope](ace_adsclearscope.htm)

[AdsGetScope](ace_adsgetscope.htm)