---
title: Dotnet Adsdataadapter Constructor String String
slug: dotnet_adsdataadapter_constructor_string_string_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsdataadapter_constructor_string_string_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 0f529ec3e2cf9be7a088741de78a744a784de568
---

# Dotnet Adsdataadapter Constructor String String

AdsDataAdapter Constructor( String, String )

AdsDataAdapter Constructor( String, String )

Advantage .NET Data Provider

| AdsDataAdapter Constructor( String, String )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of an AdsDataAdapter object with a given SQL statement and a connection string to associate with the command.

public AdsDataAdapter( string selectCommand,

string connection );

Remarks

The selectCommand string is expected to be a valid SQL SELECT statement or stored procedure to be used as the [CommandText](dotnet_adscommand_commandtext.md) of the [SelectCommand](dotnet_adsdataadapter_selectcommand.md) property of the AdsDataAdapter. A new [AdsConnection](dotnet_adsconnection.md) object will be created and opened using the given connection string.
