AdsClearAllScopes




Advantage Database Server 12  

TAdsTable.AdsClearAllScopes

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsClearAllScopes  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsClearAllScopes Advantage TDataSet Descendant ade\_Adsclearallscopes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsClearAllScopes  Advantage TDataSet Descendant |  |  |  |  |

Clears scopes on all indexes open for the given table.

Syntax

procedure AdsClearAllScopes;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: CancelRange. See your Delphi documentation for more information about this native Delphi method.

Description

This function will clear both top and bottom scopes for all index orders open for this table.

Example

AdsTable1.SetRange( [Adams], [Smith] );

AdsTable1.CancelRange;

See Also

[AdsClearScope](ade_adsclearscope.htm)

[AdsGetScope](ade_adsgetscope.htm)

[AdsSetScope](ade_adssetscope.htm)