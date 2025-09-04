AdsEncryptRecord




Advantage Database Server 12  

AdsEncryptRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsEncryptRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsEncryptRecord Advantage Client Engine ace\_Adsencryptrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsEncryptRecord  Advantage Client Engine |  |  |  |  |

Encrypts the current record after encryption has been enabled.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsEncryptRecord( ADSHANDLE hTable ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table. |

Remarks

AdsEncryptRecord encrypts the current record in a table with the current password set via [AdsEnableEncryption](ace_adsenableencryption.htm). However, any memo or BLOB data associated with the record is not encrypted. To encrypt memo and BLOB data, the entire table must be encrypted via [AdsEncryptTable](ace_adsencrypttable.htm). If the record is already encrypted, it is ignored. Note that you only need to call this API if you want the current record to be encrypted, and you are not going to make changes to the record. Normally, when encryption is enabled, any record that you change will automatically be encrypted.

 

Note This API only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.htm) for more details.

 

Note AdsEncryptRecord is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with database tables. ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsencryptrecord_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.htm)

[AdsIsRecordEncrypted](ace_adsisrecordencrypted.htm)

[AdsIsEncryptionEnabled](ace_adsisencryptionenabled.htm)

[AdsDecryptRecord](ace_adsdecryptrecord.htm)