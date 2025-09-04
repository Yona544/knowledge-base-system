AdsIsTableEncrypted




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsIsTableEncrypted

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsIsTableEncrypted  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsIsTableEncrypted Advantage TDataSet Descendant ade\_Adsistableencrypted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
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

[AdsDisableEncryption](ade_adsdisableencryption.htm)

[AdsEnableEncryption](ade_adsenableencryption.htm)

[AdsEncryptTable](ade_adsencrypttable.htm)

[AdsDecryptTable](ade_adsdecrypttable.htm)

[sp\_EncryptTable](master_sp_encrypttable.htm)

[sp\_DecryptTable](master_sp_decrypttable.htm)