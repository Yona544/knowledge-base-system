---
title: Dotnet Adscommand Verifysql
slug: dotnet_adscommand_verifysql
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_verifysql.htm
source: Advantage CHM
tags:
  - dotnet
checksum: d23fa6f16db8ba24f924f8dbdcc68e35dedfdc68
---

# Dotnet Adscommand Verifysql

AdsCommand.VerifySQL

AdsCommand.VerifySQL

Advantage .NET Data Provider

| AdsCommand.VerifySQL  Advantage .NET Data Provider |  |  |  |  |

Verifies the given SQL statement is valid.

public void VerifySQL( string strSQL );

Remarks

This method verifies the given statement (strSQL) is a valid SQL statement. The statement is sent to the server where it is parsed but not executed. An exception is raised if the statement is not valid.

See Also

[ExecuteReader](dotnet_adscommand_executereader.md)

[ExecuteNonQuery](dotnet_adscommand_executenonquery.md)

[ExecuteScalar](dotnet_adscommand_executescalar.md)
