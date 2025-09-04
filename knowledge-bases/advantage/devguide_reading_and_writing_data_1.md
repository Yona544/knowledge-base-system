Reading and Writing Data




Advantage Database Server 12  

     Reading and Writing Data

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Reading and Writing Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Reading and Writing Data Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Reading\_and\_Writing\_Data\_1 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 16 - Advantage and Java > Reading and Writing Data / Dear Support Staff, |  |
| Reading and Writing Data  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You access individual columns in a ResultSet by calling one of its getter methods. All ResultSet getter methods are overloaded. You can identify a column either by ordinal position or by name.

Which getter method you call depends on the data type of the column you are reading. For example, you call getString in order to read a column containing text, and getBoolean to read a logical column.

If the result set is based on a live (dynamic) cursor, you can change its data and apply the change to the underlying Advantage table. You write to a column of a ResultSet by calling one of its setter methods. Like getter methods, ResultSet setter methods are overloaded, taking either the ordinal position of a field or the field name, in addition to the value you are writing to the field.

Once you have written to one or more fields of an updatable ResultSet record, you apply the changes to the underlying table by calling the ResultSet's updateRow method.

The following event handler, associated with the Get Address button (shown in Figure 16-1), demonstrates how to read a field from a ResultSet:

void getAddressBtn\_actionPerformed(ActionEvent e) {  
  PreparedStatement getCustStmt;  
  if (custNoText.getText() == "") {  
    System.out.println("Enter a customer ID");  
    return;  
  }  
  try {  
    getCustStmt = conn.prepareStatement(  
      "SELECT \* FROM CUSTOMER WHERE [customer id] = ?" );  
    getCustStmt.setInt( 1,  
      Integer.parseInt(custNoText.getText()));  
    ResultSet rs = getCustStmt.executeQuery();  
    if (isRSEmpty(rs)) {  
      JOptionPane.showMessageDialog(this,  
       "No records in result set");  
      jTable1.setModel(new ResultTableModel(null));  
      return;  
    }  
    oldAddressText.setText(rs.getString("Address"));  
    jTable1.setModel(new ResultTableModel(rs));  
  }  
  catch (Exception e1) {  
    System.err.println( e1.getMessage());  
  }  
}

The next event handler, associated with the Set New Address button (shown in Figure 16-1), demonstrates writing to a field and saving the change to ADS:

void setAddressBtn\_actionPerformed(ActionEvent e) {  
  PreparedStatement getCustStmt;  
  if (custNoText.getText() == "") {  
    System.out.println("Enter a customer ID");  
    return;  
  }  
  try {  
    getCustStmt = conn.prepareStatement(  
      "SELECT \* FROM CUSTOMER WHERE [customer id] = ?" );  
    getCustStmt.setInt( 1,  
      Integer.parseInt(custNoText.getText()));  
    ResultSet rs = getCustStmt.executeQuery();  
    if (isRSEmpty(rs)) {  
      JOptionPane.showMessageDialog(this,  
       "No records in result set");  
      return;  
    }  
    rs.updateString("Address", newAddressText.getText());  
    rs.updateRow();  
  }  
  catch (Exception e1) {  
    System.err.println( e1.getMessage());  
  }  
}