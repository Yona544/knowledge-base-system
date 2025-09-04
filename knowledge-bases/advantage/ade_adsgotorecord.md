AdsGotoRecord




Advantage Database Server 12  

TAdsTable.AdsGotoRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsGotoRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsGotoRecord Advantage TDataSet Descendant ade\_Adsgotorecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsGotoRecord  Advantage TDataSet Descendant |  |  |  |  |

Positions the given table to the given record number.

Syntax

procedure AdsGotoRecord( ulRecNum : Longint );

Parameter

|  |  |
| --- | --- |
| ulRecNum | Record number to goto. |

CAUTION It is recommended that this Advantage extended method not be used. Please read the [Caution About Extended Methods](ade_caution_about_extended_methods.htm) for more information. The suggested native Delphi method to use instead is: TTable.GotoBookmark. See your Delphi documentation for more information about this native Delphi method.

 

Note Explicitly moving to a deleted record when using the Advantage proprietary table format (ADT) is an illegal operation and will return the error 5022 (AE\_INVALID\_RECORD\_NUMBER), invalid record number.

Description

AdsGotoRecord ignores filters, relations, and scopes. If ulRec is zero, the client will be unpositioned (EOF and BOF will be set), and the current record number will be set to 0. If ulRec is greater than the number of records in the table, the client will be unpositioned (EOF and BOF will be set), and the current record number will be set to the number of records in the table + 1.

Example

SavePlace := AdsTable1.GetBookmark;

AdsTable1.FindKey( ['Smith'] );

 

{. . .your code here. . .}

 

Adstable1.GotoBookmark( SavePlace );

See Also

[AdsGetRecordNum](ade_adsgetrecordnum.htm)

[AdsGotoBottom](ade_adsgotobottom.htm)

[AdsGotoTop](ade_adsgototop.htm)

[AdsSkip](ade_adsskip.htm)

[AdsWriteRecord](ade_adswriterecord.htm)