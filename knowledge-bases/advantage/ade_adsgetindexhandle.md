AdsGetIndexHandle




Advantage Database Server 12  

TAdsTable.AdsGetIndexHandle

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetIndexHandle  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetIndexHandle Advantage TDataSet Descendant ade\_Adsgetindexhandle Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetIndexHandle  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the handle of an index order given the index order name.

Syntax

function AdsGetIndexHandle( strIndexOrder : String ) : ADSHANDLE;

Parameter

|  |  |
| --- | --- |
| strIndexOrder | Name of index order for which to search. |

Description

For non-compound indexes, the index order name is the base of the file name (up to 8 characters). For compound indexes, the index order name is the tag name (up to 10 characters for CDXs, IDXs, and NTXs and up to 128 characters for ADIs).

If there is more than one index order open with the same name, the Advantage Client Engine will return the first one it finds.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName;DeptNum', 'Empid>50', '', [] );

 

hHandle := AdsTable1.AdsGetIndexHandle( Tag1 );

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsGetIndexName](ade_adsgetindexname.htm)

[AdsOpenIndex](ade_adsopenindex.htm)