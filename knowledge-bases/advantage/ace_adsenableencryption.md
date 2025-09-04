AdsEnableEncryption




Advantage Database Server 12  

AdsEnableEncryption

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsEnableEncryption  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsEnableEncryption Advantage Client Engine ace\_Adsenableencryption Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsEnableEncryption  Advantage Client Engine |  |  |  |  |

Enables Advantage encryption and decryption on a free table

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsEnableEncryption (ADSHANDLE hTable,  UNSIGNED8 \*pucPassword); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table or cursor. |
| pucPassword (I) | Case-sensitive text password. This is expected to be a null terminated string. |

Remarks

This function enables encryption and decryption of individual records in the specified free table. After a successful call to AdsEnableEncryption, any record that is updated will also be encrypted. Also, any record read that was previously encrypted will be viewed in its unencrypted form. If the current record in a table needs to be encrypted, but not updated, use [AdsEncryptRecord](ace_adsencryptrecord.htm). If all records in a table need to be encrypted, use [AdsEncryptTable](ace_adsencrypttable.htm) or [sp\_EncryptTable](master_sp_encrypttable.htm).

Only one password can be used to encrypt records in a table. When encryption is enabled for the first time on a table, the table header is updated with the encryption information. Subsequent requests to enable encryption on the table will only succeed if the correct password is supplied. To remove encryption information from the table header, see [AdsDecryptTable](ace_adsdecrypttable.htm) or [sp\_DecryptTable](master_sp_decrypttable.htm).

If AdsEnableEncryption fails for any reason, any encrypted records will be treated as read-only. If the entire table is encrypted, the entire table will be treated as read-only.

Note AdsEnableEncryption is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with [database tables](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)). ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

 

Note The password is case sensitive, so using "secret" will encrypt data differently than "SECRET".

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsenableencryption_example)

See Also

[AdsEncryptTable](ace_adsencrypttable.htm)

[AdsDisableEncryption](ace_adsdisableencryption.htm)

[AdsDecryptTable](ace_adsdecrypttable.htm)

[AdsIsEncryptionEnabled](ace_adsisencryptionenabled.htm)

[AdsIsRecordEncrypted](ace_adsisrecordencrypted.htm)