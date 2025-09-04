---
title: Master Sp Encrypttable
slug: master_sp_encrypttable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_encrypttable.htm
source: Advantage CHM
tags:
  - master
checksum: 4df781edf767bd5e8a8e93215a753435e47f66e3
---

# Master Sp Encrypttable

sp\_EncryptTable

sp\_EncryptTable

Advantage SQL Engine

| sp\_EncryptTable  Advantage SQL Engine |  |  |  |  |

Encrypts a table.

 

Syntax

sp\_EncryptTable(

 TableName,Character,515 )

sp\_EncryptTable(

 TableName,Character,515,

 Password,Character,20 )

Parameters

| TableName (I) | Name of table to encrypt.  This can include path information for free tables if the table is in a different folder from the connection path. |
| Password (I) | The password to use when encrypting free tables. For data dictionary bound tables, this parameter is not specified. |

Remarks

sp\_EncryptTable can be used to encrypt data dictionary tables and free tables. When using [AES encryption](master_encryption.md), a different file format is required and this procedure will update the table as needed for the encryption type. This procedure, in conjunction with sp\_DecryptTable, can be used to convert tables between different encryption types.

For free tables, the encryption type used for the encryption is the one specified by the [EncryptionType connection string option](ace_adsconnect101.md) for the connection. For data dictionary tables, the encryption type will match that of the dictionary (the EncryptionType specified when the dictionary was created).

Example

-- Change the encryption type of an encrypted free table to the connection's current  
-- encryption type:  
EXECUTE PROCEDURE sp\_DecryptTable( 'sometable.adt', 'password' );  
EXECUTE PROCEDURE sp\_EncryptTable( 'sometable.adt', 'password' );

See Also

[sp\_DecryptTable](master_sp_decrypttable.md)

[sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md)

[Encryption Overview](master_encryption.md)
