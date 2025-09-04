AdsStmtSetTablePassword




Advantage Database Server 12  

AdsStmtSetTablePassword

Advantage Client Engine

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| AdsStmtSetTablePassword  Advantage Client Engine |  |  | Feedback on: Advantage Database Server 12 - AdsStmtSetTablePassword Advantage Client Engine ace\_Adsstmtsettablepassword Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| AdsStmtSetTablePassword  Advantage Client Engine |  |  |  |  |

Sets a base table's encryption password that will be used when the SQL statement is executed.

Syntax

|  |  |
| --- | --- |
| UNSIGNED32 | AdsStmtSetTablePassword( ADSHANDLE hStatement,  UNSIGNED8 \*pucTableName,  UNSIGNED8 \*pucPassword ); |

Parameters

|  |  |
| --- | --- |
| hStatement(I) | Handle of an SQL statement created by a call to AdsCreateSQLStatement. |
| pucTableName(I) | Name of the base table. |
| pucPassword(I) | Case-sensitive text encryption password. |

Remarks

If there are encrypted records in the base table(s) in an SQL statement, the encryption password(s) for the records must be provided before executing the query. Otherwise, the records will not be correctly considered for the result set. See [AdsEnableEncryption](ace_adsenableencryption.htm) for additional information about encryption with Advantage.

If the statement executed is an update statement, the rows modified will be encrypted with the specified encryption password.

The encryption password for the specified table will be used for all subsequent query execution on the statement handle. If the base table has no encryption information before the statement is executed, the specified encryption password will be stored in the table header when the statement is executed.

If the statement handle was created on a [database connection](javascript:hhpopuplink.TextPopup(popid_465551922,FontFace,-1,-1,-1,-1)), setting the encryption password for [database tables](javascript:hhpopuplink.TextPopup(popid_2121602366X,FontFace,-1,-1,-1,-1)) is ignored. The database tables encryption password is stored in the database and automatically available to the authenticated users.

Note If the resulting cursor is read-only, all rows will be decrypted by the server even though the data may be encrypted in the base table. To generate an encrypted read-only cursor, use [AdsStmtEnableEncryption](ace_adsstmtenableencryption.htm).

Example

[Click Here](ace_more_examples.htm#adsstmtsettablepassword_example)

See Also

[AdsStmtEnableEncryption](ace_adsstmtenableencryption.htm)

[AdsStmtDisableEncryption](ace_adsstmtdisableencryption.htm)

[AdsStmtClearTablePasswords](ace_adsstmtcleartablepasswords.htm)