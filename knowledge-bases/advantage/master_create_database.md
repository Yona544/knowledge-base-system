CREATE DATABASE




Advantage Database Server 12  

CREATE DATABASE

Advantage SQL Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| CREATE DATABASE  Advantage SQL Engine |  |  | Feedback on: Advantage Database Server 12 - CREATE DATABASE Advantage SQL Engine master\_Create\_database Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| CREATE DATABASE  Advantage SQL Engine |  |  |  |  |

Creates a new Advantage Data Dictionary

Syntax

CREATE DATABASE <database name> [ PASSWORD <adssys password> ] [ DESCRIPTION <database description> ]     [ ENCRYPT <TRUE | FALSE> ] [ ENCRYPTIONTYPE AES128 | AES256 | RC4 ]

[ DDPASSWORD <dictionary password> ]

 

database name ::= The path of the new data dictionary

adssys password ::= A password for the adssys administrator user

database description ::= A description of the data dictionary

dictionary password ::= Password for table and dictionary encryption when using AES128 or AES256 encryption

Remarks

CREATE DATABASE creates a new [Advantage Data Dictionary](master_advantage_data_dictionary.htm) and sets its description and password. By including the ENCRYPT keyword, the data dictionary (the .ADD file) will be encrypted if TRUE is specified. If FALSE is specified, it will not be encrypted (the default is FALSE).

The default [encryption type](master_encryption.htm) is RC4. If one of the AES encryption types is used, then the DDPassword option (dictionary password) must also be provided. The dictionary password is used for encrypting the dictionary files (if the ENCRYPT TRUE option is provided) and any tables in the dictionary that are encrypted.

The encryption type of an existing data dictionary (and whether or not the dictionary is encrypted) can be changed via the [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.htm) system procedure.

When called on a dictionary connection, CREATE DATABASE can only be executed by the ADSSYS user or a member of the DB:admin group.

Example(s)

CREATE DATABASE "n:\MyData\myData.ADD" PASSWORD 'admin' DESCRIPTION 'MyData Data Dictionary' ENCRYPT TRUE                        EncryptionType AES256 DDPassword 'ddpass';

CREATE DATABASE "c:\program files\my data\new.add";

CREATE DATABASE newDB;