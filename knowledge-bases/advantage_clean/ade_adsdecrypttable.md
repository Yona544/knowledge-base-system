---
title: Ade Adsdecrypttable
slug: ade_adsdecrypttable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsdecrypttable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 483f03ecd614895da03b904c67f775ca7a8c96b3
---

# Ade Adsdecrypttable

AdsDecryptTable

TAdsTable.AdsDecryptTable

Advantage TDataSet Descendant

| TAdsTable.AdsDecryptTable  Advantage TDataSet Descendant |  |  |  |  |

Decrypts an entire table.

Syntax

procedure AdsDecryptTable;

Description

AdsDecryptTable will traverse the entire table and decrypt all records with the password set via [AdsEnableEncryption](ade_adsenableencryption.md). Use of this function requires exclusive use of the table. If a record in the table is already unencrypted, it will be skipped.

The encryption information in the table header will be cleared automatically after the decrypt table operation has completed. Encryption will be disabled after the decrypt table operation has completed; that is, subsequent updates to the records will be written in unencrypted format.

Decrypting a table within a transaction is not allowed.

Note AdsDecryptTable is only applicable with free tables). The encryption process is done automatically with database tables). Data dictionary administrative access is required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsEnableEncryption( 'secret' );

AdsTable1.AdsDecryptTable;

See Also

[AdsEnableEncryption](ade_adsenableencryption.md)

[AdsEncryptTable](ade_adsencrypttable.md)

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_DecryptTable](master_sp_decrypttable.md)
