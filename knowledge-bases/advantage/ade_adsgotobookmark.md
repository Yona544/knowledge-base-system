AdsGotoBookmark




Advantage Database Server 12  

TAdsTable.AdsGotoBookmark

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGotoBookmark  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGotoBookmark Advantage TDataSet Descendant ade\_Adsgotobookmark Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGotoBookmark  Advantage TDataSet Descendant |  |  |  |  |

Positions the given table to the given bookmark.

Syntax

procedure AdsGotoBookmark( hBookmark : Longint );

Parameter

|  |  |
| --- | --- |
| hBookmark | Bookmark from a call to AdsGetBookmark. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: GotoBookmark. See your Delphi documentation for more information about this native Delphi method.

Description

This function is equivalent to AdsGotoRecord. Currently, hBookmark as returned from AdsGetBookmark is the record number.

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

 

Note This function is capable of utilizing registered callback functions. To learn more about callback functionality and how it behaves with this function, see [Callback Functionality](master_callback_functionality.htm).

Example

AdsTable1.FindKey( [Smith] );

oBookMark := AdsTable1.GetBookmark;

AdsTable1.Next;

 

AdsTable1.GotoBookmark( oBookMark );

See Also

[AdsGetBookmark](ade_adsgetbookmark.htm)

[AdsGotoRecord](ade_adsgotorecord.htm)