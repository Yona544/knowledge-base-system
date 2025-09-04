---
title: Error 6414 Connection Forcefully Refused
slug: error_6414_connection_forcefully_refused
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_6414_connection_forcefully_refused.htm
source: Advantage CHM
tags:
  - error
checksum: cb06712298f9c07b76f249596e149139da7e7105
---

# Error 6414 Connection Forcefully Refused

6414 Connection forcefully refused

6414 Connection forcefully refused

Advantage Error Guide

| 6414 Connection forcefully refused  Advantage Error Guide |  |  |  |  |

If you are attempting a TCP/IP connection, verify that client is not newer than the server. This error can occur in that situation because the client may send unexpected data to the server, which the server ignores.

If you are attempting a Transport Layer Security (TLS) connection, verify that the server successfully found and loaded the [server certificate](master_communications_encryption.md). If no certificate was given ([TLS\_KEY\_FILE](master_tls_key_file.md)) or if it was invalid, the server will not create a socket to receive TLS connections and an attempt by a client to connect to the TLS port will result in a 6414 error. Verify that the TLS\_KEY\_FILE configuration parameter is correct. If the certificate is not valid, the error log (ads\_err.dbf) should contain more information.

If you are attempting a TLS connection, verify that the port number is correct and that you have specified the [CommType](ace_adsconnect101.md) as TLS. If a TCP/IP connection is specified when connecting to the TLS port, it will result in a 6414 error.
