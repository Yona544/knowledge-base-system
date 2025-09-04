---
title: Dotnet Adscommand Prepare
slug: dotnet_adscommand_prepare
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_prepare.htm
source: Advantage CHM
tags:
  - dotnet
checksum: e37879956bf34439df3f99e7a3f68281f02bffe3
---

# Dotnet Adscommand Prepare

AdsCommand.Prepare

AdsCommand.Prepare

Advantage .NET Data Provider

| AdsCommand.Prepare  Advantage .NET Data Provider |  |  |  |  |

Performs the initial preparation of the statement specified in [AdsCommand.CommandText](dotnet_adscommand_commandtext.md).

public void Prepare();

Remarks

This method prepares the statement for execution on the server. It is generally not necessary to call this method because it is called automatically by Advantage .NET Data Provider when methods such as [AdsCommand.ExecuteReader](dotnet_adscommand_executereader.md) and [AdsCommand.ExecuteNonQuery](dotnet_adscommand_executenonquery.md) are called. There is no efficiency gain by calling this method first.

If you do call this method and [AdsCommand.CommandType](dotnet_adscommand_commandtype.md) is set to CommandType.StoredProcedure, you must have set up the parameters for the stored procedure first.

See Also

[ExecuteReader](dotnet_adscommand_executereader.md)

[ExecuteNonQuery](dotnet_adscommand_executenonquery.md)

[ExecuteScalar](dotnet_adscommand_executescalar.md)

[DeriveParameters](dotnet_adscommand_deriveparameters.md)
