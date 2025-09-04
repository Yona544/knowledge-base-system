---
title: Ade Adsdecryptrecord
slug: ade_adsdecryptrecord
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsdecryptrecord.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 888c8bba1b81b5f53602721b266a6b2c05ff8c3d
---

# Ade Adsdecryptrecord

AdsDecryptRecord

TAdsTable/TAdsQuery.AdsDecryptRecord

Advantage TDataSet Descendant

| TAdsTable/TAdsQuery.AdsDecryptRecord  Advantage TDataSet Descendant |  |  |  |  |

Decrypts the current record after encryption has been enabled.

Syntax

procedure AdsDecryptRecord;

Description

AdsDecryptRecord decrypts the current record in this table with the current password set via [AdsEnableEncryption](ade_adsenableencryption.md) . If the record is not encrypted, it is ignored.

Note AdsDecryptRecord is only applicable with free tables). The encryption process is done automatically with database tables). Data dictionary administrative access is required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.md) for more information.

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

[AdsEncryptRecord](ade_adsencryptrecord.md)
