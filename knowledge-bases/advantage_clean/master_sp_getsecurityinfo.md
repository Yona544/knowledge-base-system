---
title: Master Sp Getsecurityinfo
slug: master_sp_getsecurityinfo
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_getsecurityinfo.htm
source: Advantage CHM
tags:
  - master
checksum: 950b10824d0f7654d8575412973b2f42a1bc8118
---

# Master Sp Getsecurityinfo

sp\_GetSecurityInfo

sp\_GetSecurityInfo

Advantage SQL Engine

| sp\_GetSecurityInfo  Advantage SQL Engine |  |  |  |  |

Retrieves security-related information.

Syntax

sp\_GetSecurityInfo()

Parameters

None.

Output

The sp\_GetSecurityInfo procedure returns a result set containing a single row with the following information:

| Field Name | Field Type | Field Size | Description |
| FIPSMode | Logical | 1 | Returns TRUE if Advantage Database Server (and, by extension, the client) is in FIPS mode. |
| EncryptionType | Character | 10 | Returns the current encryption type for the connection. Values are AES128, AES256, or RC4. |
| DictionaryEncrypted | Logical | 1 | Returns TRUE if the connection is a data dictionary connection and the dictionary is encrypted. |
| CommType | Character | 10 | Returns the communication type. For local server connections, the value will be LOCAL. Otherwise it is one of: SMC (shared memory communications), TLS (Transport Layer Security communications), TCP\_IP (TCP/IP communications), UDP\_IP (UDP communications on IP). |
| TLSCipher | Character | 20 | If the communications is over TLS, this returns the cipher. The value will be one of: AES128-SHA, AES256-SHA, or RC4-MD5. |
| TLSVersion | Character | 20 | If the communications is over TLS, this returns the version information. |

See Also

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md)

[Encryption Overview](master_encryption.md)

[Communications Encryption](master_communications_encryption.md)

[FIPS](master_fips.md)
