---
title: Devguide Using A Parameterized Query 3
slug: devguide_using_a_parameterized_query_3
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_using_a_parameterized_query_3.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 9d4ca082b577d1c4585daed1291e29873fa82f84
---

# Devguide Using A Parameterized Query 3

Using a Parameterized Query

     Using a Parameterized Query

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Using a Parameterized Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Parameterized queries are defined using an AdsCommand object. Before you can invoke a parameterized query, you must create one AdsParameter object for each of the query's parameters. You can create an AdsParameter instance by calling the Add method of the AdsCommand object's Parameters property.

The definition of a parameterized query, including the creation of a parameter, is shown in the following code segment, which is part of the private InitializeDataComponents method shown earlier:

paramCommand = new AdsCommand("SELECT \* FROM INVOICE " +  
  "WHERE [Customer ID] = ?", connection);  
paramCommand.Parameters.Add(1,System.Data.DbType.Int32);

Before you can execute an AdsCommand that contains a parameterized query, you must bind data to each of its parameters. This is shown in the following method, which is called by the Show Invoices button shown in Figure 18-3:

private void doParamQuery\_Click(object sender,   
  System.EventArgs e) {  
  IDataAdapter dataAdapter;  
  DataSet ds = new DataSet();  
  DataTable dt;  
  if (paramText.Text.Equals("")) {  
    MessageBox.Show(this,  
      "You must supply a customer ID");  
    return;  
  }  
  paramCommand.Parameters[0].Value =  
    Int32.Parse(paramText.Text);  
  dataAdapter = new AdsDataAdapter(paramCommand);  
  dataAdapter.Fill(ds);  
  dt = ds.Tables[0];  
  if (dt.Rows.Count == 0)  
  {  
    MessageBox.Show(this,  
      "No invoices for customer ID");  
    return;  
  }  
  dataGrid1.DataSource = dt;  
}

As you can see from this code, after verifying that a value has been entered into the Customer ID field, the entered data is assigned to the Value property of the AdsParameter. The AdsCommand object that holds the parameter is passed as an argument to an AdsDataAdapter, which then executes the query and assigns the result set to a DataTable (using the Fill method). Note that it was not necessary to pass a connection object to the AdsDataAdapter constructor, since the AdsCommand object itself was constructed based on a connection.

This is actually a classic example of how parameterized queries are used. Specifically, the query text is defined only once, but can be executed repeatedly. And by changing only the value of the parameter, a different result set can be returned upon each execution.
