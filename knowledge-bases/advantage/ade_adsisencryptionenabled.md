AdsIsEncryptionEnabled




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsIsEncryptionEnabled

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsIsEncryptionEnabled  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsIsEncryptionEnabled Advantage TDataSet Descendant ade\_Adsisencryptionenabled Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsIsEncryptionEnabled  Advantage TDataSet Descendant |  |  |  |  |

Determines whether encryption is enabled.

Syntax

function AdsIsEncryptionEnabled : boolean;

Description

This function returns True if encryption is enabled on this dataset. False is returned if encryption has not been enabled. When encryption is enabled, updated records will be written to the table in encrypted format.

Example

{ This example decrypts the first record in the table }

AdsTable1.First;

If AdsTable1.AdsIsEncryptionEnabled Then

AdsTable1.AdsDecryptRecord;

See Also

[AdsEnableEncryption](ade_adsenableencryption.htm)

[AdsDisableEncryption](ade_adsdisableencryption.htm)

[AdsIsRecordEncrypted](ade_adsisrecordencrypted.htm)

[sp\_EncryptTable](master_sp_encrypttable.htm)

[sp\_DecryptTable](master_sp_decrypttable.htm)