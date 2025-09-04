---
title: Ade Adsstmtdisableencryption
slug: ade_adsstmtdisableencryption
product: Advantage Database Server
component: Advantage TDataSet Descendant
version: "12"
category: API
original_path_html: ade_adsstmtdisableencryption.htm
source: Advantage CHM
tags:
  - ade
  - advantage-tdataset-descendant
checksum: 3d3573bb08d4e17e2c2295de6fe46700ea391e69
---

# Ade Adsstmtdisableencryption

AdsStmtDisableEncryption

TAdsQuery.AdsStmtDisableEncryption

Advantage TDataSet Descendant

| TAdsQuery.AdsStmtDisableEncryption  Advantage TDataSet Descendant |  |  |  |  |

[TAdsQuery](ade_tadsquery.md)

Disables the encryption of a cursor generated after executing the SQL statement.

Syntax

procedure AdsStmtDisableEncryption;

Description

This function reverses the effect of [AdsStmtEnableEncryption](ade_adsstmtenableencryption.md).

Example

AdsQuery1.Close;

AdsQuery1.SQL.Clear;

AdsQuery1.SQL.Add('Select \* from Demo10 where LastName = ''Coles''');

AdsQuery1.AdsStmtEnableEncryption( 'Secret' );

AdsQuery1.ExecSQL;

AdsQuery1.AdsStmtDisableEncryption;

AdsQuery1.Open; // creates an updatable cursor

See Also

[AdsStmtEnableEncryption](ade_adsstmtenableencryption.md)
