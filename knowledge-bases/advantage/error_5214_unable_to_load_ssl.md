5214 Unable to Load SSL




Advantage Database Server 12  

5214 Unable to Load SSL

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 5214 Unable to Load SSL  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 5214 Unable to Load SSL Advantage Error Guide Error\_5214\_unable\_to\_load\_ssl Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 5214 Unable to Load SSL  Advantage Error Guide |  |  |  |  |

Problem:  The Advantage client was not able to load the OpenSSL libraries. In order to use [AES encryption](master_encryption.htm) or [TLS communications](master_communications_encryption.htm), you must have the FIPS Encryption Security Option available.

Solution: If the libraries are available, verify that they are in a path location that the client application can access.