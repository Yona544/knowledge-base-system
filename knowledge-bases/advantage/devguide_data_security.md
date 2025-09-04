Data Security




Advantage Database Server 12  

     Data Security

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Data Security  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      Data Security Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_Data\_Security Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 2 - Creating Tables > Data Security / Dear Support Staff, |  |
| Data Security  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Advantage provides security for your data in a number of important ways. Some of these are associated with how Advantage transmits data across the network, and others are associated with access rights conferred by a data dictionary. But the most fundamental of data security features is provided at the table level. Specifically, individual tables can be encrypted with a password.

When a table is encrypted with a password, both the table and its memo file are encoded using the password. (If you are using a data dictionary and ADT tables, it is possible to also have the index encrypted.) The effect of this encoding is that the raw table and memo files appear scrambled to anyone who attempts to view their contents. Without encryption, it would be possible for someone with a file viewer, or even Windows Notepad (for small tables), to open the table and view its contents.

Once the table is encrypted, you must provide the password for the table each time the table is opened. For database tables, which can only be accessed through a data dictionary, the data dictionary supplies the password automatically. Note, however, that a data dictionary itself provides security, and when the data dictionary is configured correctly, you will not be able to access the data dictionary without supplying a user name and password. The data dictionary user name and password are separate from a table's password.

If you want to view an encrypted free table using the Advantage Data Architect, you will be prompted for the password when you open the table. Similarly, before an encrypted table can be accessed from a client application, that application must submit the password.

How you submit a table's password from a client application depends on the data access mechanism you are using. For example, if you are using the ACE API, you must make a call to AdsEnableEncryption (for Advantage tables) or AdsStmtSetTablePassword (for executing SQL statements against the table), passing the table name or handle and the password as the arguments to the function call. You need to make one of these calls once per Advantage table, prior to accessing it.

The following section describes how to encrypt and decrypt a free Advantage table. For information about encrypting database tables, see Chapter 4.

   
NOTE: Encrypting or removing encryption from a table requires exclusive access. Specifically, if a table is already in use by at least one other user, you will not be permitted to either encrypt or decrypt that table. Submitting a password to access an encrypted table, however, is something that can be done in shared mode.  
 

Encrypting ADS Tables

To encrypt an Advantage table, open that table in the Table Browser. Then select Encrypt from the Table Browser's context menu. Use the following steps to encrypt the CUST.ADT table created earlier in this chapter:

If CUST.ADT is currently open in the Table Browser, right-click Table Browser and select Encrypt from the displayed context menu. If CUST.ADT is not open, right-click the CUST.ADT entry in the TABLES node of the FreeTableConnection and select Encrypt from the display context menu. The Advantage Data Architect responds by displaying the Encryption Password dialog box, shown in Figure 2-6.

Figure 2-6: The Encryption Password dialog box

You use this dialog box to enter the table encryption password twice, the second time for verification purposes. In the Password field, enter the value password. Confirm this password by entering password in the Confirmation field. Click OK when you are done.

   
NOTE: The simple password "password" is used throughout this book since it is one that is easy to remember. This password is a very poor choice for use in a real application since it is also easy to guess. String passwords should be difficult to guess, and should contain both letters and numbers. Advantage table passwords can be up to 20 characters in length. The longer the password, the stronger the table encryption.  
 

   
CAUTION: You should take steps to protect and remember any passwords you use to encrypt your tables. If you forget the password for a free table, its data will be inaccessible. You should write your passwords down, and place them in a secure location such as a safety deposit box or safe that only trusted individuals have access to.  
 

When encrypting a table, you can also just right-click the table in the Connection Repository and select Encrypt. The Advantage Data Architect will attempt to get exclusive access to the table and either display the Encryption password dialog box or provide a message that exclusive access cannot be obtained. However, this technique is best done during design (or not in a multiuser environment) so that you know that exclusive access to a table can be obtained.

Once a table is encrypted, a picture of a padlock will appear in the status bar of the Table Browser when you are viewing the table.

Use the following steps to see the effects of encryption:

If the CUST.ADT table is currently open in the Table Browser, close it.

Double-click CUST.ADT from the TABLES node of the FreeTableConnection connection in the Connection Repository. The Advantage Data Architect displays the Encryption Password dialog box:

Enter password and click OK. When the Table Browser opens the table, the unencrypted data is visible and can be edited.

Decrypting ADS Tables

You can easily decrypt and remove the password from a previously encrypted table, if you wish. With the encrypted table open in the Table Browser, right-click the Table Browser and select Decrypt from the displayed context menu. Alternatively, you can select the table from the TABLES node in the Connection Repository, then right-click and select Decrypt from the display context menu.

When you select Decrypt, the Encryption Password dialog box is displayed as long as the Advantage Data Architect can get exclusive access to the table. (You will get a message if exclusive access cannot be obtained.) Enter the table's current password into this dialog box to decrypt the table. Note that you need exclusive access to a table to decrypt it.

Since the CUST.ADT table is one that we are using for demonstration purposes only, the following steps demonstrate how to remove the encryption. This will permit you to work with this table without having to continually provide a password.

With the CUST.ADT open in the Table Browser, right-click in the Table Browser and select Decrypt. The Encryption Password dialog box is displayed.

Enter password in the Password field and then click OK to decrypt the CUST.ADT table.