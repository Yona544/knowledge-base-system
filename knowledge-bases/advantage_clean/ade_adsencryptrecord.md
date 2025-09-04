---
title: Ade Adsencryptrecord
slug: ade_adsencryptrecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsencryptrecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: b3591950293365b68260349a6519dce2564a8ca3
---

# Ade Adsencryptrecord

AdsEncryptRecord

TAdsTable/TAdsQuery.AdsEncryptRecord

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsEncryptRecord  Advantage TDataSet Descendant |  |  |  |  |

Encrypts the current record after encryption has been enabled.

Syntax

procedure AdsEncryptRecord;

Description

AdsEncryptRecord encrypts the current record in the table with the current password set via [AdsEnableEncryption](ade_adsenableencryption.md). However, any memo or BLOB data associated with the record is not encrypted. To encrypt memo and BLOB data, the entire table must be encrypted via [AdsEncryptTable](ade_adsencrypttable.md). If the record is already encrypted, it is ignored. Note that you only need to call this API if you want the current record to be encrypted, and you are not going to make changes to the record. Normally, when encryption is enabled, any record that you change will automatically be encrypted.

Note AdsEncryptRecord is only applicable with free tables). The encryption process is done automatically with database tables). Data dictionary administrative access is required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

Example

This example encrypts all records in the table and then decrypts all of them.

AdsTable1.Active := TRUE;

AdsTable1.AdsEnableEncryption( 'secret' );

AdsTable1.First;

While AdsTable1.EOF = FALSE Do

Begin

AdsTable1.AdsEncryptRecord;

AdsTable1.Next;

End;

 

AdsTable1.First;

While AdsTable1.EOF = FALSE Do

Begin

AdsTable1.AdsDecryptRecord;

AdsTable1.Next;

End;

See Also

[AdsEnableEncryption](ade_adsenableencryption.md)

[AdsIsRecordEncrypted](ade_adsisrecordencrypted.md)

[AdsIsEncryptionEnabled](ade_adsisencryptionenabled.md)

[AdsDecryptRecord](ade_adsdecryptrecord.md)
