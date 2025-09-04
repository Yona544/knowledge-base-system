---
title: Ade Communicationtype
slug: ade_communicationtype
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_communicationtype.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: a2d5d9f800223abf20ac6166b1999ced041f0a62
---

# Ade Communicationtype

CommunicationType

TAdsConnection.CommunicationType

Advantage TDataSet Descendant

| TAdsConnection.CommunicationType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.md)

Specifies the communication setting for this connection.

Syntax

TAdsCommunicationType = ( ctAdsDefault, ctAdsUDPIP, ctAdsIPX, ctAdsTCPIP );

property CommunicationType: TAdsCommunicationType;

Description

This property is ignored for stADS\_LOCAL connections. The CommunicationType property can be set to one of the following values:

| Value | Meaning |
| ctAdsDefault | (Default) This value indicates that the all communication types should be tried and the first to successfully connect to Advantage should be used. |
| ctAdsUDPIP | If this option is specified, then all communications with the Advantage Database Server uses the UDP/IP protocol. |
| ctAdsIPX | If this option is specified, then all communications with the Advantage Database Server uses the IPX protocol. |
| ctAdsTCPIP | If this option is specified, then all communications with the Advantage Database Server uses the TCP/IP protocol. |
| ctAdsTLS | If this option is specified, [Transport Layer Security](master_communications_encryption.md) will be used. When TLS is used, the EncryptionOptions.TLSCertificate and EncryptionOptions.TLSCommonName properties must also be specified. |
