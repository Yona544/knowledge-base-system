---
title: Master System Dictionary
slug: master_system_dictionary
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_system_dictionary.htm
source: Advantage CHM
tags:
  - master
checksum: 5ac6a980b76b65966cfb716a2ca7316452427859
---

# Master System Dictionary

system.dictionary

system.dictionary

Advantage SQL Engine

| system.dictionary  Advantage SQL Engine |  |  |  |  |

Contains a single row for all dictionary properties.

| Field Name | Field Type | Field Size | Description |
| Version\_Major | Short | 2 | Major version number of the dictionary. |
| Version\_Minor | Short | 2 | Minor version number of the dictionary. |
| Default\_Table\_Path | Character | 260 | Default table path for the dictionary. |
| Temp\_Table\_Path | Character | 260 | Temporary table path for the dictionary. |
| Log\_In\_Required | Logical | 1 | Determines if a username and password is required for a database connection. |
| Verify\_Access\_Rights | Logical | 1 | Determines if the users access rights when opening a database table, view, or executing a stored procedure are enforced. |
| Encrypt\_Table\_Password | Charcter | 20 | Password used for encrypting tables. This value is only returned for administrative data dictionary connections. |
| Encrypt\_New\_Table | Logical | 1 | Determines if a new table added to or created in the data dictionary will be encrypted. |
| Enable\_Internet | Logical | 1 | Determines if Internet access is allowed to this data dictionary. |
| Internet\_Security\_Level | Short | 2 | The security level for communications over the Internet. |
| Max\_Failed\_Attempts | Short | 2 | The maximum number of failed connection attempts allowed before Internet access is shut off. |
| Logins\_Disabled | Logical | 1 | Determines if logins are currently disabled. See [Disabling Database Logins](master_disabling_database_logins.md) for more details. |
| Logins\_Disabled\_msg | Memo | variable | Specifies the custom error string that will be returned to users attempting to connect to the database when logins are disabled. |
| Comment | Memo | variable | Description of the dictionary. |
| User\_Defined\_Prop | Binary | variable | The user defined property. |
| FTS\_Delimiters | Memo | variable | FTS delimiter characters. |
| FTS\_Noise\_Words | Memo | variable | FTS noise words. |
| FTS\_DropChars | Memo | variable | FTS drop characters. |
| FTS\_Conditional\_Chars | Memo | variable | FTS conditional drop characters. |
| Dictionary\_Encrypted | Logical | 1 | Determines if the data dictionary file is encrypted. |
| Encrypt\_Indexes | Logical | 1 | Determines if indexes are encrypted. |
| Encrypt\_Communication | Logical | 1 | Determines if communication between the client and server is encrypted. |
| Data\_Encryption\_Type | Integer | 4 | Specifies the type of encryption that is used for newly encrypted tables. This property is set when the dictionary is created. Possible values include ADS\_ENCRYPTION\_RC4 (3), ADS\_ENCRYPTION\_AES128 (5), and ADS\_ENCRYPTION\_AES256 (6). It is possible to change the encryption type with the system procedure [sp\_SetDDEncryptionType](master_sp_setddencryptiontype.md). |
| Query\_Via\_Root | Integer | 4 | This property specifies whether passthrough queries are allowed through the [root dictionary](master_root_dictionary.md). Valid values are a combination (bitmask) of ADS\_DD\_QVR\_OPT\_QUERY (0x01) and ADS\_DD\_QVR\_OPT\_PROCEDURE (0x02). The first value indicates that passthrough queries are allowed. The second value indicates that passthrough procedure calls are allowed. This property is checked by the Advantage Web Platform when queries and procedure calls are made "through" the root dictionary to another dictionary. If the value is not set, then the request is denied. This property was introduced primarily for use by the Web Administrator Utility. |
