AdsDecryptTable




Advantage Database Server 12  

AdsDecryptTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDecryptTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDecryptTable Advantage Client Engine ace\_Adsdecrypttable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDecryptTable  Advantage Client Engine |  |  |  |  |

Decrypts an entire table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsDecryptTable (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table. |

Remarks

AdsDecryptTable will traverse the entire table and decrypt all records with the password set via [AdsEnableEncryption](ace_adsenableencryption.htm). Use of this function requires exclusive use of the table. If a record in the table is already unencrypted, it will be skipped.

The encryption information in the table header will be cleared automatically after the decrypt table operation has completed. Encryption will be disabled after the decrypt table operation has completed; that is, subsequent updates to the records will be written in unencrypted format.

Decrypting a table within a transaction is not allowed.

Note AdsDecryptTable only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.htm) for more detail.

Note AdsDecryptTable is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with [database tables](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)). ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsdecrypttable_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.htm)

[AdsEncryptTable](ace_adsencrypttable.htm)

[sp\_EncryptTable](master_sp_encrypttable.htm)

[sp\_DecryptTable](master_sp_decrypttable.htm)