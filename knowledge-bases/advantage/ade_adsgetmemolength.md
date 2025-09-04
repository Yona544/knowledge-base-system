AdsGetMemoLength




Advantage Database Server 12  

TAdsTable.AdsGetMemoLength

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetMemoLength  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetMemoLength Advantage TDataSet Descendant ade\_Adsgetmemolength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetMemoLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the length of the specified memo field of the current record.

Syntax

function AdsGetMemoLength( strFieldName : String ) : Longint;

Parameter

|  |  |
| --- | --- |
| strFieldName | Name of memo field. |

Description

AdsGetMemoLength returns the length of the specified memo field in characters.  For Unicode memo fields of type ADS\_NMEMO this is the number of 16-bit code units.  For memo fields of type ADS\_MEMO, the length in characters is the same as the length in bytes. AdsGetMemoLength will not support binary object fields. Use AdsGetBinaryLength for binary fields.

Example

lMemoLength := AdsTable1.AdsGetMemoLength( Notes );

See Also

[AdsGetField](ade_adsgetfield.htm)

[AdsGetFieldLength](ade_adsgetfieldlength.htm)

[AdsGetFieldType](ade_adsgetfieldtype.htm)

[AdsGetMemoDataType](ade_adsgetmemodatatype.htm)

[AdsGetString](ade_adsgetstring.htm)