Strong Encryption Usage Overview




Advantage Database Server 12  

Strong Encryption Usage Overview

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Strong Encryption Usage Overview  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Strong Encryption Usage Overview Advantage Concepts Master\_SE\_Usage\_Overview Advantage Concepts > Advantage Functionality > Encryption > Strong Encryption Usage Overview / Dear Support Staff, |  |
| Strong Encryption Usage Overview  Advantage Concepts |  |  |  |  |

Beginning with v10.1, Advantage provides the ability to encrypt data with 128-bit and 256-bit Advanced Encryption Standard (AES) and to use Transport Layer Security (TLS) for encrypted communications. This topic provides an overview of the basic steps necessary use strong encryption in an application. For more details, refer to the [data encryption overview](master_encryption.htm) and [communications encryption overview](master_communications_encryption.htm).

Required Libraries

In order to use AES encryption and TLS communications, you must use the FIPS Encryption Security Option.  Please contact your Advantage sales representative or visit [http://scn.sap.com/community/ads](http://www.sybase.com/products/databasemanagement/advantagedatabaseserver/encryption "http://scn.sap.com/community/ads") for licensing information. The module contains two libraries that the server and client must be able to access. Instructions are included for distributing the libraries.

Supported Table Types

AES encryption can be used with the Advantage proprietary (ADT) and Visual FoxPro (VFP) table types. However, the new encryption scheme requires additional header and table information. Tables that support AES encryption are not compatible with earlier versions of Advantage.

Data dictionaries, data dictionary bound tables, and free tables can be encrypted with AES. However, due to the cost of generating the key data and verifying the password, using AES encryption with free tables may add significant processing time to an application. More information is available in the [encryption overview](master_encryption.htm).

Using AES with New Data

When an application creates new tables and new data dictionaries, Advantage creates the table structure to support the encryption type that is specified on the connection on which the new table or dictionary is created. For example, if you create a new free table connection with a [connection option](ace_adsconnect101.htm) of "EncryptionType=AES256;" or a [DataEncryptionType](ade_dataencryptiontype.htm) of etAdsAES256 (in Delphi), then any new ADT or VFP table or data dictionary created on that connection will support AES encryption. When an application makes a connection to a data dictionary that supports AES encryption, that connection acquires the encryption type of the dictionary and any table encrypted on that connection will use AES encryption.

When creating a new data dictionary to support AES encryption, it is necessary to supply a data dictionary password. This password is used to create the key data that is used with the AES encryption for the dictionary and all tables. This dictionary password must be supplied on the connection that is used for creating the dictionary. It can be supplied as a connection string option such as "[DDPassword=thepassword;](ace_adsconnect101.htm)" or via the [EncryptionOptions.DataDictionaryPassword](ade_datadictionarypassword.htm) in a Delphi application. If you use SQL to create the dictionary the password can be provided via the DDPassword option in the [CREATE DATABASE](master_create_database.htm) statement.

Using AES with Existing Data

In order to use AES encryption on existing data dictionaries and tables that were created with the default encryption type, it is necessary to convert them to support AES encryption.

|  |  |
| --- | --- |
| · | Convert a table's structure to support AES and encrypt it with [sp\_EncryptTable](master_sp_encrypttable.htm). |

|  |  |
| --- | --- |
| · | Convert an existing dictionary to support AES encryption with [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm). |

Encrypting Communications

In order to encrypt communications data between client and server with AES, use Transport Layer Security (TLS). Specify the communication type as TLS (eg., use [CommType=TLS](ace_adsconnect101.htm); in the connection string or specify the [TAdsConnection.CommunicationType](ade_communicationtype.htm) as ctAdsTLS). Refer to the [communications encryption overview](master_communications_encryption.htm) for details on this.

Providing Dictionary Password Securely

When using AES encryption with data dictionaries, a data dictionary password is required. This password can be supplied with the connection from the client (as described above for creating new dictionaries). This works well for development and for local server applications. However, in a production environment, it is probably not desirable to make the application provide the dictionary password because it means that it must be hard coded in the application, provided by the user, or extracted from the local machine in some other fashion.

When using Advantage Database Server, the dictionary password can be supplied as a [command line parameter or through the SE\_Passwords configuration option](master_se_passwords.htm) when the server is started. This can provide a much more secure method of providing the dictionary password.

Application Feedback

An application can use the following system procedures to retrieve information regarding FIPS mode, AES encryption, and TLS communications.

|  |  |
| --- | --- |
| · | [sp\_GetTableEncryptionType](master_sp_gettableencryptiontype.htm): Retrieve the encryption type associated with a specific table. |

|  |  |
| --- | --- |
| · | [sp\_GetSecurityInfo](master_sp_getsecurityinfo.htm): Retrieve the connection's encryption type, the type of communication (e.g., TLS), and whether or not the application is running in FIPS mode. |