---
title: Ace Adsstmtsettablepassword
slug: ace_adsstmtsettablepassword
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtsettablepassword.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5597819ccb1f203d6c2a120a72323d14ae94a9b1
---

# Ace Adsstmtsettablepassword

AdsStmtSetTablePassword

AdsStmtSetTablePassword

Advantage Client Engine

| AdsStmtSetTablePassword  Advantage Client Engine |  |  |  |  |

Sets a base table's encryption password that will be used when the SQL statement is executed.

Syntax

| UNSIGNED32 | AdsStmtSetTablePassword( ADSHANDLE hStatement,  UNSIGNED8 \*pucTableName,  UNSIGNED8 \*pucPassword ); |

Parameters

| hStatement(I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |
| pucTableName(I) | Name of the base table. |
| pucPassword(I) | Case-sensitive text encryption password. |

Remarks

If there are encrypted records in the base table(s) in an SQL statement, the encryption password(s) for the records must be provided before executing the query. Otherwise, the records will not be correctly considered for the result set. See [AdsEnableEncryption](ace_adsenableencryption.md) for additional information about encryption with Advantage.

If the statement executed is an update statement, the rows modified will be encrypted with the specified encryption password.

The encryption password for the specified table will be used for all subsequent query execution on the statement handle. If the base table has no encryption information before the statement is executed, the specified encryption password will be stored in the table header when the statement is executed.

If the statement handle was created on a database connection), setting the encryption password for database tables) is ignored. The database tables encryption password is stored in the database and automatically available to the authenticated users.

Note If the resulting cursor is read-only, all rows will be decrypted by the server even though the data may be encrypted in the base table. To generate an encrypted read-only cursor, use [AdsStmtEnableEncryption](ace_adsstmtenableencryption.md).

Example

[Click Here](ace_more_examples.md#adsstmtsettablepassword_example)

See Also

[AdsStmtEnableEncryption](ace_adsstmtenableencryption.md)

[AdsStmtDisableEncryption](ace_adsstmtdisableencryption.md)

[AdsStmtClearTablePasswords](ace_adsstmtcleartablepasswords.md)
