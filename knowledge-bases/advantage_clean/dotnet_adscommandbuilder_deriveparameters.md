---
title: Dotnet Adscommandbuilder Deriveparameters
slug: dotnet_adscommandbuilder_deriveparameters
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommandbuilder_deriveparameters.htm
source: Advantage CHM
tags:
  - dotnet
checksum: e692bd6440dc18d97155741d3f0301b79c375a8a
---

# Dotnet Adscommandbuilder Deriveparameters

AdsCommandBuilder.DeriveParameters

AdsCommandBuilder.DeriveParameters

Advantage .NET Data Provider

| AdsCommandBuilder.DeriveParameters  Advantage .NET Data Provider |  |  |  |  |

Populates the [AdsCommand.Parameters](dotnet_adscommand_parameters.md) collection with the parameter information for the stored procedure specified in the SelectCommand CommandText property.

public static void DeriveParameters( AdsCommand command );

Remarks

This method provides a simple method for populating the Parameters collection of the given command prior to executing a stored procedure. If [AdsCommand.CommandType](dotnet_adscommand_commandtype.md) is not set to StoredProcedure, this method throws an ArgumentException.

This call requires a round trip to the server to retrieve the parameter information for the named stored procedure. Therefore it is more efficient to set the parameter information explicitly.

Calling this method is equivalent to calling the [AdsCommand.DeriveParameters](dotnet_adscommand_deriveparameters.md) method directly.

See Also

[AdsCommand.Parameters](dotnet_adscommand_parameters.md)

[AdsCommand.DeriveParameters](dotnet_adscommand_deriveparameters.md)
