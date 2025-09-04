TLSCommonName




Advantage Database Server 12  

TAdsConnection.EncryptionOptions.TLSCommonName

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.EncryptionOptions.TLSCommonName  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.EncryptionOptions.TLSCommonName Advantage TDataSet Descendant Ade\_TLSCommonName Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.EncryptionOptions.TLSCommonName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

The expected common name for the TLS connection.

Syntax

property EncryptionOtpions.TLSCommonName: String;

Description

Specifies the expected "common name" from the server when using Transport Layer Security (TLS) [communications](master_communications_encryption.htm). If this is not given or does not match the common name sent back from the server, the connection is terminated.

See Also

[EncryptionOptions.TLSCertificate](ade_tlscertificate.htm)

[EncryptionOptions.TLSCipherSuite](ade_tlsciphersuite.htm)