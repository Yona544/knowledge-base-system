TLSCipherSuite




Advantage Database Server 12  

TAdsConnection.EncryptionOptions.TLSCipherSuite

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.EncryptionOptions.TLSCipherSuite  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.EncryptionOptions.TLSCipherSuite Advantage TDataSet Descendant Ade\_TLSCipherSuite Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.EncryptionOptions.TLSCipherSuite  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Choose which cipher suites the client will allow for TLS communications.

Syntax

property EncryptionOtpions.TLSCipherSuite: TAdsTLSCipherSuites;

 

TAdsTLSCipherSuites = set of TAdsTLSCipherSuite;

TAdsTLSCipherSuite = ( tlsAES128SHA, tlsAES256SHA, tlsRC4MD5 );

 

Description

Use this to specify which cipher suites are allowed for Transport Layer Security (TLS) communications. See [TLS\_CIPHERS](master_tls_ciphers.htm) and [Communication Encryption](master_communications_encryption.htm) for more information.

See Also

[EncryptionOptions.TLSCertificate](ade_tlscertificate.htm)

[EncryptionOptions.TLSCommonName](ade_tlscommonname.htm)