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
| Creating a Table and Granting Rights to It  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Creating a Table and Granting Rights to It Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Creating\_a\_Table\_and\_Granting\_Rights\_to\_It\_1 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 16 - Advantage and Java > Creating a Table and Granting Rights to It / Dear Support Staff, |  |
| Creating a Table and Granting Rights to It  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The AdsJava project permits a user to enter the name of a table that will be created in the data dictionary, after which all groups will be granted rights to the table. This operation is demonstrated in the following event handler, which is associated with the actionPerformed event of the Create Table and Grant Rights button (shown in Figure 16-1):

void createTableBtn\_actionPerformed(ActionEvent e) {  
  boolean found = false;  
  Connection adminconn;  
  Statement adminstmt;  
  Statement grantstmt;  
  ResultSet rs;  
  String tn = tableNameText.getText();  
  //Check for semicolon hack  
  if (! (tn.indexOf(";") == -1)) {  
    JOptionPane.showMessageDialog(this,  
      "Table name may not contain a semicolon");  
    return;  
  }  
  if (tableNameText.getText().equals("")) {  
     JOptionPane.showMessageDialog(this,  
       "Please enter a table name");  
    return;  
  }  
  try {  
    adminconn = DriverManager.getConnection(  
      "jdbc:extendedsystems:advantage://server:6262/share"+  
      "/adsbook/"demodictionary.add;" +  
      "user=adssys;password=password");  
    adminstmt = adminconn.createStatement();  
    rs =  
      adminstmt.executeQuery(  
        "SELECT NAME FROM system.tables");  
    String tabName;  
    if (! isRSEmpty(rs)) {  
      rs.first();  
      do {  
        tabName = rs.getString("Name");  
        if (tabName.equalsIgnoreCase(tn)) {  
         found = true;  
         break;  
        }  
      } while (rs.next());  
    }  
    if (found) {  
      JOptionPane.showMessageDialog(this,  
        "Table already exists. Cannot create");  
      return;  
    }  
    adminstmt.executeUpdate("CREATE TABLE " + tn +  
      "([Full Name] CHAR(30)," +  
      "[Date of Birth] DATE," +  
      "[Credit Limit] MONEY, " +  
      "Active LOGICAL)");  
    rs = adminstmt.executeQuery(  
      "SELECT \* FROM system.usergroups");  
    if (isRSEmpty(rs)) {  
      JOptionPane.showMessageDialog(this,  
        "No groups to grant rights to");  
      return;  
    }  
    grantstmt = adminconn.createStatement();  
    rs.first();  
    do {  
      grantstmt.executeUpdate("GRANT ALL ON [" + tn + "]" +  
        " TO [" +  rs.getString("Name") + "]");  
    } while (rs.next());  
    JOptionPane.showMessageDialog(this, "The " +   
      tn + " table " +  
      "has been created, with rights granted to all groups");  
  } catch (Exception e1) {  
    System.out.println(e1.getMessage());  
  }  
}

This event handler begins by verifying that the table name does not include a semicolon, which could be used to introduce a SQL injection attack. Since this value represents a table name, using a parameterized query (the common method used to avoid injection attacks) is not an option.

Next, this code verifies that the table does not already exist in the data dictionary. Once that is done, a new connection is created using the data dictionary administrative account. This connection is then used to call CREATE TABLE to create the table, and then to call GRANT for each group returned in the system.usergroups table.

   
NOTE: The administrative user name and passwords are represented by string literals in this code segment. This was done for convenience, but in a real application you would either ask for this information from the user, or you would obfuscate this information so that it could not be retrieved.