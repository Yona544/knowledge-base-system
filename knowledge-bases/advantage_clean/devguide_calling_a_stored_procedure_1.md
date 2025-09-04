---
title: Devguide Calling A Stored Procedure 1
slug: devguide_calling_a_stored_procedure_1
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_calling_a_stored_procedure_1.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 67b5309ebde1074fba7038feb2dc37bb629e28d4
---

# Devguide Calling A Stored Procedure 1

Calling a Stored Procedure

     Calling a Stored Procedure

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Calling a Stored Procedure  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Calling a stored procedure is no different than executing any other query. If your stored procedure does not require input parameters, you use a Statement instance. You use a PreparedStatement instance if there are one or more input parameters. If the stored procedure returns one or more records, you invoke the executeQuery method of the Statement or PreparedStatement object, and you invoke the execute or the executeUpdate methods when the stored procedure does not return records.

Invoking a stored procedure that takes one input parameter is demonstrated by the following code associated with the actionPerformed event handler for the Show 10% of Invoices button (shown in Figure 16-1). The stored procedure referenced in this code is the SQL stored procedure created in Chapter 7. If you did not create this stored procedure, but created one of the other stored procedures described in that chapter, substitute the name of the stored procedure object in your data dictionary in the EXECUTE PROCEDURE string, like this:

void callStoredProcBtn\_actionPerformed(ActionEvent e) {  
  PreparedStatement getCustStmt;  
  if (custNoText.getText() == "") {  
    System.out.println("Enter a customer ID");  
    return;  
  }  
  try {  
    getCustStmt = conn.prepareStatement(  
      "EXECUTE PROCEDURE SQLGet10Percent( ? )" );  
    getCustStmt.setInt( 1,  
      Integer.parseInt(paramText.getText()));  
    ResultSet rs = getCustStmt.executeQuery();  
    if (isRSEmpty(rs)) {  
      jTable1.setModel(new ResultTableModel(null));  
      JOptionPane.showMessageDialog(this,  
       "No records in result set");  
      return;  
    }  
    jTable1.setModel(new ResultTableModel(rs));  
  }  
  catch (Exception e1) {  
    JOptionPane.showMessageDialog(this,  
      e1.getMessage());  
  }  
}
