---
title: Dotnet Adsconnectionstringbuilder Class
slug: dotnet_adsconnectionstringbuilder_class
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet_adsconnectionstringbuilder_class.htm
source: Advantage CHM
tags:
  - dotnet
checksum: e047f1a3c666e4c454f1b4a1a90716ae2ac64ca5
---

# Dotnet Adsconnectionstringbuilder Class

AdsConnectionStringBuilder Class

AdsConnectionStringBuilder Class

Advantage .NET Data Provider

| AdsConnectionStringBuilder Class  Advantage .NET Data Provider |  |  |  |  |

Full name: Advantage.Data.Provider.AdsConnectionStringBuilder

Implements: System.Data.Common.DbConnectionStringBuilder

[Constructors](dotnet_adsconnectionstringbuilder_constructors.md)

[Properties](dotnet_adsconnectionstringbuilder_properties.md)

[Methods](dotnet_adsconnectionstringbuilder_methods.md)

Note This class is new in the .NET Framework version 2.0.

The AdsConnectionStringBuilder class provides a simple way to create and manage the contents of connection strings used by the AdsConnection class. It provides a way to assign the properties using properties in the class from which it will build a syntactically correct connection string with the proper key/value pairs. In addition, an existing connection string can be assigned to it, and then the values for the keys can be retrieved via the properties.

Example

try

{

// Create a new connection string builder

AdsConnectionStringBuilder builder =

new AdsConnectionStringBuilder();

 

// set some properties in it

builder.DataSource = @"c:\data";

builder.ServerType = "local";

 

Console.WriteLine( builder.ConnectionString );

 

// Assign the connection string and print the properties

builder.ConnectionString =

@"data source=c:\data\mydata.add;user id=theuser;" +

"password=somepass;servertype=remote";

Console.WriteLine( "Data source = {0}", builder.DataSource );

Console.WriteLine( "ServerType = {0}", builder.ServerType );

Console.WriteLine( "User = {0}", builder.UserID );

Console.WriteLine( "Password = {0}", builder.Password );

 

}

catch ( Exception e )

{

Console.WriteLine( e.ToString() );

}
