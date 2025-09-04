AdsDecryptRecord




Advantage Database Server 12  

AdsDecryptRecord

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDecryptRecord  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDecryptRecord Advantage Client Engine ace\_Adsdecryptrecord Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDecryptRecord  Advantage Client Engine |  |  |  |  |

Decrypts the current record after encryption has been enabled.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsDecryptRecord( ADSHANDLE hTable ); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table. |

Remarks

AdsDecryptRecord decrypts the current record in a table with the current password set via AdsEnableEncryption. If the record is not encrypted, it is ignored.

Note AdsDecryptRecord only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.htm) for more details.

Note AdsDecryptRecord is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with [database tables](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)). ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsdecryptrecord_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.htm)

[AdsIsRecordEncrypted](ace_adsisrecordencrypted.htm)

[AdsIsEncryptionEnabled](ace_adsisencryptionenabled.htm)

[AdsEncryptRecord](ace_adsencryptrecord.htm)