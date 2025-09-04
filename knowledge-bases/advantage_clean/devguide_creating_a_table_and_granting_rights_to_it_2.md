---
title: Devguide Creating A Table And Granting Rights To It 2
slug: devguide_creating_a_table_and_granting_rights_to_it_2
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_a_table_and_granting_rights_to_it_2.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 439d04f60616c78469ca616e45c4cadc2d5c62ba
---

# Devguide Creating A Table And Granting Rights To It 2

Creating a Table and Granting Rights to It

     Creating a Table and Granting Rights to It

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating a Table and Granting Rights to It  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The VB\_ADO.vbp project permits a user to enter the name of a table that will be created in the data dictionary, after which all groups will be granted rights to the table. This operation is demonstrated in the following subprocedure, which is associated with the click event of the Create Table and Grant Rights button shown in Figure 17-1:

If TableNameText.Text = "" Then  
  MsgBox "Please enter the name of the table to create"  
  Exit Sub  
End If  
'Check for semicolon hack  
If InStr(1, TableNameText.Text, ";", \_   
    vbTextCompare) <> 0 Then  
  MsgBox "Table name may not contain a semicolon"  
  Exit Sub  
End If  
If AdsRecordset.State = adStateOpen Then  
  AdsRecordset.Close  
End If  
AdminConnection.ConnectionString = \_  
  "Provider=Advantage OLE DB Provider;" + \_  
  "Data Source=" + DataPath + ";user ID=adssys;" + \_  
  "password=password;" + \_  
  "ServerType=ADS\_LOCAL\_SERVER | ADS\_REMOTE\_SERVER;" + \_  
    "FilterOptions=RESPECT\_WHEN\_COUNTING;" + \_  
    "TrimTrailingSpaces=True"  
AdminConnection.Open  
Set AdminCommand.ActiveConnection = AdminConnection  
AdsRecordset.Open "SELECT COUNT(\*) FROM system.tables " + \_  
  "WHERE UCASE(Name) = UCASE(TableName.Text)", \_  
  AdminConnection, adOpenDynamic, adLockPessimistic, \_  
    adCmdText  
AdsRecordset.MoveFirst  
If AdsRecordset.Fields(0).Value = 1 Then  
  MsgBox "This table already exists. Cannot create"  
  Exit Sub  
End If  
AdminCommand.CommandText = "CREATE TABLE " + TableNameText.Text + \_  
  "([Full Name] CHAR(30)," + \_  
  "[Date of Birth] DATE," + \_  
  "[Credit Limit] MONEY, " + \_  
  "Active LOGICAL)"  
AdminCommand.Execute  
AdsRecordset.Close  
AdsRecordset.Open "SELECT \* FROM system.usergroups", \_  
  AdminConnection, adOpenDynamic, adLockPessimistic, adCmdText  
If AdsRecordset.BOF And AdsRecordset.EOF Then  
  MsgBox "No groups to grant rights to"  
  Exit Sub  
End If  
AdsRecordset.MoveFirst  
While Not AdsRecordset.EOF  
  AdminCommand.CommandText = "GRANT ALL ON " + \_  
    TableNameText.Text + " TO """ + \_  
    AdsRecordset.Fields(0).Value + """"  
  AdminCommand.Execute  
  AdsRecordset.MoveNext  
Wend  
AdminConnection.Close  
MsgBox "The " + TableNameText.Text + " table has been " + \_  
  "created, with rights granted to all groups"

This subprocedure begins by verifying that the table name does not include a semicolon, which could be used to convert the subsequent GRANT SQL statement into a SQL script. Since this value represents a table name, a parameterized query is not an option.

Next, this code verifies that the table does not already exist in the data dictionary. Once that is done, a new connection is created using the data dictionary administrative account. This connection is then used to call CREATE TABLE to create the table, and then to call GRANT for each group returned in the system.usergroups table.

   
NOTE: The administrative user name and passwords are represented by string literals in this code segment. This was done for convenience, but in a real application, either you would ask for this information from the user or you would obfuscate this information so that it could not be retrieved from the executable.
