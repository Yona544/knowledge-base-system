AdsStmtClearTablePasswords




Advantage Database Server 12  

TAdsQuery.AdsStmtClearTablePasswords

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.AdsStmtClearTablePasswords  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.AdsStmtClearTablePasswords Advantage TDataSet Descendant ade\_Adsstmtcleartablepasswords Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.AdsStmtClearTablePasswords  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

Clears all table encryption passwords associated with the component.

Syntax

procedure AdsStmtClearTablePasswords;

Description

This method removes all table encryption passwords set using [AdsStmtSetTablePassword](ade_adsstmtsettablepassword.htm).

Example

AdsQuery1.Close;

AdsQuery1.SQL.Clear;

AdsQuery1.SQL.Add('Select \* from Demo10 where LastName = ''Coles''');

{ Demo10 has records encrypted with password 'Secret' }

AdsQuery1.AdsStmtSetTablePassword( 'Demo10', 'SECRET' );

AdsQuery1.ExecSQL; // This will fail because password is case sensitive

AdsQuery1.AdsStmtClearTablePasswords;

AdsQuery1.AdsStmtSetTablePassword( 'Demo10', 'Secret' );

AdsQuery1.ExecSQL;

See Also

[AdsStmtEnableEncryption](ade_adsstmtenableencryption.htm)

[AdsStmtDisableEncryption](ade_adsstmtdisableencryption.htm)

[AdsStmtSetTablePassword](ade_adsstmtsettablepassword.htm)