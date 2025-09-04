EncryptionPassword




Advantage Database Server 12  

TAdsTable.EncryptionPassword

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsTable.EncryptionPassword  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsTable.EncryptionPassword Advantage TDataSet Descendant ade\_Encryptionpassword\_tadstable Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsTable.EncryptionPassword  Advantage TDataSet Descendant |  |  |  |  |

[TAdsTable](ade_tadstable_7.htm)

Specifies an encryption password to use on encrypted [free tables](javascript:hhpopuplink.TextPopup(popid_432789652,FontFace,-1,-1,-1,-1)).

Syntax

property EncryptionPassword: string;

Description

Use EncryptionPassword to specify the encryption password to use on encrypted [free tables](javascript:hhpopuplink.TextPopup(popid_432789652,FontFace,-1,-1,-1,-1)). The decryption process is done automatically with [database tables](javascript:hhpopuplink.TextPopup(popid_2068228995,FontFace,-1,-1,-1,-1)), and EncryptionPassword is ignored.

Note Storing hard-coded password entries as property values or in code can compromise security.

See Also

[AdsStmtSetTablePassword](ade_adsstmtsettablepassword.htm)

[AdsStmtEnableEncryption](ade_adsstmtenableencryption.htm)