---
title: Master Sp Setddencryptiontype
slug: master_sp_setddencryptiontype
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_setddencryptiontype.htm
source: Advantage CHM
tags:
  - master
checksum: 92a9c51fb9ab19dc0f86fde3f39c2e5cafcfd51a
---

# Master Sp Setddencryptiontype

sp\_SetDDEncryptionType

sp\_SetDDEncryptionType

Advantage SQL Engine

| sp\_SetDDEncryptionType  Advantage SQL Engine |  |  |  |  |

Changes the encryption type on a data dictionary.

Syntax

sp\_SetDDEncryptionType(

 DictionaryName,Character,515,

 AdsSysPW,Character,20,

 DDPassword,Character,20,

 EncryptionType,Character,10,

 Encrypt,Logical )

Parameters

| DictionaryName (I) | Name of data dictionary. This can include path information if the dictionary is in a different folder from the connection path. This process requires exclusive access to the dictionary and, thus, cannot be opened elsewhere. |
| AdsSysPW (I) | The administrator password to the dictionary. |
| DDPassword (I) | Specifies the dictionary password. When using AES encryption, the key data derived from this password is used both for encrypting the data dictionary itself (if it is encrypted) and for encrypting tables in the dictionary. The default RC4 encryption does not use this dictionary password, although if this function is being used to change from AES encryption to RC4 encryption, this parameter still is required to specify the existing password. |
| EncryptionType (I) | Specifies the new encryption type to use. Valid values are AES128, AES256, and RC4. |
| Encrypt (I) | Specifies whether or not the dictionary itself will be encrypted. |

Output

None

Remarks

The sp\_SetDDEncryptionType procedure can be used to convert an existing data dictionary to a new encryption type. For example, in order to use a dictionary in [FIPS mode](master_fips.md), it must be converted to use [AES encryption](master_encryption.md). Even if none of the tables are encrypted, some encryption is used for storing values in the dictionary itself (e.g., password verification data, dictionary link information, etc.).

If the dictionary contains any encrypted tables, they must be decrypted prior to calling this procedure. The procedure itself verifies that all tables are decrypted prior to performing any work and returns an error if that condition is not met.

Important Note After calling this function, all user passwords will be lost. The dictionary does not store passwords. It only stores password verification information, so there is no way to retrieve and update the existing passwords. Therefore, after using this procedure, you must update all user passwords.

Example

-- Change a dictionary's encryption type to AES128 and encrypt the dictionary

EXECUTE PROCEDURE sp\_SetDDEncryptionType( 'mydd.add', 'adssyspass',

              'dictionarypassword', 'AES128', TRUE );

See Also

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_DecryptTable](master_sp_decrypttable.md)

[Encryption Overview](master_encryption.md)
