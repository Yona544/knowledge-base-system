---
title: Devguide Executing A Query
slug: devguide_executing_a_query
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_executing_a_query.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: da62ef8475b031e918f15c7209f12b332bbe2f2e
---

# Devguide Executing A Query

Executing a Query

     Executing a Query

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Executing a Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You define a query by assigning the SQL statement you want to execute to the SQL StringList property of an AdsQuery. If the query returns a result set, you execute it by calling its Open method or by setting its Active property to True. If the query does not return a result set, execute it by calling its ExecSQL method.

   
NOTE: The SQL that you can assign to the SQL property of an AdsQuery can be either a single SQL statement or an Advantage SQL script. Advantage SQL scripts are described in Chapter 13.  
 

By default, you cannot edit the result set returned by an AdsQuery. If your query produces a live cursor, setting the AdsQuery's RequestLive property to True permits you to edit the data in the result set.

The following code demonstrates the execution of a query entered by the user. It is associated with the Execute SELECT button (shown in Figure 15-2):

procedure TForm1.DoSelectClick(Sender: TObject);  
begin  
  if AdsQuery1.Active then AdsQuery1.Close;  
  AdsQuery1.SQL.Text := SELECTText.Text;  
  AdsQuery1.Open;  
  DataSource1.DataSet := AdsQuery1;  
end;
