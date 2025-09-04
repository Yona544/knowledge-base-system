AdsStmtSetTablePassword




Advantage Database Server 12  

TAdsQuery.AdsStmtSetTablePassword

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.AdsStmtSetTablePassword  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.AdsStmtSetTablePassword Advantage TDataSet Descendant ade\_Adsstmtsettablepassword Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.AdsStmtSetTablePassword  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

Sets a base table's encryption password that will be used when the SQL statement is executed.

Syntax

procedure AdsStmtSetTablePassword( strTableName : string;

strPassword : string );

Parameters

|  |  |
| --- | --- |
| strTableName | Name of the base table. |
| strPassword | Case-sensitive text encryption password. |

Description

If there are encrypted records in the base table(s) in an SQL statement, the encryption password(s) for the records must be provided before executing the query. Otherwise, the records will not be correctly considered for the result set. See [AdsStmtEnableEncryption](ade_adsstmtenableencryption.htm) for additional information about using encryption with Advantage.

If the statement executed is an update statement, the rows modified will be encrypted with the specified encryption password.

The encryption password for the specified table will be used for all subsequent executions of the statement handle. If the base table has no encryption information before the statement is executed, the specified encryption password will be stored in the table header when the statement is executed.

Note If the resulting cursor is read-only, all rows will be decrypted by the server even though the data may be encrypted in the base table. To generate an encrypted read-only cursor, see [AdsStmtEnableEncryption](ade_adsstmtenableencryption.htm).

Example

AdsQuery1.Close;

AdsQuery1.SQL.Clear;

AdsQuery1.SQL.Add('Select \* from Demo10 where LastName = ''Coles''');

{ Demo10 has records encrypted with password 'Secret' }

AdsQuery1.AdsStmtSetTablePassword( 'Demo10', 'Secret' );

AdsQuery1.ExecSQL;

See Also

[AdsStmtEnableEncryption](ade_adsstmtenableencryption.htm)

[AdsStmtDisableEncryption](ade_adsstmtdisableencryption.htm)

[AdsStmtClearTablePasswords](ade_adsstmtcleartablepasswords.htm)