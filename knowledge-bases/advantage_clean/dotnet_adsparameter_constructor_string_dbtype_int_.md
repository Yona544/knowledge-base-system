---
title: Dotnet Adsparameter Constructor String Dbtype Int
slug: dotnet_adsparameter_constructor_string_dbtype_int_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_constructor_string_dbtype_int_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 8379188203808158a9d78bc0b2b7fa5e008b5da7
---

# Dotnet Adsparameter Constructor String Dbtype Int

AdsParameter Constructor ( string, DbType, int )

AdsParameter Constructor ( string, DbType, int )

Advantage .NET Data Provider

| AdsParameter Constructor ( string, DbType, int )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given name, type, and parameter width.

public AdsParameter

(

string parameterName, // (I) parameter name

DbType type, // (I) parameter type

int iSize // (I) parameter width

);

Remarks

The Size is inferred from the value of the DbType parameter and the value if it is not explicity set in the size parameter.

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

param = new AdsParameter( "name", DbType.String, 15 );

param.Value = "R & D";

cmd.Parameters.Add( param );

param = new AdsParameter( "code", DbType.Int32, 4 );

param.Value = 104;

cmd.Parameters.Add( param );

 

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );
