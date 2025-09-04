AdsGetBookmark




Advantage Database Server 12  

TAdsTable.AdsGetBookmark

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGetBookmark  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGetBookmark Advantage TDataSet Descendant ade\_Adsgetbookmark Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGetBookmark  Advantage TDataSet Descendant |  |  |  |  |

Retrieves a bookmark for a later call to AdsGotoBookmark.

Syntax

function AdsGetBookmark : Longint;

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: GetBookmark. See your Delphi documentation for more information about this native Delphi method.

Description

AdsGetBookmark returns the physical record number. It is the equivalent of AdsGetRecordNum called with IGNORE \_WHEN\_COUNTING.

Example

AdsTable1.FindKey( [Smith] );

oBookMark := AdsTable1.GetBookmark;

AdsTable1.Next;

 

AdsTable1.GotoBookmark( oBookMark );

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.htm)

[AdsGotoBookmark](ade_adsgotobookmark.htm)

[AdsGotoRecord](ade_adsgotorecord.htm)