TLS Certificates




Advantage Database Server 12  

TLS Certificates

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TLS Certificates  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - TLS Certificates Advantage Concepts master\_TLS\_Certificates Advantage Concepts > Advantage Functionality > Communications Encryption > TLS Certificates / Dear Support Staff, |  |
| TLS Certificates  Advantage Concepts |  |  |  |  |

Creating a Self-Signed Certificate for TLS Communications

In order to use Transport Layer Security (TLS), it is necessary to have a digitally signed certificate. These certificates can be purchased through a number of companies such as Thawte, VeriSign, and GeoTrust.

Depending on the usage scenario and requirements, however, you may want to use a self-signed certificate. There are a number of books and web sites that discuss the creation of digital certificates. The following is not meant to be a replacement for that information but rather is a very brief overview of steps that can be used to create a self-signed certificate on a Windows PC.

|  |  |
| --- | --- |
| · | Make sure the OpenSSL command line executable (openssl.exe in Windows) is in your path along with the libraries libeay32.dll and ssleay32.dll. |

|  |  |
| --- | --- |
| · | Set the OPENSSL\_CONF environment variable to point to your OpenSSL configuration file (openssl.cnf). |

|  |  |
| --- | --- |
| · | Edit the configuration file (openssl.cnf) to verify it has the desired settings. Examine all the values in it, particularly the paths and distinguished name information (common name, email address, etc.). |

|  |  |
| --- | --- |
| · | Run the commands to create the public and private key for the "certificate authority", the signing request, and the signed certificate. Example commands for doing this are shown in [this script](master_tls_certificate_script.htm). |

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