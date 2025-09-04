---
title: Devguide Reading And Writing Data 2
slug: devguide_reading_and_writing_data_2
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_reading_and_writing_data_2.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 078161f53515a37cd298f8d23ca4665c2f986cbf
---

# Devguide Reading And Writing Data 2

Reading and Writing Data

     Reading and Writing Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Reading and Writing Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You read data from fields of a Recordset by using the Recordset's Fields property, which is a collection property. The Fields property takes a single parameter that identifies which field's value you want to read. This value can either be an integer identifying the ordinal position of the field in the table's structure (this value is zero-based) or it can be a string identifying the field's name. The Value property of the identified field holds the field's data.

Reading data from a Recordset is demonstrated in the following Click subprocedure associated with the Get Address button shown in Figure 17-1:

Dim AdsGetCustCommand As ADODB.Command  
Dim AdsGetCustRecordset As ADODB.Recordset  
Dim AdsGetCustParameter As ADODB.Parameter  
   
If CustNoText.Text = "" Or Not IsNumeric(CustNoText.Text) Then  
  MsgBox "Please supply a valid customer ID number"  
  Exit Sub  
End If  
Set AdsGetCustCommand = New ADODB.Command  
Set AdsGetCustRecordset = New ADODB.Recordset  
Set AdsGetCustCommand.ActiveConnection = AdsConnection  
AdsGetCustCommand.CommandText = \_  
  "SELECT \* FROM CUSTOMER WHERE [Customer ID] = ?"  
Set AdsGetCustParameter = AdsGetCustCommand.CreateParameter  
AdsGetCustCommand.Prepared = True  
AdsGetCustCommand.NamedParameters = False  
AdsGetCustParameter.Type = adInteger  
AdsGetCustCommand.Parameters.Append AdsGetCustParameter  
AdsGetCustParameter.Value = CInt(CustNoText.Text)  
AdsGetCustRecordset.Open AdsGetCustCommand, , \_  
  adOpenDynamic, adLockPessimistic, adCmdText  
If AdsGetCustRecordset.BOF And \_  
  AdsGetCustRecordset.EOF Then  
  MsgBox "No records for customer ID"  
  Set DataGrid1.DataSource = Nothing  
Else  
  Set DataGrid1.DataSource = AdsGetCustRecordset  
  OldAddressText.Text = \_  
    AdsGetCustRecordset.Fields("Address").Value  
End If

So long as your Recordset contains a dynamic (live) cursor, you can make changes to a Recordset by assigning data to one or more of the Recordset's Fields Value properties, where you identify the field you are writing to by using the same technique that you use to read from a field. After changing one or more fields, you call the Update method of the Recordset to write those changes to Advantage. Alternatively, you can call the Recordset's Update, passing to it either a field name/value pair or an array of field name/value pairs. This second approach writes one or more updated fields to ADS in a single command.

The following code demonstrates one way to update a Recordset. This code can be found for the click procedure associated with the button labeled Set New Address shown in Figure 17-1:

If CustNoText.Text = "" Or Not IsNumeric(CustNoText.Text) Then  
  MsgBox "Please supply a valid customer ID number"  
  Exit Sub  
End If  
If InStr(1, TableNameText.Text, ";", vbTextCompare) <> 0 Then  
  MsgBox "Customer ID may not contain a semicolon"  
  Exit Sub  
End If  
Dim AdsGetCustRecordset As ADODB.Recordset  
Set AdsGetCustRecordset = New ADODB.Recordset  
AdsGetCustRecordset.Open "SELECT Address FROM CUSTOMER " + \_  
  "WHERE [Customer ID] = " + CustNoText.Text, \_  
  AdsConnection, adOpenDynamic, adLockPessimistic, adCmdText  
If AdsGetCustRecordset.BOF And \_  
  AdsGetCustRecordset.EOF Then  
  MsgBox "Customer ID not found"  
Else  
  AdsGetCustRecordset.Fields("Address").Value = \_  
    NewAddressText.Text  
  AdsGetCustRecordset.Update  
End If  
MsgBox "Address for customer " + CustNoText.Text + " " + \_  
  "has been updated"  
Exit Sub

Of course, a SQL UPDATE query can also be used to achieve a similar result.
