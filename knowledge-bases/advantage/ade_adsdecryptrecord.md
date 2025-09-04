AdsDecryptRecord




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsDecryptRecord

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsDecryptRecord  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsDecryptRecord Advantage TDataSet Descendant ade\_Adsdecryptrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsDecryptRecord  Advantage TDataSet Descendant |  |  |  |  |

Decrypts the current record after encryption has been enabled.

Syntax

procedure AdsDecryptRecord;

Description

AdsDecryptRecord decrypts the current record in this table with the current password set via [AdsEnableEncryption](ade_adsenableencryption.htm) . If the record is not encrypted, it is ignored.

Note AdsDecryptRecord is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_432789652,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with [database tables](javascript:hhpopuplink.TextPopup(popid_2068228995,FontFace,-1,-1,-1,-1)). Data dictionary administrative access is required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

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

[AdsEncryptRecord](ade_adsencryptrecord.htm)