AdsEncryptTable




Advantage Database Server 12  

TAdsTable.AdsEncryptTable

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.AdsEncryptTable  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.AdsEncryptTable Advantage TDataSet Descendant ade\_Adsencrypttable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.AdsEncryptTable  Advantage TDataSet Descendant |  |  |  |  |

Encrypts an entire table.

Syntax

procedure AdsEncryptTable ;

Description

AdsEncryptTable encrypts all the records in a table with the current password set via [AdsEnableEncryption](ade_adsenableencryption.htm). All fields in the table, including memo and BLOB fields, are encrypted when this function is used. This function requires exclusive use of the table. If records exist that are already encrypted, they are ignored. An entire table can be decrypted by calling [AdsDecryptTable](ade_adsdecrypttable.htm). Encrypting a table within a transaction is not allowed. Note that with a DBF table, in addition to all records being encrypted, the header of a DBF table is encrypted to prevent non-Advantage applications from opening the table.

Note AdsEncryptTable is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_432789652,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with database tables. Data dictionary administrative access is required to encrypt or decrypt [database tables](javascript:hhpopuplink.TextPopup(popid_2068228995,FontFace,-1,-1,-1,-1)). See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

 

Note Before encrypting a table, it is recommended that you pack the table first via [AdsPackTable](ade_adspacktable.htm) so that previously deleted records are not left unencrypted.

 

Note Any DBF table containing a memo or BLOB field that is encrypted with Advantage 7.0 and greater will no longer be compatible with previous versions of Advantage.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsEnableEncryption( 'secret' );

AdsTable1.AdsEncryptTable;

See Also

[Encryption](master_encryption.htm)

[AdsDecryptTable](ade_adsdecrypttable.htm)

[AdsEnableEncryption](ade_adsenableencryption.htm)