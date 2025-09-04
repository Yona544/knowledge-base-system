---
title: Dotnet Adsparameter Constructor Int Object
slug: dotnet_adsparameter_constructor_int_object_
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsparameter_constructor_int_object_.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 5aefb5cbc7527845ff529185f7c7f832ad6ccead
---

# Dotnet Adsparameter Constructor Int Object

AdsParameter Constructor ( int, object )

AdsParameter Constructor ( int, object )

Advantage .NET Data Provider

| AdsParameter Constructor ( int, object )  Advantage .NET Data Provider |  |  |  |  |

Initializes a new instance of the AdsParameter class with the given one-based index and value.

public AdsParameter

(

int iIndex, // (I) parameter index (for unnamed params)

object value // (I) parameter value

);

Remarks

This constructor can be used for statements with unnamed parameters. The parameter number is one-based. The DbType will be inferred from the value of the given object. It can be changed if desired after creating the AdsParameter object via the [AdsParameter.DbType](dotnet_adsparameter_dbtype.md) property.

Example

AdsConnection conn = new AdsConnection( "data source = c:\\data;" );

AdsCommand cmd;

AdsParameter param;

 

// open the connection

conn.Open();

// create a new command object

cmd = new AdsCommand( "update departments set [Department Name] = ? " +

"where [department code] = ?",

conn );

 

// create the two parameters.

param = new AdsParameter( 1, "Research & Development" );

cmd.Parameters.Add( param );

param = new AdsParameter( 2, 104 );

cmd.Parameters.Add( param );

 

// execute the query

Console.WriteLine( "Records affected: " + cmd.ExecuteNonQuery() );
