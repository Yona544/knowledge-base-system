---
title: Ade Tlscommonname
slug: ade_tlscommonname
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_tlscommonname.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 69084c641ae5e47c08a56be2d1db7d20cbbe3ec5
---

# Ade Tlscommonname

TLSCommonName

TAdsConnection.EncryptionOptions.TLSCommonName

Advantage TDataSet Descendant

| TAdsConnection.EncryptionOptions.TLSCommonName  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

The expected common name for the TLS connection.

Syntax

property EncryptionOtpions.TLSCommonName: String;

Description

Specifies the expected "common name" from the server when using Transport Layer Security (TLS) [communications](master_communications_encryption.md). If this is not given or does not match the common name sent back from the server, the connection is terminated.

See Also

[EncryptionOptions.TLSCertificate](ade_tlscertificate.md)

[EncryptionOptions.TLSCipherSuite](ade_tlsciphersuite.md)
