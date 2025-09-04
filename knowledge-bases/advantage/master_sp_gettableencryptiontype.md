sp\_GetTableEncryptionType




Advantage Database Server 12  

sp\_GetTableEncryptionType

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| sp\_GetTableEncryptionType  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - sp\_GetTableEncryptionType Advantage SQL Engine master\_sp\_GetTableEncryptionType Advantage SQL > System Procedures > Procedures > sp\_GetTableEncryptionType / Dear Support Staff, |  |
| sp\_GetTableEncryptionType  Advantage SQL Engine |  |  |  |  |

Returns the encryption type for a table.

Syntax

sp\_GetTableEncryptionType( TableName,CHARACTER,515 );

Parameters

TableName (I)        Name (and optional path) of table

Output

The sp\_GetTableEncryptionType procedure returns a result set containing the following information for the specified table.

|  |  |  |  |
| --- | --- | --- | --- |
| Field Name | Field Type | Field Size | Description |
| EncryptionType | Character | 10 | Returns the current encryption type for the connection. Values are AES128, AES256, or RC4. |

See Also

[sp\_EncryptTable](master_sp_encrypttable.htm)

[sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm)

[Encryption Overview](master_encryption.htm)