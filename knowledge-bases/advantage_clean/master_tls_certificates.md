---
title: Master Tls Certificates
slug: master_tls_certificates
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_tls_certificates.htm
source: Advantage CHM
tags:
  - master
checksum: 99d36364e0977270ecbd0e58adb6fdd36f5ae744
---

# Master Tls Certificates

TLS Certificates

TLS Certificates

Advantage Concepts

| TLS Certificates  Advantage Concepts |  |  |  |  |

Creating a Self-Signed Certificate for TLS Communications

In order to use Transport Layer Security (TLS), it is necessary to have a digitally signed certificate. These certificates can be purchased through a number of companies such as Thawte, VeriSign, and GeoTrust.

Depending on the usage scenario and requirements, however, you may want to use a self-signed certificate. There are a number of books and web sites that discuss the creation of digital certificates. The following is not meant to be a replacement for that information but rather is a very brief overview of steps that can be used to create a self-signed certificate on a Windows PC.

- Make sure the OpenSSL command line executable (openssl.exe in Windows) is in your path along with the libraries libeay32.dll and ssleay32.dll.

- Set the OPENSSL\_CONF environment variable to point to your OpenSSL configuration file (openssl.cnf).

- Edit the configuration file (openssl.cnf) to verify it has the desired settings. Examine all the values in it, particularly the paths and distinguished name information (common name, email address, etc.).

- Run the commands to create the public and private key for the "certificate authority", the signing request, and the signed certificate. Example commands for doing this are shown in [this script](master_tls_certificate_script.md).

Example openssl.cnf file

 

openssl\_conf = openssl\_init

 

[openssl\_init]

alg\_section = algs

 

[ ca ]

default\_ca = MyCertAuth

 

 

[ algs ]

fips\_mode = yes

 

[ MyCertAuth ]

dir              = c:/adscert

certificate      = $dir/clientcert.pem

database         = $dir/index.txt

new\_certs\_dir    = $dir/certs

private\_key      = $dir/private/certificateauthoritykey.pem

serial           = $dir/serial

 

default\_crl\_days = 7

default\_days     = 365

default\_md       = sha1

 

policy           = MyCertAuth\_policy

x509\_extensions  = certificate\_extensions

 

name\_opt        = ca\_default            # Subject Name options

cert\_opt        = ca\_default            # Certificate field options

 

[ MyCertAuth\_policy ]

commonName             = match

stateOrProvinceName    = supplied

countryName            = supplied

emailAddress           = optional

organizationName       = supplied

organizationalUnitName = optional

 

[ certificate\_extensions ]

basicConstraints = CA:false

 

subjectKeyIdentifier=hash

authorityKeyIdentifier=keyid,issuer

 

 

[ req ]

default\_bits            = 2048

default\_keyfile         = c:/adscert/private/certificateauthoritykey.pem

default\_md              = sha1

 

prompt                  = no

 

distinguished\_name      = root\_ca\_distinguished\_name

x509\_extensions         = root\_ca\_extensions

 

[ root\_ca\_distinguished\_name ]

commonName              = www.mysite.com

stateOrProvinceName     = ST

countryName             = US

emailAddress            = my@email.com

organizationName        = myorganization

 

[ root\_ca\_extensions ]

basicConstraints        = CA:true
