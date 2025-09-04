---
title: Ace Adsencryptrecord
slug: ace_adsencryptrecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsencryptrecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 9373f8beef457cc150a52b4ea253cbf9d0c500dc
---

# Ace Adsencryptrecord

AdsEncryptRecord

AdsEncryptRecord

Advantage Client Engine

| AdsEncryptRecord  Advantage Client Engine |  |  |  |  |

Encrypts the current record after encryption has been enabled.

Syntax

| UNSIGNED32 | AdsEncryptRecord( ADSHANDLE hTable ); |

Parameters

| hTable (I) | Handle of a table. |

Remarks

AdsEncryptRecord encrypts the current record in a table with the current password set via [AdsEnableEncryption](ace_adsenableencryption.md). However, any memo or BLOB data associated with the record is not encrypted. To encrypt memo and BLOB data, the entire table must be encrypted via [AdsEncryptTable](ace_adsencrypttable.md). If the record is already encrypted, it is ignored. Note that you only need to call this API if you want the current record to be encrypted, and you are not going to make changes to the record. Normally, when encryption is enabled, any record that you change will automatically be encrypted.

 

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.md) for more details.

 

Note AdsEncryptRecord is only applicable with free tables). The encryption process is done automatically with database tables. ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

Example

[Click Here](ace_aof_and_encryption_examples.md#adsencryptrecord_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.md)

[AdsIsRecordEncrypted](ace_adsisrecordencrypted.md)

[AdsIsEncryptionEnabled](ace_adsisencryptionenabled.md)

[AdsDecryptRecord](ace_adsdecryptrecord.md)
