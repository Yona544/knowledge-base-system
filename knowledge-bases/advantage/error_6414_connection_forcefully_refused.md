6414 Connection forcefully refused




Advantage Database Server 12  

6414 Connection forcefully refused

Advantage Error Guide

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| 6414 Connection forcefully refused  Advantage Error Guide |  |  | Feedback on: Advantage Database Server 12 - 6414 Connection forcefully refused Advantage Error Guide error\_6414\_connection\_forcefully\_refused Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| 6414 Connection forcefully refused  Advantage Error Guide |  |  |  |  |

If you are attempting a TCP/IP connection, verify that client is not newer than the server. This error can occur in that situation because the client may send unexpected data to the server, which the server ignores.

If you are attempting a Transport Layer Security (TLS) connection, verify that the server successfully found and loaded the [server certificate](master_communications_encryption.htm). If no certificate was given ([TLS\_KEY\_FILE](master_tls_key_file.htm)) or if it was invalid, the server will not create a socket to receive TLS connections and an attempt by a client to connect to the TLS port will result in a 6414 error. Verify that the TLS\_KEY\_FILE configuration parameter is correct. If the certificate is not valid, the error log (ads\_err.dbf) should contain more information.

If you are attempting a TLS connection, verify that the port number is correct and that you have specified the [CommType](ace_adsconnect101.htm) as TLS. If a TCP/IP connection is specified when connecting to the TLS port, it will result in a 6414 error.