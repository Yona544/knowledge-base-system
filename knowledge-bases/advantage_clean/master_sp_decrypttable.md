---
title: Master Sp Decrypttable
slug: master_sp_decrypttable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_decrypttable.htm
source: Advantage CHM
tags:
  - master
checksum: ab9f82e6bd809f197ce2d00570ba034b009fc0da
---

# Master Sp Decrypttable

sp\_DecryptTable

sp\_DecryptTable

Advantage SQL Engine

| sp\_DecryptTable  Advantage SQL Engine |  |  |  |  |

Decrypts a table.

 

Syntax

sp\_DecryptTable(

 TableName,Character,515 )

sp\_DecryptTable(

 TableName,Character,515,

 Password,Character,20 )

Parameters

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

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md)

[Encryption Overview](master_encryption.md)
