---
title: Devguide Changing A User Password 3
slug: devguide_changing_a_user_password_3
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_changing_a_user_password_3.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 5bbbb6fc360d2c0b9c573d1d048eeee6c72a98da
---

# Devguide Changing A User Password 3

Changing a User Password

     Changing a User Password

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Changing a User Password  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A user can change the password on their own connection, if you permit this. In most cases, only when every user has a distinct user name would you expose this functionality in a client application. When multiple users share a user name, this operation is usually reserved for an application administrator.

The following method, associated with the Change Password button (shown in Figure 18-3), demonstrates how you can permit a user to change their password from a client application:

private void changePasswordBtn\_Click(object sender,  
  System.EventArgs e)   
{  
  IDataReader dataReader;  
  String userName;  
  String oldPass, newPass, confirmPass;  
  oldPass = oldPassText.Text;  
  if (oldPass.Equals(""))  
  {  
   MessageBox.Show(this,  
    "Please enter your current password");  
   return;  
  }  
  newPass = newPassText.Text;  
  if (newPass.Equals(""))  
  {  
   MessageBox.Show(this,  
    "Please enter your new password");  
   return;  
  }  
  confirmPass = confirmPassText.Text;  
  if (confirmPass.Equals(""))  
  {  
   MessageBox.Show(this,  
    "Please confirm your new password");  
   return;  
  }  
  if (! newPass.Equals(confirmPass))  
  {  
   MessageBox.Show(this,  
    "New passwords do not match");  
   return;  
  }  
  if ((newPass.IndexOf(";") >= 0))   
  {  
   MessageBox.Show(this,  
    "Password may not contain a semicolon");  
   return;  
  }  
  //Get user name  
  command = connection.CreateCommand();  
  command.CommandText = "SELECT USER() FROM system.iota";  
  dataReader = command.ExecuteReader();  
  dataReader.Read();  
  userName = dataReader.GetString(0);  
  dataReader.Close();  
  //Verify current password  
  if (! CheckPassword(userName, oldPass))   
  {  
   MessageBox.Show("Cannot validate your current password. "  
     +"Cannot change password");  
   return;  
  }  
     
  try   
  {  
    command.CommandText =  "EXECUTE PROCEDURE " +   
      "sp\_ModifyUserProperty('" +   
      userName + "', 'USER\_PASSWORD', '" + newPass + "')";  
    command.ExecuteNonQuery();  
  }   
  catch (Exception ex)   
  {  
    MessageBox.Show(ex.Message);  
    return;  
  }  
  MessageBox.Show("Password successfully changed. " +   
    "New password will be valid next time you connect");  
}

A number of interesting tricks are used in this code. First, the user name is obtained by requesting the USER scalar function from the system.iota table. USER returns the user name on the connection through which the query is executed. Next, the user is asked for their current password, and the user name and password is used to attempt a new connection, which if successful confirms that the user is valid. This password validation is performed using the custom CheckPassword method. The following is the implementation of this method:

private Boolean CheckPassword(String uName, String pass)   
{  
  //Verify the current password  
  AdsConnection tempConnection;  
  tempConnection = new AdsConnection(  
    "Data Source=" + DataPath + ";user ID=" + uName + ";" +  
    "password=" + pass + ";" +   
    "ServerType=ADS\_LOCAL\_SERVER | ADS\_REMOTE\_SERVER;" +   
    "TrimTrailingSpaces=True");  
  try   
  {  
    tempConnection.Open();  
    tempConnection.Close();  
    return true;  
  }   
  catch (Exception)   
  {  
    return false;  
  }  
} //CheckPassword

Finally, the user is asked for their new password twice (for confirmation). If all is well, the sp\_ModifyUserProperty stored procedure is called to change the user's password. This password will be valid once the user terminates all connections on this user account.

   
NOTE: If you run this code, and change the password of the adsuser account, you should use the Advantage Data Architect to change the password back to password. Otherwise, you will not be able to run this project again since the password is hard-coded into the connection string.
