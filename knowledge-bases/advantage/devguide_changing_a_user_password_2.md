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
| Changing a User Password  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Changing a User Password Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Changing\_a\_User\_Password\_2 Advantage Developer's Guide > Part III - Accessing Advantage Data > Chapter 17 - MDAC, OLE DB, ADO > Changing a User Password / Dear Support Staff, |  |
| Changing a User Password  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A user can change the password on their own connection, if you permit this. In most cases, only when every user has a distinct user name would you expose this functionality in a client application. When multiple users share a user name, this operation is usually reserved for an application administrator.

The following subprocedure, associated with the Change Password button (shown in Figure 17-1), demonstrates how you can permit a user to change their password from a client application:

Dim UserName As String  
Dim OldPass As String  
Dim NewPass1 As String  
Dim NewPass2 As String  
If AdsRecordset.State = adStateOpen Then  
  AdsRecordset.Close  
End If  
AdsRecordset.Open "SELECT USER() FROM system.iota", \_  
  AdsConnection, adOpenDynamic, adLockPessimistic, adCmdText  
UserName = AdsRecordset.Fields(0).Value  
AdsRecordset.Close  
OldPass = InputBox("Enter your current password")  
If OldPass = "" Then Exit Sub  
If Not CheckPass(UserName, OldPass) Then  
  MsgBox "Cannot validate your current password. " + \_  
    "Cannot change password"  
  Exit Sub  
End If  
'Get new password  
NewPass1 = InputBox("Enter your new password")  
If NewPass1 = "" Then  
  MsgBox "Password cannot be blank. Cannot change password"  
  Exit Sub  
End If  
'Check for semicolon hack  
If InStr(1, NewPass1, ";", vbTextCompare) <> 0 Then  
  MsgBox "Password may not contain a semicolon"  
  Exit Sub  
End If  
NewPass2 = InputBox("Confirm your new password")  
If NewPass1 <> NewPass2 Then  
  MsgBox "Passwords did not match. Cannot change password"  
  Exit Sub  
End If  
'Green light to change password  
AdsCommand.CommandText = \_  
  "EXECUTE PROCEDURE sp\_ModifyUserProperty('" + UserName + \_  
  "', 'USER\_PASSWORD', '" + NewPass1 + "')"  
AdsCommand.Execute  
MsgBox "Password successfully changed. " + \_  
  "New password will be valid next time you connect"

A number of interesting tricks are used in this code. First, the user name is obtained by requesting the USER scalar function from the system.iota table. USER returns the user name on the connection through which the query is executed. Next, the user is asked for their current password, and the user name and password are used to attempt a new connection, which, if successful, confirms that the user is valid. This validation occurs in a subfunction named CheckPass. The following code is found in this function:

Private Function CheckPass(UName As String, \_  
  Pass As String) As Boolean  
  Dim TempConnection As ADODB.Connection  
  On Error GoTo ErrorHandler  
  'Try to make a new connection using this password  
  Set TempConnection = New ADODB.Connection  
  TempConnection.ConnectionString = \_  
    "Provider=Advantage OLE DB Provider;" + \_  
    "Data Source=" + DataPath + ";user ID=" + UName + ";" \_  
    + "password=" + Pass + ";" + \_  
    "ServerType=ADS\_LOCAL\_SERVER | ADS\_REMOTE\_SERVER;"  
  TempConnection.Open  
  'Password must be ok. Close TempConnection  
  TempConnection.Close  
  CheckPass = True  
  Exit Function  
ErrorHandler:  
  CheckPass = False  
End Function

Finally, the user is asked for their new password twice (for confirmation). If all is well, the sp\_ModifyUserProperty stored procedure is called to change the user's password. This password will be valid once the user terminates all connections on this user account.

   
NOTE: If you run this code, and change the password of the adsuser account, you should use the Advantage Data Architect to change the password back to password; otherwise, you will not be able to run this project again since the password is hard-coded into the connection string.