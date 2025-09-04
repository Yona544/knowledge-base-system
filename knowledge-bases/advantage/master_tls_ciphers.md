TLS\_Ciphers




Advantage Database Server 12  

TLS\_Ciphers

Advantage Database Server

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TLS\_Ciphers  Advantage Database Server |  |  | Feedback on: Advantage Database Server 12 - TLS\_Ciphers Advantage Database Server Master\_TLS\_Ciphers Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TLS\_Ciphers  Advantage Database Server |  |  |  |  |

The TLS\_CIPHERS configuration parameter can be used for defining which cipher suites are allowed for Transport Layer Security (TLS) [communications](master_communications_encryption.htm). If multiple ciphers are allowed, they can be delimited with commas or colons.  Valid values include:

|  |  |
| --- | --- |
| · | AES128-SHA - 128-bit Advanced Encryption Standard (AES) for encryption and SHA-1 (Secure Hash Algorithm) for message authentication. |

|  |  |
| --- | --- |
| · | AES256-SHA - 256-bit Advanced Encryption Standard (AES) for encryption and SHA-1 (Secure Hash Algorithm) for message authentication. |

|  |  |
| --- | --- |
| · | RC4-MD5 - 128-bit RC4 for encryption and MD5 for message authentication. Note that this is not a FIPS-compliant cipher. |

These names can be shortened to just the encryption name (without the hash name). For example, to specify the AES ciphers:

TLS\_CIPHERS=AES128:AES256

This option is equivalent to the command line parameter /TLSCiphers