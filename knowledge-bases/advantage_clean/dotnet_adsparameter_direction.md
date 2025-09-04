---
title: Dotnet Adsparameter Direction
slug: dotnet_adsparameter_direction
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_direction.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 2ab0b174572c799f241f6d49c7ab43f8a982cef7
---

# Dotnet Adsparameter Direction

AdsParameter.Direction

AdsParameter.Direction

Advantage .NET Data Provider

| AdsParameter.Direction  Advantage .NET Data Provider |  |  |  |  |

Gets or sets a value indicating whether the parameter is input or output.

public ParameterDirection Direction {get; set;}

Remarks

The Advantage .NET Data Provider currently only supports ParameterDirection.Input and ParameterDirection.Output. Input parameters can be used with SQL statements and stored procedures for sending data to the server. Output parameters can be used with stored procedures. Any AdsParameters with the Direction set to ParameterDirection.Output with names that match the data dictionary definition for stored procedure output parameters will be populated automatically when the stored procedure is executed.

See Also

[AdsCommand.DeriveParameters](dotnet_adscommand_deriveparameters.md)
