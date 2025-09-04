---
title: Devguide Using A Parameterized Query 1
slug: devguide_using_a_parameterized_query_1
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_using_a_parameterized_query_1.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: b2468d74d8912096eedbde3a108fe78e0326e7f4
---

# Devguide Using A Parameterized Query 1

Using a Parameterized Query

     Using a Parameterized Query

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Using a Parameterized Query  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Instead of using a Statement object, you use a PreparedStatement object when you need to execute a parameterized query. You can create a PreparedStatement object by calling the prepareStatement method of a Connection object, passing the parameterized query as an argument.

Before executing the PreparedStatement, you must call one of its setter methods for each parameter in the query. Which setter method you call depends on the data type of the parameter. If the parameter is a String, you call setString. On the other hand, if the parameter is an Integer, you call setInt.

The PreparedStatement was created in the databaseInit method shown earlier in this chapter. Data is bound to the single parameter and the query is executed from the following event handler, which is associated with the Show Invoices button (shown in Figure 16-1):

void showInvoiceBtn\_actionPerformed(ActionEvent e) {  
  try{  
    prepStmt.setInt( 1,  
      Integer.parseInt(paramText.getText()));  
    ResultSet rs = prepStmt.executeQuery();  
    if (isRSEmpty(rs)) {  
      JOptionPane.showMessageDialog(this,  
       "No records in result set");  
      return;  
    }  
    jTable1.setModel(new ResultTableModel(rs));  
  }  
  catch (Exception e1) {  
    System.err.println( e1.getMessage());  
  }  
}
