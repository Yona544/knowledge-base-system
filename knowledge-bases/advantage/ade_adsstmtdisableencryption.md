AdsStmtDisableEncryption




Advantage Database Server 12  

TAdsQuery.AdsStmtDisableEncryption

Advantage TDataSet Descendant

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| TAdsQuery.AdsStmtDisableEncryption  Advantage TDataSet Descendant |  |  | Feedback on: Advantage Database Server 12 - TAdsQuery.AdsStmtDisableEncryption Advantage TDataSet Descendant ade\_Adsstmtdisableencryption Advantage Web Development > Advantage Delphi OData Client > Delphi OData Components > TODataSet / Dear Support Staff, |  |
| TAdsQuery.AdsStmtDisableEncryption  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.htm)

Disables the encryption of a cursor generated after executing the SQL statement.

Syntax

procedure AdsStmtDisableEncryption;

Description

This function reverses the effect of [AdsStmtEnableEncryption](ade_adsstmtenableencryption.htm).

Example

AdsQuery1.Close;

AdsQuery1.SQL.Clear;

AdsQuery1.SQL.Add('Select \* from Demo10 where LastName = ''Coles''');

AdsQuery1.AdsStmtEnableEncryption( 'Secret' );

AdsQuery1.ExecSQL;

AdsQuery1.AdsStmtDisableEncryption;

AdsQuery1.Open; // creates an updatable cursor

See Also

[AdsStmtEnableEncryption](ade_adsstmtenableencryption.htm)