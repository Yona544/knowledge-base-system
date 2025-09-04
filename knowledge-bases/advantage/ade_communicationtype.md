CommunicationType




Advantage Database Server 12  

TAdsConnection.CommunicationType

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.CommunicationType  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.CommunicationType Advantage TDataSet Descendant ade\_Communicationtype Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.CommunicationType  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies the communication setting for this connection.

Syntax

TAdsCommunicationType = ( ctAdsDefault, ctAdsUDPIP, ctAdsIPX, ctAdsTCPIP );

property CommunicationType: TAdsCommunicationType;

Description

This property is ignored for stADS\_LOCAL connections. The CommunicationType property can be set to one of the following values:

|  |  |
| --- | --- |
| Value | Meaning |
| ctAdsDefault | (Default) This value indicates that the all communication types should be tried and the first to successfully connect to Advantage should be used. |
| ctAdsUDPIP | If this option is specified, then all communications with the Advantage Database Server uses the UDP/IP protocol. |
| ctAdsIPX | If this option is specified, then all communications with the Advantage Database Server uses the IPX protocol. |
| ctAdsTCPIP | If this option is specified, then all communications with the Advantage Database Server uses the TCP/IP protocol. |
| ctAdsTLS | If this option is specified, [Transport Layer Security](master_communications_encryption.htm) will be used. When TLS is used, the EncryptionOptions.TLSCertificate and EncryptionOptions.TLSCommonName properties must also be specified. |