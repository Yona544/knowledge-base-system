---
title: Devguide Setting An Index
slug: devguide_setting_an_index
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_setting_an_index.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 051fa7e5d376036d0fdb887bd3c0d6e556cac928
---

# Devguide Setting An Index

Setting an Index

     Setting an Index

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Setting an Index  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

If you are connected to a data dictionary, and you have designated a default index for a table, that index will automatically be used when you open that table using an AdsTable. If you do not have a default index, or want to switch to some other index, you set the IndexName property of the AdsTable to the name of the index you want to use. This is demonstrated in the following code segment, which is associated with the Select Invoice No Index button (shown in Figure 15-2):

procedure TForm1.SetIndexBtnClick(Sender: TObject);  
begin  
  if (AdsTable1.TableName <> 'INVOICE') and  
    (AdsTable1.Active) then  
    AdsTable1.Close;  
  AdsTable1.IndexName := 'Invoice No';  
end;
