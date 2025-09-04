---
title: Devguide Changing A User Password
slug: devguide_changing_a_user_password
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_changing_a_user_password.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 2a25ae6f4038c2477fc0241ba6b6c6cdb6b425da
---

# Devguide Changing A User Password

Changing a User Password

     Changing a User Password

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Changing a User Password  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A user can change the password on the users own connection, if you permit this change. In most cases, only when every user has a distinct user name would you expose this functionality in a client application. When multiple users share a user name, this operation is usually reserved for an application administrator.

As was done in the preceding section, this code demonstrates changing a user password using an AdsDictionary component. For an example of changing a password using the sp\_ModifyUserProperty stored procedure, refer to Chapters 1618.

procedure TForm1.ChangePasswordBtnClick(Sender: TObject);  
var  
  UserName: String;  
  OldPass: String;  
  NewPass1: String;  
  NewPass2: String;  
  {$HINTS OFF}  
  function CheckPass(UName, UPass: String): Boolean;  
  var  
    TempConnection: TAdsConnection;  
  begin  
    result := False;  
    TempConnection := TAdsConnection.Create(nil);  
    try  
      TempConnection.AliasName := AdsConnection1.AliasName;  
      TempConnection.AdsServerTypes :=  
        AdsConnection1.AdsServerTypes;  
      TempConnection.Username := UName;  
      TempConnection.Password := UPass;  
      TempConnection.LoginPrompt := False;  
      try  
        TempConnection.IsConnected := True;  
      except  
        result := False;  
      end;  
      result := True;  
    finally  
       TempConnection.IsConnected := False;  
       TempConnection.Free;  
    end;  
  end; //CheckPass  
  {$HINTS ON}  
   
begin  
  UserName := AdsConnection1.Username;  
  OldPass := 'Enter password';  
  OldPass := InputBox('Password',   
  'Enter your current password', OldPass);  
  if OldPass = 'Enter password' then Exit;  
   
  if not CheckPass(UserName, OldPass) then  
  begin  
    ShowMessage('Cannot validate your current password. ' +  
      'Cannot change password');  
    Exit;  
  end;  
   
  NewPass1 := '';  
  NewPass2 := '';  
  NewPass1 := InputBox('Password',   
    'Enter your new Password', NewPass1);  
  if NewPass1 = '' then  
  begin  
    ShowMessage('Password cannot be blank. ' +  
      'Cannot change password');  
    Exit;  
  end;  
  NewPass2 := InputBox('Password',   
    'Confirm your new password', NewPass2);  
  if NewPass1 <> NewPass2 then  
  begin  
    ShowMessage('Passwords did not match. ' +  
      'Cannot change password');  
    Exit;  
  end;  
   
  //Connect AdsDictionary1 and change password  
  AdsDictionary1.AliasName := AdsConnection1.AliasName;  
  AdsDictionary1.AdsServerTypes :=  
    AdsConnection1.AdsServerTypes;  
  AdsDictionary1.UserName := AdsConnection1.Username;  
  AdsDictionary1.Password := OldPass;  
  AdsDictionary1.LoginPrompt := False;  
  AdsDictionary1.Connect;  
  AdsDictionary1.SetUserProperty(AdsConnection1.Username,  
    ADS\_DD\_USER\_PASSWORD, PChar(NewPass1),  
    (StrLen(PChar(NewPass1)) + 1));  
  AdsDictionary1.Disconnect;  
   
  ShowMessage('Password successfully changed. ' +  
    'New password will be valid next time you connect');  
end;

This code segment is a bit simpler than the preceding one. After verifying that the user knows the current password with which they are connected, they are prompted for their new password twice, for confirmation purposes. Next, the AdsDictionary component is configured to connect with the user account, after which its SetUserProperty method is invoked to change the user's password. As the final dialog box displayed by this event handler indicates, this password will be valid once the user terminates all connections on this user account.

   
NOTE: If you run this code, and change the password of the adsuser account, you should use the Advantage Data Architect to change the password back to password. Otherwise, you will not be able to run this project again, since the literal 'password' is assigned to the Password property of the AdsConnection component in this project.
