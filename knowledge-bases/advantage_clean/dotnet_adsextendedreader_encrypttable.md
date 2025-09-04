---
title: Dotnet Adsextendedreader Encrypttable
slug: dotnet_adsextendedreader_encrypttable
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsextendedreader_encrypttable.htm
source: Advantage CHM
tags:
  - dotnet
checksum: af64981d215248b0e19d88ffde2149e86d5b3b79
---

# Dotnet Adsextendedreader Encrypttable

AdsExtendedReader.EncryptTable

AdsExtendedReader.EncryptTable

Advantage .NET Data Provider

| AdsExtendedReader.EncryptTable  Advantage .NET Data Provider |  |  |  |  |

Encrypts an entire table

public void EncryptTable( string strPassword );

Remarks

EncryptTable encrypts all the records in a table with the given. All fields in the table, including memo and BLOB fields, are encrypted when this function is used. This function requires exclusive use of the table, specified in the ConnectionString (Shared=FALSE). If records exist that are already encrypted, they are ignored. An entire table can be decrypted by calling DecryptTable. Encrypting a table within a transaction is not allowed. Note that with a DBF table, in addition to all records being encrypted, the header of a DBF table is encrypted to prevent non-Advantage applications from opening the table.

 

Note EncryptTable only accepts table handles. The use of a cursor handle with this API is illegal and will result in an error.

 

Note EncryptTable is only applicable with free tables. The encryption process is done automatically with database tables. Data dictionary administrative access is required to encrypt or decrypt database tables. See Advantage Data Dictionary for more information.

 

Note Before encrypting a table, it is recommended that you pack the table first via PackTable so that previously deleted records are not left unencrypted.

 

Note Any DBF table containing a memo or BLOB field that is encrypted with Advantage 7.0 or greater will no longer be compatible with previous versions of Advantage.

See Also

[Encryption](master_encryption.md)

[DecryptTable](dotnet_adsextendedreader_decrypttable.md)

[PackTable](dotnet_adsextendedreader_packtable.md)

[AdsConnection.ConnectionString](dotnet_adsconnection_connectionstring.md)

[sp\_EncryptTable](master_sp_encrypttable.md)

[sp\_DecryptTable](master_sp_decrypttable.md)
