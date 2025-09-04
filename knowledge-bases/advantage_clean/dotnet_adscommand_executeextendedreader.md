---
title: Dotnet Adscommand Executeextendedreader
slug: dotnet_adscommand_executeextendedreader
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_executeextendedreader.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 597d1e1ff258adc5d25609a19604b2a2503e0f64
---

# Dotnet Adscommand Executeextendedreader

AdsCommand.ExecuteExtendedReader

AdsCommand.ExecuteExtendedReader

Advantage .NET Data Provider

| AdsCommand.ExecuteExtendedReader  Advantage .NET Data Provider |  |  |  |  |

Executes the AdsCommand.CommandText and returns an AdsExtendedReader with the result set.

public AdsExtendedReader ExecuteExtendedReader();

Remarks

ExecuteExtendedReader executes the SQL statement or stored procedure or opens the table that is specified in the AdsCommand.CommandText property.

[AdsExtendedReader](dotnet_adsextendedreader.md) is derived from AdsDataReader and offers an extended feature set that includes advanced table navigation, indexed searches, scopes, filters, locks and direct data manipulation. Use [ExecuteExtendedReader](dotnet_adscommand_executeextendedreader.md) to obtain an AdsExtendedReader object. Use [ExecuteReader](dotnet_adscommand_executereader.md) to obtain a standard AdsDataReader object.

Example

See [ExecuteReader](dotnet_adscommand_executereader.md)

See Also

[ExecuteReader](dotnet_adscommand_executereader.md)

[ExecuteReader( CommandBehavior )](dotnet_adscommand_executereader_commandbehavior_.md)

ExecuteExtendedReader( CommandBehavior )

[CommandText](dotnet_adscommand_commandtext.md)

[AdsDataReader](dotnet_adsdatareader.md)

[AdsExtendedReader](dotnet_adsextendedreader.md)
