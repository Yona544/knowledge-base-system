---
title: Ace Adsisencryptionenabled
slug: ace_adsisencryptionenabled
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsisencryptionenabled.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 3fb7ec4e2e5be4adbeb7142ae395f50907c4b810
---

# Ace Adsisencryptionenabled

AdsIsEncryptionEnabled

AdsIsEncryptionEnabled

Advantage Client Engine

| AdsIsEncryptionEnabled  Advantage Client Engine |  |  |  |  |

Returns the current encryption status for the specified table.

Syntax

| UNSIGNED32 | AdsIsEncryptionEnabled( ADSHANDLE hTable,  UNSIGNED16 \*pusIsEnabled ); |

Parameters

| hTable (I) | Handle of a table. |
| pusIsEnabled (O) | Returns True or False |

Remarks

This function returns True if encryption is enabled on the specified table via AdsEnableEncryption. False is returned if encryption has not been enabled. When encryption is enabled, updated records will be written to the table in encrypted format.

Example

[Click Here](ace_aof_and_encryption_examples.md#adsisencryptionenabled_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.md)

[AdsDisableEncryption](ace_adsdisableencryption.md)

[AdsIsRecordEncrypted](ace_adsisrecordencrypted.md)

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_DecryptTable](master_sp_decrypttable.md)
