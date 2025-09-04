---
title: Dotnet Adsdataadapter Selectcommand
slug: dotnet_adsdataadapter_selectcommand
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_selectcommand.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 7e82481c9be1b60c692e025925ee219fdf3e5ec6
---

# Dotnet Adsdataadapter Selectcommand

AdsDataAdapter.SelectCommand

AdsDataAdapter.SelectCommand

Advantage .NET Data Provider

| AdsDataAdapter.SelectCommand  Advantage .NET Data Provider |  |  |  |  |

Gets or sets an SQL statement, stored procedure, or table name used to select records in the data source.

public AdsCommand SelectCommand { get; set; }

Remarks

This command is used by the [AdsDataAdapter.Fill](dotnet_adsdataadapter_fill.md) call to select the data that is put into the DataSet.

When SelectCommand is assigned to a previously created [AdsCommand](dotnet_adscommand.md), the AdsCommand is not cloned. The SelectCommand maintains a reference to the previously created AdsCommand object.

If the SelectCommand does not return any rows, no tables are added to the DataSet, and no exception is raised.

The SelectCommand must be set before and [AdsCommandBuilder](dotnet_adscommandbuilder.md) can be used with this AdsDataAdapter.

See Also

[AdsCommandBuilder](dotnet_adscommandbuilder.md)
