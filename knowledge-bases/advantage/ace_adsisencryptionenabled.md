AdsIsEncryptionEnabled




Advantage Database Server 12  

AdsIsEncryptionEnabled

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsEncryptionEnabled  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsEncryptionEnabled Advantage Client Engine ace\_Adsisencryptionenabled Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsEncryptionEnabled  Advantage Client Engine |  |  |  |  |

Returns the current encryption status for the specified table.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsEncryptionEnabled( ADSHANDLE hTable,  UNSIGNED16 \*pusIsEnabled ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table. |
| pusIsEnabled (O) | Returns True or False |

Remarks

This function returns True if encryption is enabled on the specified table via AdsEnableEncryption. False is returned if encryption has not been enabled. When encryption is enabled, updated records will be written to the table in encrypted format.

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsisencryptionenabled_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.htm)

[AdsDisableEncryption](ace_adsdisableencryption.htm)

[AdsIsRecordEncrypted](ace_adsisrecordencrypted.htm)

[sp\_EncryptTable](master_sp_encrypttable.htm)

[sp\_DecryptTable](master_sp_decrypttable.htm)