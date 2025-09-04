---
title: Error X509 Certificate Errors
slug: error_x509_certificate_errors
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_x509_certificate_errors.htm
source: Advantage CHM
tags:
  - error
checksum: c09f45cdbab52f5af5c6c985b97a2da4d58e6252
---

# Error X509 Certificate Errors

X509 Certificate Errors

X509 Certificate Errors

Advantage Error Guide

| X509 Certificate Errors  Advantage Error Guide |  |  |  |  |

When using [TLS Communications](master_communications_encryption.md), the certificate is verified by the OpenSSL libraries. If errors occur, the connection will not be established. The following error numbers and names are possible.  For more detailed information on a particular error, please see <http://www.openssl.org/docs/crypto/X509_STORE_CTX_get_error.html>.

| 2 | X509\_V\_ERR\_UNABLE\_TO\_GET\_ISSUER\_CERT |
| 3 | X509\_V\_ERR\_UNABLE\_TO\_GET\_CRL |
| 4 | X509\_V\_ERR\_UNABLE\_TO\_DECRYPT\_CERT\_SIGNATURE |
| 5 | X509\_V\_ERR\_UNABLE\_TO\_DECRYPT\_CRL\_SIGNATURE |
| 6 | X509\_V\_ERR\_UNABLE\_TO\_DECODE\_ISSUER\_PUBLIC\_KEY |
| 7 | X509\_V\_ERR\_CERT\_SIGNATURE\_FAILURE |
| 8 | X509\_V\_ERR\_CRL\_SIGNATURE\_FAILURE |
| 9 | X509\_V\_ERR\_CERT\_NOT\_YET\_VALID |
| 10 | X509\_V\_ERR\_CERT\_HAS\_EXPIRED |
| 11 | X509\_V\_ERR\_CRL\_NOT\_YET\_VALID |
| 12 | X509\_V\_ERR\_CRL\_HAS\_EXPIRED |
| 13 | X509\_V\_ERR\_ERROR\_IN\_CERT\_NOT\_BEFORE\_FIELD |
| 14 | X509\_V\_ERR\_ERROR\_IN\_CERT\_NOT\_AFTER\_FIELD |
| 15 | X509\_V\_ERR\_ERROR\_IN\_CRL\_LAST\_UPDATE\_FIELD |
| 16 | X509\_V\_ERR\_ERROR\_IN\_CRL\_NEXT\_UPDATE\_FIELD |
| 17 | X509\_V\_ERR\_OUT\_OF\_MEM |
| 18 | X509\_V\_ERR\_DEPTH\_ZERO\_SELF\_SIGNED\_CERT |
| 19 | X509\_V\_ERR\_SELF\_SIGNED\_CERT\_IN\_CHAIN |
| 20 | X509\_V\_ERR\_UNABLE\_TO\_GET\_ISSUER\_CERT\_LOCALLY |
| 21 | X509\_V\_ERR\_UNABLE\_TO\_VERIFY\_LEAF\_SIGNATURE |
| 22 | X509\_V\_ERR\_CERT\_CHAIN\_TOO\_LONG |
| 23 | X509\_V\_ERR\_CERT\_REVOKED |
| 24 | X509\_V\_ERR\_INVALID\_CA |
| 25 | X509\_V\_ERR\_PATH\_LENGTH\_EXCEEDED |
| 26 | X509\_V\_ERR\_INVALID\_PURPOSE |
| 27 | X509\_V\_ERR\_CERT\_UNTRUSTED |
| 28 | X509\_V\_ERR\_CERT\_REJECTED |
| 29 | X509\_V\_ERR\_SUBJECT\_ISSUER\_MISMATCH |
| 30 | X509\_V\_ERR\_AKID\_SKID\_MISMATCH |
| 31 | X509\_V\_ERR\_AKID\_ISSUER\_SERIAL\_MISMATCH |
| 32 | X509\_V\_ERR\_KEYUSAGE\_NO\_CERTSIGN |
| 33 | X509\_V\_ERR\_UNABLE\_TO\_GET\_CRL\_ISSUER |
| 34 | X509\_V\_ERR\_UNHANDLED\_CRITICAL\_EXTENSION |
| 35 | X509\_V\_ERR\_KEYUSAGE\_NO\_CRL\_SIGN |
| 36 | X509\_V\_ERR\_UNHANDLED\_CRITICAL\_CRL\_EXTENSION |
| 37 | X509\_V\_ERR\_INVALID\_NON\_CA |
| 38 | X509\_V\_ERR\_PROXY\_PATH\_LENGTH\_EXCEEDED |
| 39 | X509\_V\_ERR\_KEYUSAGE\_NO\_DIGITAL\_SIGNATURE |
| 40 | X509\_V\_ERR\_PROXY\_CERTIFICATES\_NOT\_ALLOWED |
| 41 | X509\_V\_ERR\_INVALID\_EXTENSION |
| 42 | X509\_V\_ERR\_INVALID\_POLICY\_EXTENSION |
| 43 | X509\_V\_ERR\_NO\_EXPLICIT\_POLICY |
| 44 | X509\_V\_ERR\_UNNESTED\_RESOURCE |
| 50 | X509\_V\_ERR\_APPLICATION\_VERIFICATION |
