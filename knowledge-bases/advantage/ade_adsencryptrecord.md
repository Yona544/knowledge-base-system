AdsEncryptRecord




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsEncryptRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsEncryptRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsEncryptRecord Advantage TDataSet Descendant ade\_Adsencryptrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsEncryptRecord  Advantage TDataSet Descendant |  |  |  |  |

Encrypts the current record after encryption has been enabled.

Syntax

procedure AdsEncryptRecord;

Description

AdsEncryptRecord encrypts the current record in the table with the current password set via [AdsEnableEncryption](ade_adsenableencryption.htm). However, any memo or BLOB data associated with the record is not encrypted. To encrypt memo and BLOB data, the entire table must be encrypted via [AdsEncryptTable](ade_adsencrypttable.htm). If the record is already encrypted, it is ignored. Note that you only need to call this API if you want the current record to be encrypted, and you are not going to make changes to the record. Normally, when encryption is enabled, any record that you change will automatically be encrypted.

Note AdsEncryptRecord is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_432789652,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with [database tables](javascript:hhpopuplink.TextPopup(popid_2068228995,FontFace,-1,-1,-1,-1)). Data dictionary administrative access is required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

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

[AdsEnableEncryption](ade_adsenableencryption.htm)

[AdsIsRecordEncrypted](ade_adsisrecordencrypted.htm)

[AdsIsEncryptionEnabled](ade_adsisencryptionenabled.htm)

[AdsDecryptRecord](ade_adsdecryptrecord.htm)