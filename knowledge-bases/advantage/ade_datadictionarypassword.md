DataDictionaryPassword




Advantage Database Server 12  

TAdsConnection.EncryptionOptions.DataDictionaryPassword

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.EncryptionOptions.DataDictionaryPassword  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.EncryptionOptions.DataDictionaryPassword Advantage TDataSet Descendant Ade\_DataDictionaryPassword Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.EncryptionOptions.DataDictionaryPassword  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies the data dictionary password for a dictionary encrypted with AES.

Syntax

property EncryptionOptions.DataDictionaryPassword: String;

Description

Specifies the AES password for the dictionary if using [strong encryption](master_encryption.htm). When connecting to Advantage Database Server, it is more secure to use the [SE\_PASSWORDS](master_se_passwords.htm) configuration option to specify this value. Note that if an application does provide this option, the server will validate the password each time a connection is made. This is a relatively expensive operation due to the large number of iterations the hash function is executed.