---
title: Ace Adsstmtenableencryption
slug: ace_adsstmtenableencryption
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsstmtenableencryption.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 008ff5ad2cc11df96d7df1fced61f3eee3f88e0d
---

# Ace Adsstmtenableencryption

AdsStmtEnableEncryption

AdsStmtEnableEncryption

Advantage Client Engine

| AdsStmtEnableEncryption  Advantage Client Engine |  |  |  |  |

Encrypts the cursor generated after executing the SQL statement.

Syntax

| UNSIGNED32 | AdsStmtEnableEncryption( ADSHANDLE hStatement,  UNSIGNED8 \*pucPassword ); |

Parameters

| hStatement(I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.md). |
| pucPassword(I) | Case-sensitive text encryption password. |

Remarks

Enabling encryption on the statement handle ensures that the data travels across the network in encrypted format when using default encryption. When encryption is enabled for the statement handle, the cursor generated is encrypted on the server with the specified encryption password. The encrypted data is automatically decrypted by the client.

This API is not necessary when using [AES encryption](master_encryption.md). If any table involved in a query uses AES encryption, then the resulting cursor will be encrypted with AES (using a random key). In order to ensure data on the wire is encrypted when using AES, use [communications encryption](master_communications_encryption.md).

This API provides additional security for your data. When you use encrypted tables with the default encryption in SQL statements, you must use AdsStmtSetTablePassword to provide the encryption passwords for the base tables. This allows the server to read the data in those tables. If the SQL statements result in static cursors (e.g., a join), then the resulting rowset is, by default, not encrypted. This means that the data will be transmitted to the client in the clear. If this is not desirable, you can use the AdsStmtEnableEncryption API. This ensures that all cursors are encrypted on the server. If your SELECT statements result only in live cursors, then the cursor will now be a static cursor and a temporary table (cursor) is created by the server.

This function affects cursors created in the subsequent query executing on the specified statement handle.

Note The encrypted cursor is always read-only. See [AdsStmtSetTablePassword](ace_adsstmtsettablepassword.md) for information about creating an updatable cursor with encrypted data.

Example

[Click Here](ace_more_examples.md#adsstmtenableencryption_example)

See Also

[AdsStmtDisableEncryption](ace_adsstmtdisableencryption.md)

[AdsStmtSetTablePassword](ace_adsstmtsettablepassword.md)

[AdsStmtClearTablePasswords](ace_adsstmtcleartablepasswords.md)
