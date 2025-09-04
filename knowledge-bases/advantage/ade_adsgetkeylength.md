AdsGetKeyLength




Advantage Database Server 12  

TAdsTable.AdsGetKeyLength

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetKeyLength  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetKeyLength Advantage TDataSet Descendant ade\_Adsgetkeylength Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetKeyLength  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the key size in bytes of the given index order.

Syntax

function AdsGetKeyLength : Word;

Description

Returns the number of bytes in each physical key in the index file. If the index key evaluates to a variable-length expression, this function will return zero for the length.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'Empid>50', '', [] );

AdsTable1.IndexName := 'Tag1';

 

wKeyLength := AdsTable1.AdsGetKeyLength;

{ wKeyLength equals 20 }

See Also

[AdsExtractKey](ade_adsextractkey.htm)

[AdsGetKeyType](ade_adsgetkeytype.htm)