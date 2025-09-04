---
title: Ade Adsstmtcleartablepasswords
slug: ade_adsstmtcleartablepasswords
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsstmtcleartablepasswords.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: fd68975df926b05135f36330dac3064ca59e5a7e
---

# Ade Adsstmtcleartablepasswords

AdsStmtClearTablePasswords

TAdsQuery.AdsStmtClearTablePasswords

Advantage TDataSet Descendant

| TAdsQuery.AdsStmtClearTablePasswords  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Clears all table encryption passwords associated with the component.

Syntax

procedure AdsStmtClearTablePasswords;

Description

This method removes all table encryption passwords set using [AdsStmtSetTablePassword](ade_adsstmtsettablepassword.md).

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

[AdsStmtEnableEncryption](ade_adsstmtenableencryption.md)

[AdsStmtDisableEncryption](ade_adsstmtdisableencryption.md)

[AdsStmtSetTablePassword](ade_adsstmtsettablepassword.md)
