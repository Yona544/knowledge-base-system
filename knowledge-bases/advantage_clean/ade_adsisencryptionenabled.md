---
title: Ade Adsisencryptionenabled
slug: ade_adsisencryptionenabled
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsisencryptionenabled.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 452a05fa16c3d564c1a13f2a08009285b6956db1
---

# Ade Adsisencryptionenabled

AdsIsEncryptionEnabled

TAdsTable/TAdsQuery.AdsIsEncryptionEnabled

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsIsEncryptionEnabled  Advantage TDataSet Descendant |  |  |  |  |

Determines whether encryption is enabled.

Syntax

function AdsIsEncryptionEnabled : boolean;

Description

This function returns True if encryption is enabled on this dataset. False is returned if encryption has not been enabled. When encryption is enabled, updated records will be written to the table in encrypted format.

Example

{ This example decrypts the first record in the table }

AdsTable1.First;

If AdsTable1.AdsIsEncryptionEnabled Then

AdsTable1.AdsDecryptRecord;

See Also

[AdsEnableEncryption](ade_adsenableencryption.md)

[AdsDisableEncryption](ade_adsdisableencryption.md)

[AdsIsRecordEncrypted](ade_adsisrecordencrypted.md)

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_DecryptTable](master_sp_decrypttable.md)
