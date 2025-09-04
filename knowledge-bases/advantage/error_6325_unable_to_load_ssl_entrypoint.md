6325 Unable to Load SSL Entrypoint




Advantage Database Server 12  

6325 Unable to Load SSL Entrypoint

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6325 Unable to Load SSL Entrypoint  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6325 Unable to Load SSL Entrypoint Advantage Error Guide error\_6325\_UNABLE\_TO\_LOAD\_SSL\_entrypoint Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6325 Unable to Load SSL Entrypoint  Advantage Error Guide |  |  |  |  |

The client communications layer was not able to load one of the entrypoints from the OpenSSL libraries. This may mean that the wrong version of the library was loaded. In order to use [AES encryption](master_encryption.htm) or [TLS communications](master_communications_encryption.htm), you must have the FIPS Encryption Security Option available. If the libraries are available, verify that they are in a path location that the application can access.