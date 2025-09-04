AdsClearScope




Advantage Database Server 12  

TAdsTable.AdsClearScope

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsClearScope  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsClearScope Advantage TDataSet Descendant ade\_Adsclearscope Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsClearScope  Advantage TDataSet Descendant |  |  |  |  |

Clears scope on the given index order.

Syntax

type TAdsScopeOptions = ( soTOP, soBOTTOM );

 

procedure AdsClearScope( eScopeOption : TAdsScopeOption );

Parameter

|  |  |
| --- | --- |
| eScopeOption | Enumerated type for the scope option. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: CancelRange. See your Delphi documentation for more information about this native Delphi method.

Example

AdsTable1.SetRange( [Adams], [Smith] );

 

AdsTable1.CancelRange;

Description

If the top or bottom scope is cleared, any other scope settings remain. If currently positioned at EOF or BOF and a scope is cleared, it is necessary to reposition by performing a movement to see any records.

See Also

[AdsClearAllScopes](ade_adsclearallscopes.htm)

[AdsGetScope](ade_adsgetscope.htm)

[AdsGotoBottom](ade_adsgotobottom.htm)

[AdsGotoTop](ade_adsgototop.htm)

[AdsSeek](ade_adsseek.htm)

[AdsSetScope](ade_adssetscope.htm)

[AdsSkip](ade_adsskip.htm)