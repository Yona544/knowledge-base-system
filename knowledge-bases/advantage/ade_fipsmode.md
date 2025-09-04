FIPSMode




Advantage Database Server 12  

TAdsConnection.EncryptionOptions.FIPSMode

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsConnection.EncryptionOptions.FIPSMode  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsConnection.EncryptionOptions.FIPSMode Advantage TDataSet Descendant Ade\_FIPSMode Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsConnection.EncryptionOptions.FIPSMode  Advantage TDataSet Descendant |  |  |  |  |

[TAdsConnection](ade_tadsconnection_7.htm)

Specifies whether the client should be in [FIPS mode](master_fips.htm).

Syntax

property EncryptionOptions.FIPSMode: Boolean;

Description

Specifies whether or not the client should run in [FIPS mode](master_fips.htm). This setting must be the same as the server to which the connection is made. All connections must use the same value in an application. It is not allowed to mix FIPS mode connections and non-FIPS mode connections.