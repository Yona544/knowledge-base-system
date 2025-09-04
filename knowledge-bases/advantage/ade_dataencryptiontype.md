DataEncryptionType




Advantage Database Server 12  

TAdsConnection.EncryptionOptions.DataEncryptionType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.EncryptionOptions.DataEncryptionType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.EncryptionOptions.DataEncryptionType Advantage TDataSet Descendant Ade\_DataEncryptionType Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.EncryptionOptions.DataEncryptionType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies the encryption type to use on this connection.

Syntax

property EncryptionOptions.DataEncryptionType: TAdsDataEncryptionType;

 

TAdsDataEncryptionType = ( etAdsDefault, etAdsAES128, etAdsAES256, etAdsRC4 );

Description

Specifies the encryption type to use when [encrypting tables](master_encryption.htm).  A newly encrypted table will be encrypted with this encryption type.  A newly created data dictionary on this connection will use the specified encryption type. When opening an existing table or data dictionary that is encrypted, this connection option is ignored and the appropriate encryption type is used. To change the encryption type associated with an existing dictionary refer to [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm). It is important to note that any table created when an AES encryption type is used (even if the table is not encrypted) will not be compatible with versions of Advantage prior to v10.1.