---
title: Ade Adsistableencrypted
slug: ade_adsistableencrypted
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsistableencrypted.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 6c044f450764efa029bc30cff1f6e4ffb75fccbc
---

# Ade Adsistableencrypted

AdsIsTableEncrypted

TAdsTable/TAdsQuery.AdsIsTableEncrypted

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsIsTableEncrypted  Advantage TDataSet Descendant |  |  |  |  |

Returns the encrypted status of the specified dataset.

Syntax

function AdsIsTableEncrypted : boolean;

Description

Returns True if the header of the table indicates that the dataset is encrypted; otherwise, returns False. Note that this function will return False even if all the records in the dataset are encrypted, but AdsEncryptTable was not previously used to "encrypt" the table header.

Example

AdsTable1.Active := TRUE;

if ( AdsTable1.AdsIsTableEncrypted ) then

AdsTable1.AdsEnableEncryption( 'secret' );

 

See Also

[AdsDisableEncryption](ade_adsdisableencryption.md)

[AdsEnableEncryption](ade_adsenableencryption.md)

[AdsEncryptTable](ade_adsencrypttable.md)

[AdsDecryptTable](ade_adsdecrypttable.md)

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_DecryptTable](master_sp_decrypttable.md)
