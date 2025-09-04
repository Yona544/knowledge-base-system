AX\_SetPassword()




Advantage Database Server 12  

AX\_SetPassword()

Advantage Visual Objects and Vulcan.NET RDD

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AX\_SetPassword()  Advantage Visual Objects and Vulcan.NET RDD |  |  | Feedback on: Advantage Database Server 12 - AX\_SetPassword() Advantage Visual Objects and Vulcan.NET RDD vo\_Ax\_setpassword Advantage Visual Objects and Vulcan.NET RDD > Developing Visual Objects and Vulcan.NET Applications > Advanced  Functions > AX\_SetPassword() / Dear Support Staff, |  |
| AX\_SetPassword()  Advantage Visual Objects and Vulcan.NET RDD |  |  |  |  |

Sets the password to be used for subsequent encryption/decryption operations.

Syntax

AX\_SetPassword( [<cString>] )

|  |  |
| --- | --- |
| <cString> | A character string indicating the password to be used in all subsequent encryption/decryption operations. The string may be up to 20 characters long. This value is case-sensitive. For example, a string encrypted with the password "BOGUS" would be different than if the password "bogus" were used. |

To clear the password, pass an empty string ("") as the parameter.

Note Make sure to trim all trailing spaces from the password before passing it on to the AX\_SetPassword() function, unless the spaces are intended to be part of the password.

Description

A single call to AX\_SetPassword() should be made to initiate encryption and decryption in the current work area.

After setting a password with AX\_SetPassword(), all new records appended or updated in the current work area will be encrypted as they are stored.

For additional security, the security code is stored in memory in an encrypted form. Therefore, the security code is not easily accessed at runtime.

Object-oriented Example

See [CLASS AxDBServer](vo_class_axdbserver.htm) for code sample for the AxDBServer class.

|  |
| --- |
| // Open TEST.DBF and set CRYPT as the encryption password for this |
| // workarea. Then, encrypt a record that will be added to the file. |
| oDB := AxDBServer{ "TEST", .f., .f., "DBFNTXAX" } |
| oDB:AX\_SetPassword( "CRYPT" ) |
|  |
| // Add a record which will be encrypted |
| oDB:Append() |
| oDB:LastName := "Flintstone" |

Procedural Example

|  |
| --- |
| USE test VIA "DBFNTXAX" |
| AX\_SetPassword( "CRYPT" ) |
|  |
| // Add a record which will be encrypted |
| Append Blank |
| Test->LastName := "Rubble" |