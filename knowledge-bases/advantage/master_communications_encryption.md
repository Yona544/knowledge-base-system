Communications Encryption




Advantage Database Server 12  

Communications Encryption

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Communications Encryption  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Communications Encryption Advantage Concepts master\_Communications\_Encryption Advantage Concepts > Advantage Functionality > Communications Encryption / Dear Support Staff, |  |
| Communications Encryption  Advantage Concepts |  |  |  |  |

Encrypting communications between Advantage clients and Advantage Database Server is an important part of securing data and preventing unauthorized viewing of it. If communication data is not encrypted, it is possible for table data to be viewed (sniffed) when it is transmitted over a network.

If the connection to Advantage Database Server is made through a virtual private network (VPN) that makes use of a cryptographic tunneling protocol, then the data will be encrypted and no other encryption may be necessary. In many situations, however, the data will be transmitted in the clear. If an application is being run in such a situation, then it may be desirable to enable encryption at the Advantage level.

You can enable communications encryption when using a data dictionary by setting the ENCRYPT\_COMMUNICATION database property via [sp\_ModifyDatabase()](master_sp_modifydatabase.htm). The property can also be set by accessing the dictionary properties dialog in Advantage Data Architect. If encryption is enabled by this mechanism, the Advantage client and Advantage Database Server negotiate a 160-bit symmetric key and encrypt all communications using RC4. This encryption can be used on top of both TCP/IP and UDP communications.

Beginning in v10.1, Transport Layer Security (TLS) is another option for encrypting communications. This requires an optional module based on libraries from the OpenSSL Project. For information on obtaining this add-on, contact your Advantage sales representative or visit www.AdvantageDatabase.com.

TLS operates over TCP/IP and uses RSA for the key exchange, 128-bit or 256-bit Advanced Encryption Standard (AES) for encryption and SHA-1 (Secure Hash Algorithm) for message authentication. These cipher suites are referred to as AES128-SHA and AES256-SHA. In addition, the cipher suite RC4-MD5, which uses RSA for the key exchange, 128-bit RC4 for encryption and MD5 for message authentication is also available.

TLS can be used with both data dictionary connections and free table connections. In addition to acquiring the add-on module, you must specify the [TLS\_KEY\_FILE](master_tls_key_file.htm) configuration option for the server and provide the necessary connection options from the client.

Specifically, the following steps are required on the server. Note that the configuration information can be provided in the configuration file (in the Advantage\Configuration registry in Windows or in ads.conf in Linux) or as command line parameters when starting the server.

|  |  |
| --- | --- |
| · | In the server configuration, specify the [TLS\_KEY\_FILE](master_tls_key_file.htm) value or the TLSKeyFile command line parameter. This refers to the certificate file (PEM) format that contains both the private key and the signed certificate for the TLS communications. You can obtain a digital certificate through companies such as Thawte, VeriSign, and GeoTrust. You can also create a [self-signed certificate](master_tls_certificates.htm). |

|  |  |
| --- | --- |
| · | If the certificate file is password protected, specify the [TLS\_KEY\_PASSWORD](master_tls_key_password.htm) configuration parameter or the TLSKeyPassword command line parameter. |

|  |  |
| --- | --- |
| · | To restrict the available cipher suites, specify the [TLS\_CIPHERS](master_tls_ciphers.htm) configuration parameter or the TLSCiphers command line parameter. For example, to restrict the ciphers to use AES, specify a value of "AES128-SHA:AES256-SHA". |

|  |  |
| --- | --- |
| · | The default port for TLS communications is 6263. To change this specify the [RECEIVE\_TLS\_PORT](master_receive_tls_port.htm) configuration parameter. |

At the client, it is necessary to specify TLS communications and provide the necessary certificate information through [connection string parameters](ace_adsconnect101.htm).

|  |  |
| --- | --- |
| · | Specify the communications type as TLS (e.g., CommType=TLS;) |

|  |  |
| --- | --- |
| · | Specify the certificate file that contains the public key information for the server's certificate (e.g., TLSCertificate=c:\mypath\clientcert.pem) |

|  |  |
| --- | --- |
| · | Specify the expected common name for the server certificate (e.g., TLSCommonName=www.myserver.com). |

|  |  |
| --- | --- |
| · | It is also possible to restrict the allowed cipher suite with the TLSCiphers option (e.g., "TLSCiphers=AES256-SHA;" will limit the communication to only 256-bit AES.). Note that in order to successfully connect to the server, a shared cipher must be specified. |

|  |  |
| --- | --- |
| · | If the connection specifies the port number, be sure to use the TLS port (default is 6263). If a port is not specified, the normal discovery process will determine the port number from the server. |