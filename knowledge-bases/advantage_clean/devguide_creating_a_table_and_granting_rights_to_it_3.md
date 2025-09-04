---
title: Devguide Creating A Table And Granting Rights To It 3
slug: devguide_creating_a_table_and_granting_rights_to_it_3
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_a_table_and_granting_rights_to_it_3.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: b783fcd35d401834fcc76de88ae795d8251e1923
---

# Devguide Creating A Table And Granting Rights To It 3

Creating a Table and Granting Rights to It

     Creating a Table and Granting Rights to It

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating a Table and Granting Rights to It  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The CS\_ADONET project permits a user to enter the name of a table that will be created in the data dictionary, after which all groups will be granted rights to the table. This operation is demonstrated in the following method, which is associated with the Create Table and Grant Rights button shown in Figure 18-3:

private void addTableBtn\_Click(object sender,  
  System.EventArgs e)  
  {  
  AdsConnection adminConnection;  
  IDbCommand adminCommand;  
  AdsDataAdapter adminAdapter;  
  DataSet ds;  
  DataTable dt;  
  DataRow dr;  
  String tabName;  
   
  tabName = tableNameText.Text;  
  if (tabName.Equals(""))  
  {  
    MessageBox.Show(this,  
      "Please enter the name of the table to create");  
    return;  
  }  
  //Check for SQL injections hack  
  if ((tabName.IndexOf(";") >= 0))   
  {  
    MessageBox.Show(this,  
      "Table name may not contain a semicolon");  
   return;  
  }  
  try   
  {  
    adminConnection = new AdsConnection(  
      "Data Source=" + DataPath + ";user ID=adssys;" +  
      "password=password;" +   
      "ServerType=ADS\_LOCAL\_SERVER | ADS\_REMOTE\_SERVER;" +  
      "TrimTrailingSpaces=True");  
    adminConnection.Open();  
    adminAdapter = new AdsDataAdapter("SELECT Name FROM " +  
      "system.tables " +  
      "WHERE UCase(Name) = '" + tabName.ToUpper() + "'",  
      adminConnection);       
    ds = new DataSet();   
    adminAdapter.Fill(ds);  
    dt = ds.Tables[0];  
    if (dt.Rows.Count != 0)   
    {  
      MessageBox.Show(this,   
        "This table already exists. Cannot create");  
      return;  
     }  
    adminCommand = new AdsCommand("CREATE TABLE [" +  
      tabName + "] " +   
      "([Full Name] CHAR(30), [Date of Birth] DATE," +  
      "[Credit Limit] MONEY, Active LOGICAL)",  
       adminConnection);  
    adminCommand.ExecuteNonQuery();  
    adminAdapter = new AdsDataAdapter("SELECT Name FROM " +  
      "system.usergroups", adminConnection);  
    ds = new DataSet();   
    adminAdapter.Fill(ds);  
    dt = ds.Tables[0];  
    if (dt.Rows.Count == 0)   
    {  
      MessageBox.Show(this, "No groups to grant rights to");  
      return;  
    }  
    adminCommand = adminConnection.CreateCommand();  
    for (int i=0; i <= dt.Rows.Count - 1 ; i++)   
    {  
      dr = dt.Rows[i];  
      adminCommand.CommandText = "GRANT ALL ON " +   
        tabName + " TO \"" + dr[0].ToString() + "\"";  
      adminCommand.ExecuteNonQuery();  
    }  
  }  
  catch (System.Exception ex)   
  {  
    Console.WriteLine("Exception", ex);  
    throw(ex);  
  }  
  MessageBox.Show(this,  
    "The " + tabName + " table has been " +   
    "created, with rights granted to all groups");  
  return;  
}

This method begins by verifying that the table name does not include a semicolon, which could be used to convert the subsequent GRANT SQL statement into a SQL script. Since this value represents a table name, a parameterized query is not an option.

Next, this code verifies that the table does not already exist in the data dictionary. Once that is done, a new connection is created using the data dictionary administrative account. This connection is then used to call CREATE TABLE to create the table, and then to call GRANT for each group returned in the system.usergroups table.

   
NOTE: The administrative user name and passwords are represented by string literals in this code segment. This was done for convenience, but in a real application you would either ask for this information from the user or you would obfuscate this information so that it could not be retrieved.
