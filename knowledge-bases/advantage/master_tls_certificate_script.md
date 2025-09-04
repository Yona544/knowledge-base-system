TLS Certificate Script




Advantage Database Server 12  

TLS Certificate Script

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TLS Certificate Script  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - TLS Certificate Script Advantage Concepts master\_TLS\_Certificate\_Script Advantage Concepts > Advantage Functionality > Communications Encryption > TLS Certificate Script / Dear Support Staff, |  |
| TLS Certificate Script  Advantage Concepts |  |  |  |  |

If you run the following commands (e.g., in a Windows batch file), it produces a clientcert.pem file, which is the file specified in the client's [connection option](ace_adsconnect101.htm) TLSCertificate.  It also produces a servercert.pem file, which is referred to by the server configuration parameter [TLS\_KEY\_FILE](master_tls_key_file.htm).

To use this script, place it in a directory such as c:\adscert along with the openssl.cnf file. Make sure the "dir" key value in the openssl.cnf file matches the directory you choose.

if not exist private md private

if not exist certs md certs

 

if not exist index.txt copy NUL index.txt

if not exist serial echo 01 > serial

 

 

set OPENSSL\_CONF=.\openssl.cnf

 

rem This creates clientcert.pem, which is the public root certificate for our "CA"

rem The private key ends up in the private directory (specified in the .cnf file by the

rem private\_key value)

openssl req -x509 -newkey rsa:2048 -out clientcert.pem -outform PEM -passout pass:mypassword

 

rem  The result of this is:

rem   testkey.pem:  The private key

rem   testreq.pem:  The certificate request

openssl req -sha1 -newkey rsa:2048 -passout pass:mypassword -keyout testkey.pem -keyform PEM -out testreq.pem -outform PEM -subj /C=us/ST=ST/L=MyCity/CN=www.mysite.com/O=myorganization

 

rem This creates the signed certificate

openssl ca -in testreq.pem -passin pass:mypassword -out signedcert.pem

 

 

rem Combine the private key and the signed certificate into a single PEM file

rem for the server.

copy /b testkey.pem+signedcert.pem servercert.pem