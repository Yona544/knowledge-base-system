---
title: Dotnet Adsdataadapter Constructor String Adsconnection
slug: dotnet_adsdataadapter_constructor_string_adsconnection_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_constructor_string_adsconnection_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: ed9e7b8981bf7b1d53af29e419cfc57ecc783338
---

# Dotnet Adsdataadapter Constructor String Adsconnection

AdsDataAdapter Constructor( String, AdsConnection )

AdsDataAdapter Constructor( String, AdsConnection )

Advantage .NET Data Provider

| AdsDataAdapter Constructor( String, AdsConnection )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsDataAdapter object with a given SQL statement and a connection to associate with the command.

public AdsDataAdapter( string selectCommand,

AdsConnection connection );

Remarks

The selectCommand string is expected to be a valid SQL SELECT statement or stored procedure to be used as the [CommandText](dotnet_adscommand_commandtext.md) of the [SelectCommand](dotnet_adsdataadapter_selectcommand.md) property of the AdsDataAdapter.
