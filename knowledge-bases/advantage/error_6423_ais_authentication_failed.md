6423 Authentication failed




Advantage Database Server 12  

6423 Authentication failed

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6423 Authentication failed  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6423 Authentication failed Advantage Error Guide error\_6423\_ais\_authentication\_failed Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6423 Authentication failed  Advantage Error Guide |  |  |  |  |

This error indicates that the client was not able to establish a valid connection with the Advantage Database Server.

This error can occur if a pre-v10.1 client attempts to connect to a data dictionary [encrypted with AES](master_encryption.htm). The old client will use the old style encryption during the authentication (handshaking) process and will not be able to authenticate with the server that is using the newer encryption.