AdsExtendedReader.DecryptTable




Advantage Database Server 12  

AdsExtendedReader.DecryptTable

Advantage .NET Data Provider

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsExtendedReader.DecryptTable  Advantage .NET Data Provider |  |  | Feedback on: Advantage Database Server 12 - AdsExtendedReader.DecryptTable Advantage .NET Data Provider dotnet\_Adsextendedreader\_decrypttable Advantage .NET Data Provider > AdsExtendedReader Class > AdsExtendedReader Methods > AdsExtendedReader.DecryptTable / Dear Support Staff, |  |
| AdsExtendedReader.DecryptTable  Advantage .NET Data Provider |  |  |  |  |

Decrypts an entire table

public void DecryptTable( string strPassword );

Remarks

DecryptTable will traverse the entire table and decrypt all records using the given password. Use of this function requires exclusive use of the table, specified in the ConnectionString (Shared=FALSE). If a record in the table is already unencrypted, it will be skipped. The encryption information in the table header will be cleared automatically after the decrypt table operation has completed. Encryption will be disabled after the decrypt table operation has completed; that is, subsequent updates to the records will be written in unencrypted format.

Decrypting a table within a transaction is not allowed.

Note DecryptTable only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error.

 

Note DecryptTable is only applicable with free tables. The encryption process is done automatically with database tables. Data dictionary administrative access is required to encrypt or decrypt database tables. See Advantage Data Dictionary for more information.

See Also

[EncryptTable](dotnet_adsextendedreader_encrypttable.htm)

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.htm)

[sp\_EncryptTable](master_sp_encrypttable.htm)

[sp\_DecryptTable](master_sp_decrypttable.htm)