---
title: Dotnet Adscommand Deriveparameters
slug: dotnet_adscommand_deriveparameters
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adscommand_deriveparameters.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 333142269388fbadd0b310ad8238d9053ab1f792
---

# Dotnet Adscommand Deriveparameters

AdsCommand.DeriveParameters

AdsCommand.DeriveParameters

Advantage .NET Data Provider

| AdsCommand.DeriveParameters  Advantage .NET Data Provider |  |  |  |  |

Populates the [AdsCommand.Parameters](dotnet_adscommand_parameters.md) collection with the parameter information for the stored procedure specified in [AdsCommand.CommandText](dotnet_adscommand_commandtext.md).

public void DeriveParameters();

Remarks

DeriveParameters provides a simple method for populating the Parameters collection prior to executing a stored procedure. If [AdsCommand.CommandType](dotnet_adscommand_commandtype.md) is not set to StoredProcedure, this method throws an ArgumentException.

The DeriveParameters method creates one AdsParameter object for each parameter defined for the stored procedure in the Advantage Data Dictionary. It fills in the [AdsParameter.ParameterName](dotnet_adsparameter_parametername.md), [AdsParameter.DbType](dotnet_adsparameter_dbtype.md), and [AdsParameter.Direction](dotnet_adsparameter_direction.md) properties. Note that if you are using a stored procedure to perform the updates with an AdsDataAdapter, you will probably need to set the AdsParameter.SourceColumn property to match the DataSet column names after calling DeriveParameters.

This call requires a round trip to the server to retrieve the parameter information for the named stored procedure. Therefore, it is more efficient to set the parameter information explicitly.

Example

conn = new AdsConnection( "data source=c:\\data\\test.add;" +

"user id=test;" );

 

conn.Open();

 

AdsCommand cmd = conn.CreateCommand();

 

// assign the procedure name

cmd.CommandText = "testproc";

// set command type to stored procedure

cmd.CommandType = CommandType.StoredProcedure;

// load the parameter collection from the data dictionary info

cmd.DeriveParameters();

// assign in put parameters

cmd.Parameters["inparam1"].Value = 234;

cmd.Parameters["inparam2"].Value = "xyz";

 

// execute the stored procedure

cmd.ExecuteNonQuery();

// print an output parameter

Console.WriteLine( cmd.Parameters["outparam"].Value );

See Also

[Parameters](dotnet_adscommand_parameters.md)

[AdsCommandBuilder.DeriveParameters](dotnet_adscommandbuilder_deriveparameters.md)
