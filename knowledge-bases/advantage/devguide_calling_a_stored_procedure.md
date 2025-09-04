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
| Calling a Stored Procedure  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Calling a Stored Procedure Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Calling\_a\_Stored\_Procedure Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 15 - Using Advantage from Delphi > Calling a Stored Procedure / Dear Support Staff, |  |
| Calling a Stored Procedure  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Stored procedures are invoked using SQL EXECUTE PROCEDURE statements in most of the Advantage data access mechanisms, and you can use an AdsQuery in Delphi to do the same. But Delphi developers have an alternative solutionbeing able to invoke a stored procedure using the AdsStoredProc component.

There are several advantages to invoking a stored procedure using an AdsStoredProc. The first is that you can use the Params property of the stored procedure to configure and assign the stored procedure's input parameters. After configuring a stored procedure in the Delphi IDE, you can select the Params property editor of the stored procedure to view the names and data types of each parameter. The names and data types of each of the stored procedure's parameters automatically appear in the Params property editor. If you like, you can then assign default values to the parameters that appear in the Params property editor, though binding values to parameters is often something that you do at runtime.

Another advantage of AdsStoredProc is realized when the stored procedure returns a result set. Specifically, stored procedures that return a result set can be treated exactly the same as AdsTables and AdsQueries that return a result set. They can be assigned to the DataSet property of a DataSource so that the returned data can be associated with data-aware controls. The AdsStoredProc also populates any output parameters, which can be read individually using the Params property or ParamByName method.

At a minimum, you must set the AdsConnection and the StoredProcName properties of the stored procedure. Also, you must assign values to all input parameters, if present, prior to executing the stored procedure. Set the AdsStoredProc component's ParamBindMode property to pbByName or pbByNumber, based on whether you want to bind parameters by name or position, respectively.

If your stored procedure returns a result set, you execute it by calling its Open method, or by setting its Active property to True. If your stored procedure does not return a result set, you execute it by calling its ExecProc method.

If you want to execute a given stored procedure more than once, and with different values passed to its input parameters, you must first close the stored procedure before changing any input parameters. However, this is not necessary for a stored procedure that does not return a result set.

The use of a stored procedure is demonstrated by the following code associated with the OnClick event handler for the Show 10% of Invoices button (shown in Figure 15-2). This code assumes that the SQL stored procedure created in Chapter 7, SQLGet10Percent, is assigned to the StoredProcName property of the AdsStoredProc component referenced in this code.

procedure TForm1.CallStoredProcBtnClick(Sender: TObject);  
begin  
  if AdsStoredProc1.Active then AdsStoredProc1.Close;  
  if ParamText.Text = '' then  
  begin  
    ShowMessage('Please enter a customer number');  
    Exit;  
  end;  
  AdsStoredProc1.Params[0].Value := ParamText.Text;  
  try  
    AdsStoredProc1.Open;  
  except  
    on e: Exception do  
      ShowMessage(e.Message);  
  end;  
  DataSource1.DataSet := AdsStoredProc1;  
end;

To view the stored procedure's parameters, select AdsStoredProc1 on the main form and then, using the Object Inspector, select the Params property and click the ellipsis button that appears. Delphi displays the parameters in the Params collection editor shown in Figure 15-3.

Figure 15-3: The Params collection editor

If you select one of the available parameters in the Params collection editor, you can view and edit the parameters properties using the Object Inspector shown in Figure 15-4.

Figure 15-4: The Object Inspector