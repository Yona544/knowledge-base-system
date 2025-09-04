Creating a Table and Granting Rights to It




Advantage Database Server 12  

     Creating a Table and Granting Rights to It

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Creating a Table and Granting Rights to It  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating a Table and Granting Rights to It Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_a\_Table\_and\_Granting\_Rights\_to\_It Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 15 - Using Advantage from Delphi > Creating a Table and Granting Rights to It / Dear Support Staff, |  |
| Creating a Table and Granting Rights to It  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The Delphi\_TDataSet project permits a user to enter the name of a table that will be created in the data dictionary, after which all groups will be granted rights to the table. This operation is demonstrated in the following event handler, which is associated with the OnClick event of the Create Table and Grant Rights button (shown in Figure 15-2). Unlike most of the code shown in this chapter, several comment lines are retained here, due to its complexity:

procedure TForm1.CreateTableBtnClick(Sender: TObject);  
var  
  AdminConnection: TAdsConnection;  
  AdminTable: TAdsTable;  
  Strings: TStringList;  
  i: Integer;  
begin  
  if TableNameText.Text = '' then  
  begin  
    ShowMessage('Please enter the name of the ' +  
      'table to create');  
    Exit;  
  end;  
  //Create Connection and Table objects  
  AdminConnection := TAdsConnection.Create(nil);  
  AdminConnection.Name := 'Admin';  
  AdminTable := TAdsTable.Create(AdminConnection);  
  AdminTable.DatabaseName := AdminConnection.Name;  
  Strings := TStringList.Create;  
  try  
    //Configure Connection and Table objects  
    AdminConnection.AliasName := AdsConnection1.AliasName;  
    AdminConnection.AdsServerTypes :=  
      AdsConnection1.AdsServerTypes;  
    AdminConnection.Username := 'adssys';  
    AdminConnection.Password := 'password';  
    AdminConnection.LoginPrompt := False;  
    AdminConnection.IsConnected := True;  
    AdminConnection.GetTableNames(Strings,  
      TableNameText.Text);  
    for i := 0 to Pred(Strings.Count) do  
      if AnsiCompareText(Strings.Strings[i],  
        TableNameText.Text) = 0 then  
      begin  
        ShowMessage('This table already exists. ' +  
          'Cannot create');  
        Exit;  
      end;  
    //Define new table structure and create it  
    with AdminTable.FieldDefs do  
    begin  
      Add('Full Name', ftString, 30);  
      Add('Date of Birth', ftDate);  
      with AddFieldDef do  
      begin  
        Name := 'Credit Limit';  
        DataType := ftBCD;  
        Precision := 20;  
        Size := 4;  
      end;  
      Add('Active', ftBoolean);  
    end;  
    AdminTable.TableType := ttAdsADT;  
    AdminTable.TableName := TableNameText.Text;  
    AdminTable.CreateTable;  
    //Configure and connect the AdsDictionary object  
    AdsDictionary1.AliasName := AdminConnection.AliasName;  
    AdsDictionary1.AdsServerTypes :=  
      AdminConnection.AdsServerTypes;  
    AdsDictionary1.UserName := AdminConnection.Username;  
    AdsDictionary1.Password := AdminConnection.Password;  
    AdsDictionary1.LoginPrompt := False;  
    AdsDictionary1.Connect;  
    Strings.Clear;  
    AdsDictionary1.GetGroupNames(Strings);  
    if Strings.Count = 0 then  
    begin  
      ShowMessage('No groups to grant rights to');  
      Exit;  
    end;  
    //Grant access rights to all groups  
    for i := 0 to Pred(Strings.Count) do  
      AdsDictionary1.SetObjectAccessRights  
        (TableNameText.Text, Strings.Strings[i], 'RW');  
    //cleanup  
  finally  
    AdsDictionary1.Disconnect;  
    Strings.Free;  
    AdminTable.Free;  
    AdminConnection.IsConnected := False;  
    AdminConnection.Free;  
  end;  
  ShowMessage('The ' + TableNameText.Text ' table has been '  
    +'created, with rights granted to all groups');  
end;

This event handler demonstrates a number of interesting techniques. First, while it uses an AdsDictionary component that was placed at design time onto the main form (shown in Figure 15-2), the AdsConnection and AdsTable used by the administrative connection are created and then discarded at runtime. This approach is always valid, and could have been used by many of the other event handlers listed in this chapter. In most cases, however, components that are placed and configured at design time are easier to maintain.

After verifying that the requested table does not already exist in the data dictionary, the administrative connection is configured and opened, and a new AdsTable is configured to use it. Next, the table's structure is defined (using both the Add and AddFieldDefs methods of the AdsTable), and the table is created with a call to CreateTable.

   
NOTE: The administrative user name and passwords are represented by string literals in this code segment. This was done for convenience, but in a real application, either you would ask for this information from the user or you would encrypt this data to prevent its discovery. (String literals can be inspected in compiled applications using a variety of tools.)  
 

After creating the table, the AdsDictionary component is configured and opened. Finally, the list of groups is retrieved and used to grant read and write access to the table.