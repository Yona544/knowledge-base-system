AdsStmtEnableEncryption




Advantage Database Server 12  

AdsStmtEnableEncryption

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtEnableEncryption  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtEnableEncryption Advantage Client Engine ace\_Adsstmtenableencryption Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtEnableEncryption  Advantage Client Engine |  |  |  |  |

Encrypts the cursor generated after executing the SQL statement.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtEnableEncryption( ADSHANDLE hStatement,  UNSIGNED8 \*pucPassword ); |

Parameters

|  |  |
| --- | --- |
| hStatement(I) | Handle of an SQL statement created by a call to [AdsCreateSQLStatement](ace_adscreatesqlstatement.htm). |
| pucPassword(I) | Case-sensitive text encryption password. |

Remarks

Enabling encryption on the statement handle ensures that the data travels across the network in encrypted format when using default encryption. When encryption is enabled for the statement handle, the cursor generated is encrypted on the server with the specified encryption password. The encrypted data is automatically decrypted by the client.

This API is not necessary when using [AES encryption](master_encryption.htm). If any table involved in a query uses AES encryption, then the resulting cursor will be encrypted with AES (using a random key). In order to ensure data on the wire is encrypted when using AES, use [communications encryption](master_communications_encryption.htm).

This API provides additional security for your data. When you use encrypted tables with the default encryption in SQL statements, you must use AdsStmtSetTablePassword to provide the encryption passwords for the base tables. This allows the server to read the data in those tables. If the SQL statements result in static cursors (e.g., a join), then the resulting rowset is, by default, not encrypted. This means that the data will be transmitted to the client in the clear. If this is not desirable, you can use the AdsStmtEnableEncryption API. This ensures that all cursors are encrypted on the server. If your SELECT statements result only in live cursors, then the cursor will now be a static cursor and a temporary table (cursor) is created by the server.

This function affects cursors created in the subsequent query executing on the specified statement handle.

Note The encrypted cursor is always read-only. See [AdsStmtSetTablePassword](ace_adsstmtsettablepassword.htm) for information about creating an updatable cursor with encrypted data.

Example

[Click Here](ace_more_examples.htm#adsstmtenableencryption_example)

See Also

[AdsStmtDisableEncryption](ace_adsstmtdisableencryption.htm)

[AdsStmtSetTablePassword](ace_adsstmtsettablepassword.htm)

[AdsStmtClearTablePasswords](ace_adsstmtcleartablepasswords.htm)