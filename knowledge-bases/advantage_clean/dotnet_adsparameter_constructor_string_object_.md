---
title: Dotnet Adsparameter Constructor String Object
slug: dotnet_adsparameter_constructor_string_object_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_constructor_string_object_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 454147aad6ad58846234a6b805dfe4008b8b6c8b
---

# Dotnet Adsparameter Constructor String Object

AdsParameter Constructor ( string, object )

AdsParameter Constructor ( string, object )

Advantage .NET Data Provider

| AdsParameter Constructor ( string, object )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name and value.

public AdsParameter

(

string parameterName, // (I) parameter name

object value // (I) parameter value

);

Remarks

The DbType will be inferred from the value of the given object. It can be changed if desired after creating the AdsParameter object via the [AdsParameter.DbType](dotnet_adsparameter_dbtype.md) property.

Example

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

AdsParameter param;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand( "update departments set [Department Name] = :name " +

"where [department code] = :code",

conn );

 

// create the two parameters.

param = new AdsParameter( "name", "Research & Development" );

cmd.Parameters.Add( param );

param = new AdsParameter( "code", 104 );

cmd.Parameters.Add( param );

 

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );
