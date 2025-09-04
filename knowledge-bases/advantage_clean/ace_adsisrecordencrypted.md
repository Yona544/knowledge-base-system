---
title: Ace Adsisrecordencrypted
slug: ace_adsisrecordencrypted
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisrecordencrypted.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5e4c34580b2c3577b844971dd9c713604a84be30
---

# Ace Adsisrecordencrypted

AdsIsRecordEncrypted

AdsIsRecordEncrypted

Advantage Client Engine

| AdsIsRecordEncrypted  Advantage Client Engine |  |  |  |  |

Returns the encrypted status of the current record

Syntax

| UNSIGNED32 | AdsIsRecordEncrypted (ADSHANDLE hTable,  UNSIGNED16 \*pusIsEncrypted); |

Parameters

| hTable (I) | Handle of a table or cursor |
| pusIsEncrypted (O) | Returns True or False |

Remarks

AdsIsRecordEncrypted will return True if the current record is encrypted. It will return False if the record is not encrypted.

For tables [encrypted with AES](master_encryption.md), this function will always return False. The server handles all encryption and decryption and returns unencrypted records to the client.

Example

[Click Here](ace_aof_and_encryption_examples.md#adsisrecordencrypted_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.md)

[AdsDisableEncryption](ace_adsdisableencryption.md)

[AdsEncryptRecord](ace_adsencryptrecord.md)

[AdsDecryptRecord](ace_adsdecryptrecord.md)
