---
title: Devguide Reading And Writing Data
slug: devguide_reading_and_writing_data
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_reading_and_writing_data.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 6547e8125d2a60703326a069e6bf582c6d2aa379
---

# Devguide Reading And Writing Data

Reading and Writing Data

     Reading and Writing Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Reading and Writing Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You access individual records in a TDataSet using its Fields property or its FieldByName method. Fields is a collection property, and you must pass it an index that identifies which field you want to read from or write to, based on its zero-based ordinal position in the table's structure. When you invoke FieldByName, you pass a string containing the name of the field you want to work with. This approach works for any AdsTable, AdsQuery, or AdsStoredProc component that returns a result set.

The following event handler, associated with the Get Address button (shown in Figure 15-2), demonstrates how to read a field:

procedureC TForm1.GetAddressBtnClick(Sender: TObject);  
begin  
  if AdsTable1.Active then AdsTable1.Close;  
  AdsTable1.TableName := 'CUSTOMER';  
  AdsTable1.IndexName := 'Customer ID';  
  AdsTable1.Open;  
  if AdsTable1.FindKey([CustNoText.Text]) then  
    OldAddressText.Text :=  
      AdsTable1.FieldByName('Address').AsString  
  else  
    ShowMessage('Customer ID ' + CustNoText.Text +   
      ' not found');  
  DataSource1.DataSet := AdsTable1;  
end;

The following event handler, associated with the Set New Address button (shown in Figure 15-2), demonstrates writing to a field:

procedure TForm1.SetAddressBtnClick(Sender: TObject);  
begin  
  if AdsTable1.Active then AdsTable1.Close;  
  AdsTable1.TableName := 'CUSTOMER';  
  AdsTable1.IndexName := 'Customer ID';  
  AdsTable1.Open;  
  if AdsTable1.FindKey([CustNoText.Text]) then  
  begin  
    AdsTable1.Edit;  
    AdsTable1.FieldByName('Address').AsString :=  
      NewAddressText.Text;  
    AdsTable1.Post;  
  end  
  else  
    ShowMessage('Customer ID ' + CustNoText.Text +   
      ' not found');  
  DataSource1.DataSet := AdsTable1;  
end;
