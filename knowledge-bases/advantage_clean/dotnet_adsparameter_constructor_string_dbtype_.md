---
title: Dotnet Adsparameter Constructor String Dbtype
slug: dotnet_adsparameter_constructor_string_dbtype_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_constructor_string_dbtype_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 8467abda1685e8c896d686296b4fea2ca9ce3f1a
---

# Dotnet Adsparameter Constructor String Dbtype

AdsParameter Constructor ( string, DbType )

AdsParameter Constructor ( string, DbType )

Advantage .NET Data Provider

| AdsParameter Constructor ( string, DbType )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name and type.

public AdsParameter

(

string parameterName, // (I) parameter name

DbType type // (I) parameter type

);

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

param = new AdsParameter( "budget", DbType.Currency );

param.Value = (Decimal)8400000;

cmd.Parameters.Add( param );

param = new AdsParameter( "code", DbType.Int32 );

param.Value = 104;

cmd.Parameters.Add( param );

 

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );
