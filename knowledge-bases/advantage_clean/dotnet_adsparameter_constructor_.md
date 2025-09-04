---
title: Dotnet Adsparameter Constructor
slug: dotnet_adsparameter_constructor_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_constructor_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 511a62cf35b5f055fd381f13986d7873995702f3
---

# Dotnet Adsparameter Constructor

AdsParameter Constructor ()

AdsParameter Constructor ()

Advantage .NET Data Provider

| AdsParameter Constructor ()  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with all default values for the properties.

public AdsParameter();

Remarks

Using this constructor is equivalent to calling [AdsCommand.CreateParameter](dotnet_adscommand_createparameter.md).

Example

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

AdsParameter param;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand( "update departments set budget = :budget " +

"where [department code] = :code",

conn );

 

// create the two parameters.

param = new AdsParameter();

param.Value = 400000;

param.ParameterName = "budget";

cmd.Parameters.Add( param );

param = new AdsParameter();

param.Value = 110;

param.ParameterName = "code";

cmd.Parameters.Add( param );

 

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );

See Also

[AdsCommand.CreateParameter](dotnet_adscommand_createparameter.md)
