AdsNumericsAsFloats




Advantage Database Server 12  

AdsTableOptions.AdsNumericsAsFloats

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsTableOptions.AdsNumericsAsFloats  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - AdsTableOptions.AdsNumericsAsFloats Advantage TDataSet Descendant ade\_Adsnumericsasfloats Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsTableOptions.AdsNumericsAsFloats  Advantage TDataSet Descendant |  |  |  |  |

[AdsTableOptions](ade_adstableoptions.htm)

Boolean flag used to force legacy behavior when using DBF numeric fields.

Syntax

property AdsTableOptions.AdsNumericsAsFloats

Description

In Advantage 8.1, the numeric field type was added to ADT tables. As part of this change, numeric persistent fields are now created as TAdsBcdField objects, as opposed to TFloatField objects. In most situations, this will not affect existing applications, because numeric fields did not exist in ADT tables before 8.1, so there is no existing code that utilizes persistent fields on numeric ADT fields.

One corner-case that will be affected, however, are static queries run on DBF base tables that have numeric fields. In this situation, the static result set is actually an ADT table. In the past, numeric DBF fields were mapped to either the ftFloat or ftSmallInt data type. In Advantage 8.1 and newer, numeric DBF fields in static cursors are now mapped directly to numeric ADT fields.

This change can cause runtime errors if you are using persistent fields. The persistent field will be defined as a TFloatField, for example, but at runtime the data type will be returned as TBcdField, and an exception will be raised of the form: "Type mismatch for field 'XXXX', expecting: Float actual: BCD". To resolve these errors, set the AdsNumericsAsFloats property to true.