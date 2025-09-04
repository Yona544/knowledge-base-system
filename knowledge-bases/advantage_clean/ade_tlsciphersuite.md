---
title: Ade Tlsciphersuite
slug: ade_tlsciphersuite
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tlsciphersuite.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 859edf31673c15617baca826efa00d655039c7da
---

# Ade Tlsciphersuite

TLSCipherSuite

TAdsConnection.EncryptionOptions.TLSCipherSuite

Advantage TDataSet Descendant

| TAdsConnection.EncryptionOptions.TLSCipherSuite  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Choose which cipher suites the client will allow for TLS communications.

Syntax

property EncryptionOtpions.TLSCipherSuite: TAdsTLSCipherSuites;

 

TAdsTLSCipherSuites = set of TAdsTLSCipherSuite;

TAdsTLSCipherSuite = ( tlsAES128SHA, tlsAES256SHA, tlsRC4MD5 );

 

Description

Use this to specify which cipher suites are allowed for Transport Layer Security (TLS) communications. See [TLS\_CIPHERS](master_tls_ciphers.md) and [Communication Encryption](master_communications_encryption.md) for more information.

See Also

[EncryptionOptions.TLSCertificate](ade_tlscertificate.md)

[EncryptionOptions.TLSCommonName](ade_tlscommonname.md)
