AdsSetScope




Advantage Database Server 12  

TAdsTable.AdsSetScope

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSetScope  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSetScope Advantage TDataSet Descendant ade\_Adssetscope Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSetScope  Advantage TDataSet Descendant |  |  |  |  |

Sets a scope for the given index order.

Syntax

type TAdsScopeOptions = ( soTOP, soBOTTOM );

 

procedure AdsSetScope( eScopeOption : TAdsScopeOptions; strScope : String );

Parameter

|  |  |
| --- | --- |
| eScopeOption | Indicates which scope value to set. |
| strScope | Scope value to set. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: SetRange. See your Delphi documentation for more information about this native Delphi method.

Description

AdsSetScope sets a scope for the index to limit the number of records visible. For example, setting a soTOP scope of "M" on an index on a character field will make an AdsGotoTop call on this index go to the first key greater than or equal to "M". A soBOTTOM scope will make the indicated value the last one visible in the index order. For example, if AdsSetScope is called with soBOTTOM and "Smith" on a lastname index, the last Smith on an AdsGotoBottom call will be the current record. Set the scope for top and bottom to the same value to only view records with the given scope value from the index.

It is not necessary to have both top and bottom scopes set at the same time. The Advantage Client Engine does not check that the soTOP and soBOTTOM scopes are not mutually exclusive. When setting scopes on descending indexes, the soTOP scope will be set at the logical top of the index (largest key) and the soBOTTOM is at the logical bottom (smallest key).

To set a scope on indexes built on date, time, or timestamp fields, the date and time values must be formatted as text. The date should be formatted according to [DateFormat](ade_dateformat.htm). For example, to set a scope on a date index, an application might pass "2/25/1997" as the scope value. To set a scope on a timestamp index, the value could be "2/25/1997 3:25pm".

Note If both a narrow scope and a narrow filter (narrow meaning that very few records match the scope or filter conditions) are being used on the same table, poor performance may result. Since knowledge of scopes is only on the client, and filters are handled on the server, the filtering of records on the server may unnecessarily traverse well beyond the bounds of a scope, causing poor performance. If this condition is expected, it is recommended to use either a scope or a filter, but not both.

Example

AdsTable1.SetRange( [Adams], [Smith] );

AdsTable1.CancelRange;

See Also

[AdsClearAllScopes](ade_adsclearallscopes.htm)

[AdsClearScope](ade_adsclearscope.htm)

[AdsGetScope](ade_adsgetscope.htm)

[AdsGotoBottom](ade_adsgotobottom.htm)

[AdsGotoTop](ade_adsgototop.htm)

[AdsSeek](ade_adsseek.htm)

[AdsSkip](ade_adsskip.htm)