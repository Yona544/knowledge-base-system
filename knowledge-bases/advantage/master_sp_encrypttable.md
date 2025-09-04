sp\_EncryptTable




Advantage Database Server 12  

sp\_EncryptTable

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_EncryptTable  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_EncryptTable Advantage SQL Engine master\_sp\_EncryptTable Advantage SQL > System Procedures > Procedures > sp\_EncryptTable / Dear Support Staff, |  |
| sp\_EncryptTable  Advantage SQL Engine |  |  |  |  |

Encrypts a table.

 

Syntax

sp\_EncryptTable(

 TableName,Character,515 )

sp\_EncryptTable(

 TableName,Character,515,

 Password,Character,20 )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name of table to encrypt.  This can include path information for free tables if the table is in a different folder from the connection path. |
| Password (I) | The password to use when encrypting free tables. For data dictionary bound tables, this parameter is not specified. |

Remarks

sp\_EncryptTable can be used to encrypt data dictionary tables and free tables. When using [AES encryption](master_encryption.htm), a different file format is required and this procedure will update the table as needed for the encryption type. This procedure, in conjunction with sp\_DecryptTable, can be used to convert tables between different encryption types.

For free tables, the encryption type used for the encryption is the one specified by the [EncryptionType connection string option](ace_adsconnect101.htm) for the connection. For data dictionary tables, the encryption type will match that of the dictionary (the EncryptionType specified when the dictionary was created).

Example

-- Change the encryption type of an encrypted free table to the connection's current  
-- encryption type:  
EXECUTE PROCEDURE sp\_DecryptTable( 'sometable.adt', 'password' );  
EXECUTE PROCEDURE sp\_EncryptTable( 'sometable.adt', 'password' );

See Also

[sp\_DecryptTable](master_sp_decrypttable.htm)

[sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm)

[Encryption Overview](master_encryption.htm)