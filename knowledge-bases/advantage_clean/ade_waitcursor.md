---
title: Ade Waitcursor
slug: ade_waitcursor
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_waitcursor.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3a29a4d6ca6aa8da8c7079724310f1f5cd9930fe
---

# Ade Waitcursor

WaitCursor

TAdsQuery.WaitCursor

Advantage TDataSet Descendant

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
