AdsDisableEncryption




Advantage Database Server 12  

TAdsTable/TAdsQuery.AdsDisableEncryption

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable/TAdsQuery.AdsDisableEncryption  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable/TAdsQuery.AdsDisableEncryption Advantage TDataSet Descendant ade\_Adsdisableencryption Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable/TAdsQuery.AdsDisableEncryption  Advantage TDataSet Descendant |  |  |  |  |

Turns off Advantage encryption.

Syntax

procedure AdsDisableEncryption;

Description

AdsDisableEncryption turns off Advantage encryption for the specified dataset. This function is useful so that future updates will not cause the record to be written in an encrypted form. AdsDisableEncryption also allows you to write a previously encrypted record in its decrypted form. To do this, first set the password to what was originally used to encrypt the record via [AdsEnableEncryption](ade_adsenableencryption.htm). Then, read the record. Next, clear the password via AdsDisableEncryption. Finally, update some data in the record. When the record is flushed, it will be written in its decrypted form.

Note Be sure to disable encryption before updating the record; otherwise, the record will be written in encrypted form to disk.

Note AdsDisableEncryption is only applicable with [free tables](javascript:hhpopuplink.TextPopup(popid_432789652,FontFace,-1,-1,-1,-1)). The encryption process is done automatically with [database tables](javascript:hhpopuplink.TextPopup(popid_2068228995,FontFace,-1,-1,-1,-1)). Data dictionary administrative access is required to encrypt or decrypt database tables. See [Advantage Data Dictionary](master_advantage_data_dictionary.htm) for more information.

Example

AdsTable1.Exclusive := TRUE;

AdsTable1.Active := TRUE;

AdsTable1.AdsEnableEncryption( 'secret' );

 

{. . . your code here . . .}

 

AdsTable1.AdsDisableEncryption;

See Also

[AdsEnableEncryption](ade_adsenableencryption.htm)