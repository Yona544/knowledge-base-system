---
title: Master Fips
slug: master_fips
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_fips.htm
source: Advantage CHM
tags:
  - master
checksum: 6c4c14ad6536d964e5e371095bb61e92f4677d70
---

# Master Fips

FIPS

FIPS

Advantage Concepts

| FIPS  Advantage Concepts |  |  |  |  |

The Federal Information Processing Standard (FIPS) 140-2 defines the security requirements for cryptography modules. Beginning with v10.1, Advantage has the option of running in a FIPS compliant mode to allow it to be used in FIPS-compliant applications.

Note that enabling and using FIPS-compliant cryptography in Advantage Database Server does not make an application conform to FIPS 140-2; all parts of the application must be examined and possibly updated for FIPS compliance.

The [communications](master_communications_encryption.md) and [data encryption](master_encryption.md) available in Advantage products prior to v10.1 are not approved for FIPS usage. In v10.1, 128-bit and 256-bit AES can be used for encrypting data. Encrypted communications in FIPS mode are restricted to the AES128-SHA and AES256-SHA ciphers over TLS (Transport Layer Security). Attempts to use any encryption not approved for FIPS usage when running in FIPS mode will result in an error.

In order to be able to use AES encryption, TLS communications necessary for FIPS mode operation, use the FIPS Encryption Security Option Add-on. Please contact your Advantage sales representative or visit [http://scn.sap.com/community/ads](http://www.sybase.com/products/databasemanagement/advantagedatabaseserver/encryption "http://scn.sap.com/community/ads") for additional licensing information.

The following outlines the basic steps to use FIPS mode:

- You must run both client and server in FIPS mode. The server must be started in FIPS mode by setting the FIPS configuration setting to 1 or by providing the command line parameter /FIPS at startup. The client (including local server enabled applications) can be set into FIPS mode by providing "FIPS=TRUE;" in the connection string.

- The data dictionary itself must be converted to use AES encryption. This can be done by using Advantage Data Architect or by calling the system procedure [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md).

- When connecting to a data dictionary that uses AES encryption, you must provide the data dictionary password either via the DDPassword [connection string](ace_adsconnect101.md) option, the [SE\_PASSWORDS](master_se_passwords.md) configuration parameter, or the SEPasswords command line parameter.

- Encrypted tables must be changed to use AES encryption. This can be done by using Advantage Data Architect or by using the system procedures [sp\_DecryptTable](master_sp_decrypttable.md) and [sp\_EncryptTable](master_sp_encrypttable.md).

- If [encrypted communications](master_communications_encryption.md) are necessary, you must use Transport Layer Security (TLS) with AES128-SHA or AES256-SHA.

- You can call the system procedure [sp\_GetSecurityInfo](master_sp_getsecurityinfo.md) to retrieve information about the types of encryption being used.
