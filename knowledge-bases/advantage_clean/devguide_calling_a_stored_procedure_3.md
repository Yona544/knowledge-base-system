---
title: Devguide Calling A Stored Procedure 3
slug: devguide_calling_a_stored_procedure_3
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_calling_a_stored_procedure_3.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 37aa02b015a4d81d68f2058b59382d2ae6fb5cfb
---

# Devguide Calling A Stored Procedure 3

Calling a Stored Procedure

     Calling a Stored Procedure

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Calling a Stored Procedure  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Calling a stored procedure is no different than executing any other query. You can define a SQL EXECUTE PROCEDURE statement and assign it to the CommandText property of an AdsCommand object. Alternatively, you can assign the name of the stored procedure to the CommandText property of the AdsCommand object, and then set the CommandType property to CommandType.StoredProcedure.

You create an AdsCommand object explicitly or permit an AdsDataAdapter or an AdsConnection to create one for you. If the stored procedure returns a result set, you call the AdsCommand ExecuteReader method, or the Fill method of the AdsDataAdapter that refers to the AdsCommand in its SelectCommand property. If the stored procedure does not return a result set, execute it by calling the ExecuteNonQuery method of the AdsCommand.

Invoking a stored procedure that takes one input parameter is demonstrated by the following code associated with the Show 10% of Invoices button (shown in Figure 18-3). The stored procedure referenced in this code is the SQL stored procedure you created in Chapter 7, called SQLGet10Percent.

private void callStoredProc\_Click\_1(object sender,   
  System.EventArgs e) {  
  AdsCommand storedProcCommand;  
  IDataAdapter dataAdapter;  
  DataSet ds = new DataSet();  
  DataTable dt;  
  if (paramText.Text.Equals(""))   
  {  
    MessageBox.Show(this, "You must supply a customer ID");  
    return;  
  }  
  storedProcCommand = new AdsCommand("SQLGet10Percent",  
    connection);  
  storedProcCommand.CommandType =  
    CommandType.StoredProcedure;  
  storedProcCommand.Parameters.Add(1,  
    System.Data.DbType.Int32);  
  storedProcCommand.Parameters[0].Value =   
    Int32.Parse(paramText.Text);  
  dataAdapter = new AdsDataAdapter(storedProcCommand);  
  dataAdapter.Fill(ds);  
  dt = ds.Tables[0];  
  if (dt.Rows.Count == 0)   
  {  
    MessageBox.Show(this, "No invoices for customer ID");  
    return;  
  }  
  dataGrid1.DataSource = dt;   
}
