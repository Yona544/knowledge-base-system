sp\_DecryptTable




Advantage Database Server 12  

sp\_DecryptTable

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_DecryptTable  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_DecryptTable Advantage SQL Engine master\_sp\_DecryptTable Advantage SQL > System Procedures > Procedures > sp\_DecryptTable / Dear Support Staff, |  |
| sp\_DecryptTable  Advantage SQL Engine |  |  |  |  |

Decrypts a table.

 

Syntax

sp\_DecryptTable(

 TableName,Character,515 )

sp\_DecryptTable(

 TableName,Character,515,

 Password,Character,20 )

Parameters

|  |  |
| --- | --- |
| TableName (I) | Name of table to decrypt.  This can include path information for free tables if the table is in a different folder from the connection path. |
| Password (I) | The password to use when decrypting free tables. For data dictionary bound tables, this parameter is not specified. |

Remarks

sp\_DecryptTable can be used to decrypt data dictionary tables and free tables. This procedure, in conjunction with sp\_EncryptTable, can be used to convert tables between different encryption types.

Example

-- Change the encryption type of an encrypted free table to the connection's current  
-- encryption type:  
EXECUTE PROCEDURE sp\_DecryptTable( 'sometable.adt', 'password' );  
EXECUTE PROCEDURE sp\_EncryptTable( 'sometable.adt', 'password' );

See Also

[sp\_EncryptTable](master_sp_encrypttable.htm)

[sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm)

[Encryption Overview](master_encryption.htm)