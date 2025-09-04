AdsGetAllIndexes




Advantage Database Server 12  

TAdsTable.AdsGetAllIndexes

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetAllIndexes  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetAllIndexes Advantage TDataSet Descendant ade\_Adsgetallindexes Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetAllIndexes  Advantage TDataSet Descendant |  |  |  |  |

Returns an array of open index order handles for the given table.

Syntax

function AdsGetAllIndexes( ahIndexes : Array of ADSHANDLE ) : Word;

Parameter

|  |  |
| --- | --- |
| ahIndexes | Return index order handles in the given array. |

Description

The index order handles are returned in the order they were opened. For CDX or ADI indexes, the index order handles are returned in the order in which they were created within the index file. Return value is the number of returned entries on output. AdsGetAllIndexes does not return information for full text search indexes.

Example

var

ahIndexes : Array [0 .. 10] of AdsHandle;

wIndexHandleCount : Word;

 

begin

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsCreateIndex( '', 'Tag1', 'LastName', '', '', [] );

AdsTable1.AdsCreateIndex( '', 'Tag2', 'DeptNum', '', '', [] );

 

wIndexHandleCount := AdsTable1.AdsGetAllIndexes( ahIndexes );

{ wIndexHandleCount equals 2 and ahIndexes contains two values }

See Also

[AdsCreateIndex](ade_adscreateindex.htm)

[AdsGetIndexHandle](ade_adsgetindexhandle.htm)

[AdsGetNumIndexes](ade_adsgetnumindexes.htm)

[AdsOpenIndex](ade_adsopenindex.htm)