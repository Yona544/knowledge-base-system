---
title: Ace Adsdecryptrecord
slug: ace_adsdecryptrecord
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdecryptrecord.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 99f890f533310dbbb6794623f559efd4441e3071
---

# Ace Adsdecryptrecord

AdsDecryptRecord

AdsDecryptRecord

Advantage Client Engine

| AdsDecryptRecord  Advantage Client Engine |  |  |  |  |

Decrypts the current record after encryption has been enabled.

Syntax

| UNSIGNED32 | AdsDecryptRecord( ADSHANDLE hTable ); |

Parameters

| hTable (I) | Handle of a table. |

Remarks

AdsDecryptRecord decrypts the current record in a table with the current password set via AdsEnableEncryption. If the record is not encrypted, it is ignored.

Note AdsDecryptRecord only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.md) for more details.

Note AdsDecryptRecord is only applicable with free tables). The encryption process is done automatically with database tables). ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

Example

[Click Here](ace_aof_and_encryption_examples.md#adsdecryptrecord_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.md)

[AdsIsRecordEncrypted](ace_adsisrecordencrypted.md)

[AdsIsEncryptionEnabled](ace_adsisencryptionenabled.md)

[AdsEncryptRecord](ace_adsencryptrecord.md)
