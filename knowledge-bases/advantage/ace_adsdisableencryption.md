AdsDisableEncryption




Advantage Database Server 12  

AdsDisableEncryption

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsDisableEncryption  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsDisableEncryption Advantage Client Engine ace\_Adsdisableencryption Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsDisableEncryption  Advantage Client Engine |  |  |  |  |

Turns off Advantage encryption

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsDisableEncryption (ADSHANDLE hTable); |

Parameters

|  |  |
| --- | --- |
| hTable (I) | Handle of a table or cursor |

Remarks

AdsDisableEncryption turns off Advantage encryption for the specified table. This function is useful so that future updates will not cause the record to be written in an encrypted form. AdsDisableEncryption also allows you to write a previously encrypted record in its decrypted form. To do this, first set the password to what was originally used to encrypt the record via AdsEnableEncryption. Then read the record. Next clear the password via AdsDisableEncryption. Finally, update some data in the record. When the record is flushed, it will be written in its decrypted form.

Note Be sure to disable encryption before updating the record or else the record will be written in encrypted form to disk.

Note AdsDisableEncryption is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_1731427715,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with [database tables](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)). ALTER permissions on the table are required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

Example

[Click Here](ace_aof_and_encryption_examples.htm#adsdisableencryption_example)

See Also

[AdsEnableEncryption](ace_adsenableencryption.htm)