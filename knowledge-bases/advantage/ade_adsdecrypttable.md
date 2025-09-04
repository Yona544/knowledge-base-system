AdsDecryptTable




Advantage Database Server 12  

TAdsTable.AdsDecryptTable

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsDecryptTable  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsDecryptTable Advantage TDataSet Descendant ade\_Adsdecrypttable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsDecryptTable  Advantage TDataSet Descendant |  |  |  |  |

Decrypts an entire table.

Syntax

procedure AdsDecryptTable;

Description

AdsDecryptTable will traverse the entire table and decrypt all records with the password set via [AdsEnableEncryption](ade_adsenableencryption.htm). Use of this function requires exclusive use of the table. If a record in the table is already unencrypted, it will be skipped.

The encryption information in the table header will be cleared automatically after the decrypt table operation has completed. Encryption will be disabled after the decrypt table operation has completed; that is, subsequent updates to the records will be written in unencrypted format.

Decrypting a table within a transaction is not allowed.

Note AdsDecryptTable is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_432789652,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with [database tables](javascript:hhpopuplink.TextPopup(popid_2068228995,FontFace,-1,-1,-1,-1)). Data dictionary administrative access is required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsEnableEncryption( 'secret' );

AdsTable1.AdsDecryptTable;

See Also

[AdsEnableEncryption](ade_adsenableencryption.htm)

[AdsEncryptTable](ade_adsencrypttable.htm)

[sp\_EncryptTable](master_sp_encrypttable.htm)

[sp\_DecryptTable](master_sp_decrypttable.htm)