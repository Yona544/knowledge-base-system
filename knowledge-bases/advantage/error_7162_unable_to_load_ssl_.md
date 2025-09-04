7162 Unable to Load SSL Entrypoint




Advantage Database Server 12  

7162 Unable to Load SSL Entrypoint

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7162 Unable to Load SSL Entrypoint  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7162 Unable to Load SSL Entrypoint Advantage Error Guide Error\_7162\_unable\_to\_load\_ssl\_ Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7162 Unable to Load SSL Entrypoint  Advantage Error Guide |  |  |  |  |

Problem: Advantage Database Server was not able to load one of the entrypoints from the OpenSSL libraries. This may mean that the wrong version of the library was loaded.

Solution: In order to use [AES encryption](master_encryption.htm) or [TLS communications](master_communications_encryption.htm), you must have the FIPS Encryption Security Option available. If the libraries are available, verify that they are in a path location that the server can access.