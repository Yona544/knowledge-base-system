WaitCursor




Advantage Database Server 12  

TAdsQuery.WaitCursor

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.WaitCursor  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.WaitCursor Advantage TDataSet Descendant ade\_Waitcursor Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.WaitCursor  Advantage TDataSet Descendant |  |  |  |  |

This property is no longer used and exists only for backwards compatibility. If a cursor is supplied it will be ignored. If you would like to display a cursor during query execution use code similar to the example provided below.

 

procedure TForm1.Button1Click(Sender: TObject);

var

SavedCursor : TCursor;

begin

 

SavedCursor := Screen.Cursor;

try

Screen.Cursor := crHourGlass;

AdsQuery1.Open;

finally

Screen.Cursor := SavedCursor;

end;

end;