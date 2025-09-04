Encryption with the Advantage TDataSet Descendant




Advantage Database Server 12  

Free Table Encryption with the Advantage TDataSet Descendant

Advantage Concepts

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Free Table Encryption with the Advantage TDataSet Descendant  Advantage Concepts |  |  | Feedback on: Advantage Database Server 12 - Free Table Encryption with the Advantage TDataSet Descendant Advantage Concepts master\_Encryption\_with\_the\_advantage\_tdataset\_descendant Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| Free Table Encryption with the Advantage TDataSet Descendant  Advantage Concepts |  |  |  |  |

TAdsTable/TAdsQuery.AdsEnableEncryption enables encryption for free connections at the record level such that each record modified by the application is also encrypted. Also, any record that has been previously encrypted can be viewed in its unencrypted form.

An entire free table can be encrypted by a call to TAdsTable.AdsEncryptTable, which will encrypt all records in the table that are not already encrypted. Any records encountered that are already encrypted will be ignored.

Encryption with TAdsQuery Free Connections

Working with encrypted data is quite different with TAdsQuery than it is with TAdsTable when using free connections. With the TAdsTable component, the TAdsTable.AdsEnableEncryption( strPassword: string ) is simply used after the table has been opened and the table is now ready for use. With TAdsQuery, because of the nature of SQL, encryption is not as straight forward.

SQL result sets come in two varieties, live cursors and static cursors. Live cursors are updateable result sets and static cursors are read-only result sets. With Advantage, simple Select statements can result in live cursors but more complex statements such as Joins result in static cursors. When a static cursor is created, it is physically a new temporary table. If the tables that were used in the SQL query to build the cursor are encrypted, the method TAdsQuery.AdsStmtSetTablePassword must be used to supply the password for each encrypted table in the query BEFORE the query is opened/executed. In this scenario, the resulting static cursor is not automatically encrypted. To force the resulting static cursor to be encrypted, the method TAdsQuery.AdsStmtEnableEncryption must also be used BEFORE the query is opened/executed.

The TAdsQuery component cannot be used to permanently encrypt or decrypt tables or records. TAdsTable methods must be used such as TAdsTable.AdsEncryptTable. Also, using TAdsQuery.AdsStmtEnableEncryption on ANY query makes its result set a static cursor. This means that even if the query is a simple select statement, using TAdsQuery.AdsStmtEnableEncryption will cause a temporary, encrypted, read-only result set to be created.

Static Cursor Example

In this example using a free connection, the entire result set is encrypted, even though the EMPLOYEE\_HISTORY table is not physically encrypted. This is because the method AdsStmtEnableEncryption was used to create an encrypted static cursor. In fact, none of the tables require encryption to use AdsStmtEnableEncryption. The result would be an encrypted result set while the source tables are not encrypted.

Note: When using [AES encryption](master_encryption.htm), it is not necessary to call AdsStmtEnableEncryption. If any table that is involved in the query is encrypted, then the static cursor will be encrypted. Also, the server handles all the encryption when using AES, so it may be necessary to use [communications encryption](master_communications_encryption.htm).

AdsQuery1.Close;

AdsQuery1.SQL.Clear;

AdsQuery1.SQL.Add( 'SELECT a.company\_name, b.lastname, c.history

 

FROM company a, employee b, employee\_history c

WHERE (a.id=b.company\_id) AND (c.employee\_id=b.id)' );

 

//Enable encryption on the static cursor result set.

AdsQuery1.AdsStmtEnableEncryption( 'result\_pwd' );

 

//Set the password for each table involved in the query.

AdsQuery1.AdsStmtSetTablePassword( 'company', 'comp\_pwd' );

AdsQuery1.AdsStmtSetTablePassword( 'employee', 'emp\_pwd' );

 

AdsQuery1.Open;

Live Cursor Example

AdsQuery1.Close;

AdsQuery1.SQL.Clear;

AdsQuery1.SQL.Add( 'INSERT INTO company ( company\_name )

VALUES(' + '''My Company Inc.''' +')' );

//Set the password for the table. Do not use AdsStmtEnableEncryption here

//or the result set will be read-only.

AdsQuery1.AdsStmtSetTablePassword( 'company', 'comp\_pwd' );

AdsQuery1.ExecSQL;

AdsQuery1.Close;

Advantage Extended Methods

The following are the Advantage Extended Methods relating to encryption:

|  |  |
| --- | --- |
| · | TAdsTable.AdsDecryptTable |

|  |  |
| --- | --- |
| · | TAdsTable/TAdsQuery.AdsDisableEncryption |

|  |  |
| --- | --- |
| · | TAdsTable/TAdsQuery.AdsEnableEncryption |

|  |  |
| --- | --- |
| · | TAdsTable.AdsEncryptTable |

|  |  |
| --- | --- |
| · | TAdsTable/TAdsQuery.AdsIsEncryptionEnabled |

|  |  |
| --- | --- |
| · | TAdsTable/TAdsQuery.AdsIsRecordEncrypted |

|  |  |
| --- | --- |
| · | TAdsTable/TAdsQuery.AdsIsTableEncrypted |

|  |  |
| --- | --- |
| · | TAdsTable.AdsVerifyPassword |