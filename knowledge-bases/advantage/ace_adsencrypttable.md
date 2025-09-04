AdsEncryptTable




Advantage Database Server 12  

AdsEncryptTable

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsEncryptTable  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsEncryptTable Advantage Client Engine ace\_Adsencrypttable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsEncryptTable  Advantage Client Engine |  |  |  |  |

Encrypts an entire table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsEncryptTable (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table. |

Remarks

AdsEncryptTable encrypts all the records in a table with the current password set via [AdsEnableEncryption](ace_adsenableencryption.htm). All fields in the table, including memo and BLOB fields, are encrypted when this function is used. This function requires exclusive use of the table. If records exist that are already encrypted, they are ignored. An entire table can be decrypted by calling [AdsDecryptTable](ace_adsdecrypttable.htm). Encrypting a table within a transaction is not allowed.

Note that with a DBF table, in addition to all records being encrypted, the header of a DBF table is encrypted to prevent non-Advantage applications from opening the table.

Note AdsEncryptTable only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error. See [AdsExecuteSQL](ace_adsexecutesql.htm) for more details.

 

Note AdsEncryptTable is only applicable with free tables. The encryption process is done automatically with database tables. ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

 

Note Before encrypting a table, it is recommended that you pack the table first via [AdsPackTable](ace_adspacktable.htm) so that previously deleted records are not left unencrypted.

 

Note Any DBF table containing a memo or BLOB field that is encrypted with Advantage 7.0 or greater will no longer be compatible with previous versions of Advantage.

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsencrypttable_example)

See Also

[Encryption](master_encryption.htm)

[AdsEnableEncryption](ace_adsenableencryption.htm)

[AdsDecryptTable](ace_adsdecrypttable.htm)