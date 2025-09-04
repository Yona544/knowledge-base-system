AdsSeekLast




Advantage Database Server 12  

TAdsTable.AdsSeekLast

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsSeekLast  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsSeekLast Advantage TDataSet Descendant ade\_Adsseeklast Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsSeekLast  Advantage TDataSet Descendant |  |  |  |  |

Seeks for the last value in an index.

Syntax

function AdsSeekLast( strKey : String ) : Boolean;

Parameter

|  |  |
| --- | --- |
| strKey | Search key. |

Description

AdsSeekLast will perform a seek for the last key in the indicated index order that matches the passed in search key. If the key is not in the index, the function will position the table at EOF and set the found flag to False.

Example

AdsTable1.IndexName := LastName;

bFound := AdsTable1.AdsSeekLast( Smith );

See Also

[AdsSeek](ade_adsseek.htm)