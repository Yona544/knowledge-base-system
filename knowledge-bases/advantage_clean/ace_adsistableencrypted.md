---
title: Ace Adsistableencrypted
slug: ace_adsistableencrypted
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsistableencrypted.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 6912df0e5731d9f6837e80f710283c0abd0e12ac
---

# Ace Adsistableencrypted

AdsIsTableEncrypted

AdsIsTableEncrypted

Advantage Client Engine

| AdsIsTableEncrypted  Advantage Client Engine |  |  |  |  |

Returns the encrypted status of the specified table

Syntax

| UNSIGNED32 | AdsIsTableEncrypted ( ADSHANDLE hTable,  UNSIGNED16 \*pusIsEncrypted ); |

Parameters

| hTable (I) | Handle of a table. |
| pusIsEncrypted (O) | Returns True or False. |

Remarks

Returns True if the header of the table indicates that the table is encrypted, otherwise returns False. Note that this function will return False even if all the records in the table are encrypted, but AdsEncryptTable was not previously used to encrypt the entire table.

Example

[Click Here](ace_aof_and_encryption_examples.md#adsistableencrypted_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.md)

[AdsEncryptTable](ace_adsencrypttable.md)

[AdsDecryptTable](ace_adsdecrypttable.md)

[AdsDisableEncryption](ace_adsdisableencryption.md)

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_DecryptTable](master_sp_decrypttable.md)
