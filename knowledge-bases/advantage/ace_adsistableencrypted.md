AdsIsTableEncrypted




Advantage Database Server 12  

AdsIsTableEncrypted

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsTableEncrypted  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsTableEncrypted Advantage Client Engine ace\_Adsistableencrypted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsTableEncrypted  Advantage Client Engine |  |  |  |  |

Returns the encrypted status of the specified table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsTableEncrypted ( ADSHANDLE hTable,  UNSIGNED16 \*pusIsEncrypted ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table. |
| pusIsEncrypted (O) | Returns True or False. |

Remarks

Returns True if the header of the table indicates that the table is encrypted, otherwise returns False. Note that this function will return False even if all the records in the table are encrypted, but AdsEncryptTable was not previously used to encrypt the entire table.

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsistableencrypted_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.htm)

[AdsEncryptTable](ace_adsencrypttable.htm)

[AdsDecryptTable](ace_adsdecrypttable.htm)

[AdsDisableEncryption](ace_adsdisableencryption.htm)

[sp\_EncryptTable](master_sp_encrypttable.htm)

[sp\_DecryptTable](master_sp_decrypttable.htm)