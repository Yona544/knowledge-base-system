7060 Invalid Password




Advantage Database Server 12  

7060 Invalid Password

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7060 Invalid Password  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7060 Invalid Password Advantage Error Guide error\_7060\_invalid\_password Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7060 Invalid Password  Advantage Error Guide |  |  |  |  |

Problem: An invalid or incorrect password was specified when enabling encryption. Thus, the encryption is not enabled and the encrypted records in the table cannot be decrypted or updated.

Solution: Specify a valid password when enabling encryption. The encryption password of a table is set the first time encryption is enabled on the table by a user. The password can be cleared by decrypting the table with the correct password.

Problem: An invalid password for [AES encryption](master_encryption.htm) was provided via the [SE\_Passwords](master_se_passwords.htm) server configuration option or the equivalent /SEPasswords command line parameter.

Solution: Verify that the SE\_Passwords configuration parameter value is correct. The error log should show which dictionary or table the invalid password was applied to.