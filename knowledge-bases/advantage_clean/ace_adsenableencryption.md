---
title: Ace Adsenableencryption
slug: ace_adsenableencryption
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsenableencryption.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: cdf950db56595610248508e3f87ab74a26fd1915
---

# Ace Adsenableencryption

AdsEnableEncryption

AdsEnableEncryption

Advantage Client Engine

| AdsEnableEncryption  Advantage Client Engine |  |  |  |  |

Enables Advantage encryption and decryption on a free table

Syntax

| UNSIGNED32 | AdsEnableEncryption (ADSHANDLE hTable,  UNSIGNED8 \*pucPassword); |

Parameters

| hTable (I) | Handle of a table or cursor. |
| pucPassword (I) | Case-sensitive text password. This is expected to be a null terminated string. |

Remarks

This function enables encryption and decryption of individual records in the specified free table. After a successful call to AdsEnableEncryption, any record that is updated will also be encrypted. Also, any record read that was previously encrypted will be viewed in its unencrypted form. If the current record in a table needs to be encrypted, but not updated, use [AdsEncryptRecord](ace_adsencryptrecord.md). If all records in a table need to be encrypted, use [AdsEncryptTable](ace_adsencrypttable.md) or [sp\_EncryptTable](master_sp_encrypttable.md).

Only one password can be used to encrypt records in a table. When encryption is enabled for the first time on a table, the table header is updated with the encryption information. Subsequent requests to enable encryption on the table will only succeed if the correct password is supplied. To remove encryption information from the table header, see [AdsDecryptTable](ace_adsdecrypttable.md) or [sp\_DecryptTable](master_sp_decrypttable.md).

If AdsEnableEncryption fails for any reason, any encrypted records will be treated as read-only. If the entire table is encrypted, the entire table will be treated as read-only.

Note AdsEnableEncryption is only applicable with free tables). The encryption process is done automatically with database tables). ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

 

Note The password is case sensitive, so using "secret" will encrypt data differently than "SECRET".

Example

[Click Here](ace_aof_and_encryption_examples.md#adsenableencryption_example)

See Also

[AdsEncryptTable](ace_adsencrypttable.md)

[AdsDisableEncryption](ace_adsdisableencryption.md)

[AdsDecryptTable](ace_adsdecrypttable.md)

[AdsIsEncryptionEnabled](ace_adsisencryptionenabled.md)

[AdsIsRecordEncrypted](ace_adsisrecordencrypted.md)
