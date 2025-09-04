7163 SSL Library Error




Advantage Database Server 12  

7163 SSL Library Error

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 7163 SSL Library Error  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 7163 SSL Library Error Advantage Error Guide Error\_7163\_ssl\_library\_error Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 7163 SSL Library Error  Advantage Error Guide |  |  |  |  |

Problem: A general unknown error occurred in the OpenSSL library.

Solution: The error log may contain more detailed information with additional error numbers. Refer to the [OpenSSL error information](error_openssl_errors.htm).

Problem: The server failed to load the TLS certificate ([TLS\_KEY\_FILE](master_tls_key_file.htm)) and logged 7163 errors on startup.

Solution: Verify that the path and name for the certificate file is correct. The full path must be included. If Advantage is running as a service in Windows, for example, the default directory may not be the folder containing the certificate.