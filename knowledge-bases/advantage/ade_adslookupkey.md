AdsLookupKey




Advantage Database Server 12  

TAdsTable.AdsLookupKey

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsLookupKey  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsLookupKey Advantage TDataSet Descendant ade\_Adslookupkey Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsLookupKey  Advantage TDataSet Descendant |  |  |  |  |

Performs an indexed search on the given table using the given index order to determine if a key exists in the index. Scopes and filters are ignored.

Syntax

function AdsLookupKey( const strTag, strKey : string ) : boolean;

Parameters

|  |  |
| --- | --- |
| strTag | Name of tag to search. |
| strKey | Search key. |

Description

AdsLookupKey determines if a key exists in the index. It does not perform any record movement. This function may be used to determine if a key value can be added to a unique index. See [AdsCreateIndex](ade_adscreateindex.htm) for information about unique indexes.

Example

AdsTable1.IndexName := FirstName;

bFound := AdsTable1.AdsLookupKey( 'LastName', 'Smith' );

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsSeek](ade_adsseek.htm)