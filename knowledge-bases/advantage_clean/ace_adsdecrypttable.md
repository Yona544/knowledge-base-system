---
title: Ace Adsdecrypttable
slug: ace_adsdecrypttable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdecrypttable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 7582775f60c4bceee814b652737059fa0435958e
---

# Ace Adsdecrypttable

AdsDecryptTable

AdsDecryptTable

Advantage Client Engine

| AdsDecryptTable  Advantage Client Engine |  |  |  |  |

Decrypts an entire table

Syntax

| UNSIGNED32 | AdsDecryptTable (ADSHANDLE hTable); |

Parameters

| hTable (I) | Handle of a table. |

Remarks

AdsDecryptTable will traverse the entire table and decrypt all records with the password set via [AdsEnableEncryption](ace_adsenableencryption.md). Use of this function requires exclusive use of the table. If a record in the table is already unencrypted, it will be skipped.

The encryption information in the table header will be cleared automatically after the decrypt table operation has completed. Encryption will be disabled after the decrypt table operation has completed; that is, subsequent updates to the records will be written in unencrypted format.

Decrypting a table within a transaction is not allowed.

Note AdsDecryptTable only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.md) for more detail.

Note AdsDecryptTable is only applicable with free tables). The encryption process is done automatically with database tables). ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

Example

[Click Here](ace_aof_and_encryption_examples.md#adsdecrypttable_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.md)

[AdsEncryptTable](ace_adsencrypttable.md)

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_DecryptTable](master_sp_decrypttable.md)
