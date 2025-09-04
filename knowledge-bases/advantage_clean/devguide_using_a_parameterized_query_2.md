---
title: Devguide Using A Parameterized Query 2
slug: devguide_using_a_parameterized_query_2
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_using_a_parameterized_query_2.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 6c72637290ce7792cec17115401761e1b7830a66
---

# Devguide Using A Parameterized Query 2

Using a Parameterized Query

     Using a Parameterized Query

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Using a Parameterized Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Parameterized queries are defined using a Command object. This command object can then be executed directly, so long as the query does not return a result set. If the parameterized query returns one or more records, you can execute it using the Open method of a Recordset, just as you can with a query that takes no parameters.

Before you can invoke a parameterized query, you must create one Parameter object for each of the query's parameters, and then associate each Parameter with the Command holding the parameterized query.

The definition of a parameterized query, including the creation and configuration of a parameter, is shown in the following code segment. This code segment is part of the Load event for the form object, and was omitted from the code listing shown earlier (in the section "Connecting to Data"):

'Set up the parameterized query that will be reused  
Set AdsParamQueryCommand = New ADODB.Command  
Set AdsParamQueryRecordset = New ADODB.Recordset  
Set AdsParamQueryCommand.ActiveConnection = AdsConnection  
AdsParamQueryCommand.CommandText = \_  
  "SELECT \* FROM INVOICE WHERE [Customer ID] = ?"  
Set AdsParameter = AdsParamQueryCommand.CreateParameter  
AdsParamQueryCommand.Prepared = True  
AdsParamQueryCommand.NamedParameters = False  
AdsParameter.Type = adInteger  
AdsParamQueryCommand.Parameters.Append AdsParameter

Once a Parameter has been created, configured, and associated with the Command holding the parameterized query statement, there is only one more step necessary before the query can be executed. You must bind data to each parameter. This is shown in the following click event of the DoParamQuery button (the button labeled Show Invoices in Figure 17-1):

If IsNumeric(ParamText.Text) = False Then  
  MsgBox "Invalid customer number"  
  Exit Sub  
End If  
If AdsParamQueryRecordset.State = adStateOpen Then  
  AdsParamQueryRecordset.Close  
End If  
AdsParameter.Value = CInt(ParamText.Text)  
AdsParamQueryRecordset.Open AdsParamQueryCommand, , \_  
    adOpenDynamic, adLockPessimistic, adCmdText  
If AdsParamQueryRecordset.BOF And \_  
  AdsParamQueryRecordset.EOF Then  
  MsgBox "No invoices for customer ID"  
  Set DataGrid1.DataSource = Nothing  
Else  
  Set DataGrid1.DataSource = AdsParamQueryRecordset  
End If

As you can see from this code, after verifying that a numeric value has been entered into the Customer ID field, the entered data is assigned to the Value property of the parameter and the query is executed.

This example is actually a classic example of how parameterized queries are used. Specifically, the query text is defined only once, but can be executed repeatedly. And by changing only the value of the parameter, a different result set can be returned upon each execution.

   
NOTE: The Advantage OLE DB Provider only supports positional parameters--named parameters are not supported. As a result, if you have more than one parameter, it is important to keep track of the position in which each parameter appears.
