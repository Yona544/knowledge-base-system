WaitCursor




Advantage Database Server 12  

TAdsStoredProc.WaitCursor

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsStoredProc.WaitCursor  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsStoredProc.WaitCursor Advantage TDataSet Descendant ade\_Waitcursor\_tadsstoredproc Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsStoredProc.WaitCursor  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.htm)

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