---
title: Ade Waitcursor Tadsstoredproc
slug: ade_waitcursor_tadsstoredproc
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_waitcursor_tadsstoredproc.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: c6a9eba7750d204a4e96b4f77c7d5241454520a8
---

# Ade Waitcursor Tadsstoredproc

WaitCursor

TAdsStoredProc.WaitCursor

Advantage TDataSet Descendant

| TAdsStoredProc.WaitCursor  Advantage TDataSet Descendant |  |  |  |  |

[TAdsStoredProc](ade_tadsstoredproc.md)

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
