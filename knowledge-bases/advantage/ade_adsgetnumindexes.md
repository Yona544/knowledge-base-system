AdsGetNumIndexes




Advantage Database Server 12  

TAdsTable.AdsGetNumIndexes

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetNumIndexes  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetNumIndexes Advantage TDataSet Descendant ade\_Adsgetnumindexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetNumIndexes  Advantage TDataSet Descendant |  |  |  |  |

Retrieves the total number of open index orders associated with the given table.

Syntax

function AdsGetNumIndexes : Word;

Description

Return number of index orders. For example, if the user opened a CDX file with five tags and an IDX, then this function would return the total 6. The number of indexes returned does not necessarily correspond to the number of index files opened for the table. A compound index may contain multiple index orders. Calling this function before calling [AdsGetAllIndexes](ade_adsgetallindexes.htm) will provide the number of index orders that will be returned. AdsGetNumIndexes does not return information for full text search indexes.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

AdsTable1.AdsCreateIndex( '', 'Tag2', 'DeptNum', '', '', [] );

wIndexCount := AdsTable1.AdsGetNumIndexes;

{ wIndexCount equals 2 }

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsGetAllIndexes](ade_adsgetallindexes.htm)

[AdsOpenIndex](ade_adsopenindex.htm)