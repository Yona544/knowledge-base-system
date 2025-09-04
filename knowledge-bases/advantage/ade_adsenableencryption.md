AdsEnableEncryption




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsEnableEncryption

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsEnableEncryption  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsEnableEncryption Advantage TDataSet Descendant ade\_Adsenableencryption Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsEnableEncryption  Advantage TDataSet Descendant |  |  |  |  |

Enables record-based Advantage encryption and decryption

Syntax

procedure AdsEnableEncryption ( strPassword : String );

Parameter

|  |  |
| --- | --- |
| strPassword | Case-sensitive text password. |

Description

This function enables encryption and decryption of individual records in the specified dataset. After a successful call to AdsEnableEncryption, any record that is updated will also be encrypted. Also, any record read that was previously encrypted will be viewed in its unencrypted form. If the current record in a table needs to be encrypted, but not updated, use [AdsEncryptRecord](ade_adsencryptrecord.htm). If all records in a table need to be encrypted, use [AdsEncryptTable](ade_adsencrypttable.htm) or [sp\_EncryptTable](master_sp_encrypttable.htm).

Only one password can be used to encrypt records in a dataset. When encryption is enabled for the first time on a dataset, the table header is updated with the encryption information. Subsequent requests to enable encryption on the dataset will only succeed if the correct password is supplied. To remove encryption from a table header, see [AdsDecryptTable](ade_adsdecrypttable.htm) or [sp\_DecryptTable](master_sp_decrypttable.htm).

If AdsEnableEncryption fails for any reason, any encrypted records will be treated as read-only. If the entire dataset is encrypted, the entire dataset will be treated as read-only.

Note The password is case-sensitive. Using "secret" will encrypt data differently than "SECRET".

 

Note AdsEnableEncryption is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_432789652,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with database tables. Data dictionary administrative access is required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

Example

AdsTable1.Active := TRUE;

AdsTable1.AdsEnableEncryption( 'secret' );

See Also

[AdsDisableEncryption](ade_adsdisableencryption.htm)

[AdsEncryptTable](ade_adsencrypttable.htm)

[AdsDecryptTable](ade_adsdecrypttable.htm)

[AdsIsEncryptionEnabled](ade_adsisencryptionenabled.htm)

[AdsIsRecordEncrypted](ade_adsisrecordencrypted.htm)