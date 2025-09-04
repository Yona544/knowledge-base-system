Changing a User Password




Advantage Database Server 12  

     Changing a User Password

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Changing a User Password  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Changing a User Password Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Changing\_a\_User\_Password\_1 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 16 - Advantage and Java > Changing a User Password / Dear Support Staff, |  |
| Changing a User Password  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A user can change the password on their own connection, if you permit this. In most cases, only when every user has a distinct user name would you expose this functionality in a client application. When multiple users share a user name, this operation is usually reserved for an application administrator.

The following event handler, associated with the Change Password button (shown in Figure 16-1), demonstrates how you can permit a user to change their password from a client application:

void changePasswordBtn\_actionPerformed(ActionEvent e) {  
  String userName;  
  String oldPass;  
  String newPass1;  
  String newPass2;  
  try {  
    ResultSet rs = stmt.executeQuery("SELECT USER() as " +  
     "Name FROM system.iota");  
    rs.first();  
    userName = rs.getString("Name");  
    oldPass = JOptionPane.showInputDialog(this,  
      "Enter your current password");  
    if (oldPass.equals("")) {  
      return;  
    }  
    try {  
      Connection tempcon =  
        DriverManager.getConnection(  
        "jdbc:extendedsystems:advantage://server:6262/" +   
        "share/adsbook/demodictionary.add;user=" +   
        userName +";password=" + oldPass);  
    }  
    catch (Exception e1) {  
      JOptionPane.showMessageDialog(this,  
          "Invalid password. Cannot change password");  
      return;  
    }  
    //Check for semicolon hack  
    newPass1 = JOptionPane.showInputDialog(this,  
      "Enter your new password");  
    if (! (newPass1.indexOf(";") == -1)) {  
      JOptionPane.showMessageDialog(this,  
        "Password may not contain a semicolon");  
      return;  
    }  
    newPass2 = JOptionPane.showInputDialog(this,  
      "Confirm your new password");  
    if (!newPass1.equals(newPass2)) {  
      JOptionPane.showMessageDialog(this,  
          "Passwords did not match. " + "  
            Cannot change password");  
      return;  
    }  
    stmt.executeUpdate("EXECUTE PROCEDURE "   
      +"sp\_ModifyUserProperty('"+  
      userName + "', 'USER\_PASSWORD', '" + newPass1 + "')");  
    JOptionPane.showMessageDialog(this,  
      "Password successfully changed. " +  
        "New password will be valid next time you connect");  
  } catch (Exception e1) {  
    System.out.println(e1.getMessage());  
  }  
}

A number of interesting tricks are used in this code. First, the user name is obtained by requesting the USER scalar function from the system.iota table. USER returns the user name on the connection through which the query is executed. Next, the user is asked for their current password, and the user name and password are used to attempt a new connection, which, if successful, confirms that the user is valid.

Finally, the user is asked for their new password twice (for confirmation). If all is well, the sp\_ModifyUserProperty stored procedure is called to change the user's password. As the final dialog box displayed by this event handler indicates, this password will be valid once the user terminates all connections on this user account.

   
NOTE: If you run this code, and change the password of the adsuser account, you should use the Advantage Data Architect to change the password back to password. Otherwise, you will not be able to run this project again, since the password is hard-coded into the connection string.