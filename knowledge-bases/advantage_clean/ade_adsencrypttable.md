---
title: Ade Adsencrypttable
slug: ade_adsencrypttable
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsencrypttable.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 284fca67cdc4aca8b814a805fd9e3b635a38ae07
---

# Ade Adsencrypttable

AdsEncryptTable

TAdsTable.AdsEncryptTable

Advantage TDataSet Descendant

| TAdsTable.AdsEncryptTable  Advantage TDataSet Descendant |  |  |  |  |

Encrypts an entire table.

Syntax

procedure AdsEncryptTable ;

Description

AdsEncryptTable encrypts all the records in a table with the current password set via [AdsEnableEncryption](ade_adsenableencryption.md). All fields in the table, including memo and BLOB fields, are encrypted when this function is used. This function requires exclusive use of the table. If records exist that are already encrypted, they are ignored. An entire table can be decrypted by calling [AdsDecryptTable](ade_adsdecrypttable.md). Encrypting a table within a transaction is not allowed. Note that with a DBF table, in addition to all records being encrypted, the header of a DBF table is encrypted to prevent non-Advantage applications from opening the table.

Note AdsEncryptTable is only applicable with free tables). The encryption process is done automatically with database tables. Data dictionary administrative access is required to encrypt or decrypt database tables). See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

 

Note Before encrypting a table, it is recommended that you pack the table first via [AdsPackTable](ade_adspacktable.md) so that previously deleted records are not left unencrypted.

 

Note Any DBF table containing a memo or BLOB field that is encrypted with Advantage 7.0 and greater will no longer be compatible with previous versions of Advantage.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsEnableEncryption( 'secret' );

AdsTable1.AdsEncryptTable;

See Also

[Encryption](master_encryption.md)

[AdsDecryptTable](ade_adsdecrypttable.md)

[AdsEnableEncryption](ade_adsenableencryption.md)
