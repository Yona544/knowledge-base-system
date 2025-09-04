---
title: Master Sp Gettableencryptiontype
slug: master_sp_gettableencryptiontype
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_gettableencryptiontype.htm
source: Advantage CHM
tags:
  - master
checksum: d8b4770a8ea3b3fd19e0eb2855050288606a5f49
---

# Master Sp Gettableencryptiontype

sp\_GetTableEncryptionType

sp\_GetTableEncryptionType

Advantage SQL Engine

| sp\_GetTableEncryptionType  Advantage SQL Engine |  |  |  |  |

Returns the encryption type for a table.

Syntax

sp\_GetTableEncryptionType( TableName,CHARACTER,515 );

Parameters

TableName (I)        Name (and optional path) of table

Output

The sp\_GetTableEncryptionType procedure returns a result set containing the following information for the specified table.

| Field Name | Field Type | Field Size | Description |
| EncryptionType | Character | 10 | Returns the current encryption type for the connection. Values are AES128, AES256, or RC4. |

See Also

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md)

[Encryption Overview](master_encryption.md)
