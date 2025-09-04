---
title: Ade Adsstmtenableencryption
slug: ade_adsstmtenableencryption
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsstmtenableencryption.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 8866abccb8ba84e54f58069deb166251cae33e9c
---

# Ade Adsstmtenableencryption

AdsStmtEnableEncryption

TAdsQuery.AdsStmtEnableEncryption

Advantage TDataSet Descendant

| TAdsQuery.AdsStmtEnableEncryption  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Encrypts the cursor generated after executing the SQL statement.

Syntax

procedure AdsStmtEnableEncryption( strPassword : string );

Parameter

| strPassword | Case-sensitive text encryption password. |

Description

When using the [default encryption](master_encryption.md), enabling encryption on the query component ensures that the data travels across the network in encrypted format. When encryption is enabled for the query component, the cursor generated is encrypted on the server with the specified encryption password. The encrypted data is automatically decrypted by the client.

When using AES encryption, it is not necessary to use this method. If any table involved in a query is encrypted with AES, then the resulting cursor will also be encrypted with AES (using a random key). Note too, that the server handles all AES encryption. Therefore, to ensure that data is encrypted on the wire, use [communications encryption](master_communications_encryption.md).

This API provides additional security for your data. When you use encrypted free tables in SQL statements, you must use [AdsStmtSetTablePassword](ade_adsstmtsettablepassword.md) to provide the encryption passwords for the base tables. This allows the server to read the data in those tables. If the SQL statements result in static cursors (e.g., a join), the resulting rowset is, by default, not encrypted when using the [default encryption](master_encryption.md). This means that the data will be transmitted to the client in the clear. If this is not desirable, you can use the AdsStmtEnableEncryption API. This ensures that all static cursors are encrypted on the server. If your SELECT statements result only in live cursors, then there is no temporary table (cursor) created by the server, and the data is already secure as long as the base table is encrypted.

This function affects cursors created in subsequent execution of the statement handle.

Note The encrypted cursor is always read-only. See [AdsStmtSetTablePassword](ade_adsstmtsettablepassword.md) for information about how to create an updatable cursor with encrypted data.

Example

AdsQuery1.Close;

AdsQuery1.SQL.Clear;

AdsQuery1.SQL.Add('Select \* from Demo10 where LastName = ''Coles''');

AdsQuery1.AdsStmtEnableEncryption( 'Secret' ); // Encrypts generated cursors to be sent over the network

AdsQuery1.AdsStmtSetTablePassword( 'Demo10', 'Secret' ); // Sets the password for the encrypted table

AdsQuery1.Open;

See Also

[AdsStmtDisableEncryption](ade_adsstmtdisableencryption.md)

[AdsStmtSetTablePassword](ade_adsstmtsettablepassword.md)

[AdsStmtClearTablePasswords](ade_adsstmtcleartablepasswords.md)
