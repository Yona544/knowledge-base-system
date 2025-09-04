AdsIsRecordEncrypted




Advantage Database Server 12  

AdsIsRecordEncrypted

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsIsRecordEncrypted  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsIsRecordEncrypted Advantage Client Engine ace\_Adsisrecordencrypted Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsIsRecordEncrypted  Advantage Client Engine |  |  |  |  |

Returns the encrypted status of the current record

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsIsRecordEncrypted (ADSHANDLE hTable,  UNSIGNED16 \*pusIsEncrypted); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table or cursor |
| pusIsEncrypted (O) | Returns True or False |

Remarks

AdsIsRecordEncrypted will return True if the current record is encrypted. It will return False if the record is not encrypted.

For tables [encrypted with AES](master_encryption.htm), this function will always return False. The server handles all encryption and decryption and returns unencrypted records to the client.

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsisrecordencrypted_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.htm)

[AdsDisableEncryption](ace_adsdisableencryption.htm)

[AdsEncryptRecord](ace_adsencryptrecord.htm)

[AdsDecryptRecord](ace_adsdecryptrecord.htm)