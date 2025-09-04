AdsExtendedReader.EncryptionPassword




Advantage Database Server 12  

AdsExtendedReader.EncryptionPassword

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.EncryptionPassword  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.EncryptionPassword Advantage .NET Data Provider dotnet\_Adsextendedreader\_encryptionpassword Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Properties > AdsExtendedReader.EncryptionPassword / Dear Support Staff, |  |
| AdsExtendedReader.EncryptionPassword  Advantage .NET Data Provider |  |  |  |  |

Enables record-based Advantage encryption and decryption.

public string EncryptionPassword{ set; }

Remarks

This property enables encryption and decryption of individual records in the table. After setting this property, any record that is updated will also be encrypted. Also, any record read that was previously encrypted will be viewed in its unencrypted form

If all records in a table need to be encrypted, use [EncryptTable](dotnet_adsextendedreader_encrypttable.htm).

Only one password can be used to encrypt records in a table. When encryption is set for the first time on the reader, the table header is updated with the encryption information.

To remove encryption information from the table header, see [DecryptTable](dotnet_adsextendedreader_decrypttable.htm).

If EncryptionPassword fails to set for any reason, any encrypted records will be treated as read-only. If the entire table is encrypted, the entire table will be treated as read-only.

Note EncryptionPassword is only applicable with free tables. The encryption process is done automatically with database tables. Data dictionary administrative access is required to encrypt or decrypt database tables. See Advantage Data Dictionary for more information.

 

Note The password is case sensitive, so using "secret" will encrypt data differently than "SECRET".

See Also

[EncryptTable](dotnet_adsextendedreader_encrypttable.htm)

[DecryptTable](dotnet_adsextendedreader_decrypttable.htm)