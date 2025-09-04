---
title: Ace Adsddfreetable
slug: ace_adsddfreetable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddfreetable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 4b40390b546020484204ed7711fce0cab42e1665
---

# Ace Adsddfreetable

AdsDDFreeTable

AdsDDFreeTable

Advantage Client Engine

| AdsDDFreeTable  Advantage Client Engine |  |  |  |  |

Alters an ADT table and makes it a free Advantage table file. A free Advantage table file can be used without the need of an Advantage Data Dictionary.

Syntax

UNSIGNED32 AdsDDFreeTable

(

UNSIGNED8 \*pucTableName,

UNSIGNED8 \*pucPassword

)

Parameters

| pucTableName (I) | The fully qualified path and table name of the table to be freed. |
| pucPassword (I) | If the table is encrypted, this parameter can be used to specify the table password. If the table is not encrypted this parameter can be NULL. |

Special Return Codes

| AE\_FREETABLEFAILED | The error text accompanying this code will have a description of the specific failure. |

Remarks

AdsDDFreeTable should only be used if the data dictionary the table belongs to no longer exists or is not available. If the data dictionary is available, and you want to remove a table, use the AdsDDRemoveTable API instead. The AdsDDRemoveTable API will correctly handle referential integrity rules, permissions, and other adjustments that need to be made when removing a table to maintain the integrity of the data dictionary.

This is a client-side function that must have direct access to the file passed in the pucTableName parameter. The Advantage Database Server is not used to modify the table, rather raw file I/O operations are used.

The password that is provided depends on the [encryption type](master_encryption.md). If the default encryption type (available beginning in v6) is used, then the password needs to be the table encryption password that is specified in the dictionary property. If AES encryption is used (available in v10.1 and later), then the password is the dictionary password (see [SE\_Passwords](master_se_passwords.md)).

See Also

[AdsDDRemoveTable](ace_adsddremovetable.md)

[AdsDDAddTable](ace_adsddaddtable.md)
