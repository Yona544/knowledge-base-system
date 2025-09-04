Calling a Stored Procedure




Advantage Database Server 12  

     Calling a Stored Procedure

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Calling a Stored Procedure  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Calling a Stored Procedure Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Calling\_a\_Stored\_Procedure\_2 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 17 - MDAC, OLE DB, ADO > Calling a Stored Procedure / Dear Support Staff, |  |
| Calling a Stored Procedure  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Calling a stored procedure is no different than executing any other query. If your stored procedure does not require input parameters, you can define the query text using a Command object or by passing the call to EXECUTE PROCEDURE in the first parameter of a Recordset Open invocation. Alternatively, you simply pass the name of the stored procedure object in the CommandText, and set the CommandType property (of a Command object) or CommandType parameter (of the Resultset's Open method) to adCmdStoredProc (this second technique is demonstrated in the following example). Typically, you use a Command objectexecuting it directlywhen the stored procedure does not return records, and use the Open method of a Recordset when your stored procedure returns one or more records.

Invoking a stored procedure that takes one input parameter is demonstrated by the following code associated with the click event for the Show 10% of Invoices button (shown in Figure 17-1). The stored procedure referenced in this code is the SQL stored procedure created in Chapter 7. If you did not create this stored procedure, but created one of the other AEPs described in that chapter, substitute the name of the stored procedure object in your data dictionary in the CommandText property of the Command object.

Dim AdsSPCommand As ADODB.Command  
Dim AdsSPRecordset As ADODB.Recordset  
Dim AdsSPParameter As ADODB.Parameter  
   
If ParamText.Text = "" Or Not IsNumeric(ParamText.Text) Then  
  MsgBox "Please supply a valid customer ID number"  
  Exit Sub  
End If  
Set AdsSPCommand = New ADODB.Command  
Set AdsSPRecordset = New ADODB.Recordset  
Set AdsSPCommand.ActiveConnection = AdsConnection  
AdsSPCommand.CommandText = "SQLGet10Percent"  
Set AdsSPParameter = AdsSPCommand.CreateParameter  
AdsSPCommand.Prepared = True  
AdsSPCommand.NamedParameters = False  
AdsSPParameter.Type = adInteger  
AdsSPCommand.Parameters.Append AdsSPParameter  
AdsSPParameter.Value = CInt(ParamText.Text)  
AdsSPRecordset.Open AdsSPCommand, , adOpenDynamic, \_  
  adLockPessimistic, adCmdStoredProc  
Set DataGrid1.DataSource = AdsSPRecordset  
Exit Sub