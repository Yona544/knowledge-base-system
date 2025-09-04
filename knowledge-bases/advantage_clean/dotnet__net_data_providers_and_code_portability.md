---
title: Dotnet Net Data Providers And Code Portability
slug: dotnet__net_data_providers_and_code_portability
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: dotnet__net_data_providers_and_code_portability.htm
source: Advantage CHM
tags:
  - dotnet
checksum: 1d33cfcabf8fdba7f30f3616471ba06839603fa5
---

# Dotnet Net Data Providers And Code Portability

.NET Data Providers and Code Portability

.NET Data Providers and Code Portability

Advantage .NET Data Provider

| .NET Data Providers and Code Portability  Advantage .NET Data Provider |  |  |  |  |

.NET data providers implement a set of standard interfaces and expose those interfaces through a set of objects with names specific to each implementation. This is somewhat different from other data interfaces such as ODBC and OLE DB. In those data access methodologies, the interface presented to the developer is largely a rigorously defined set of APIs or COM interfaces and are usually used with some layer of indirection between a developers application and the actual driver/provider. For example, with ODBC, an application connects to a specific driver by requesting it via a registered data source.

With .NET data providers, though, it is more common for a developers application to directly access the provider objects. One of the benefits of this is that it eliminates extra layers of indirection between the application and the provider. It also allows an application to easily access provider-specific functionality because the application can simply call any methods that are publicly defined on the objects even if those methods are not part of the specification. For example, the [AdsCommand.DeriveParameters](dotnet_adscommand_deriveparameters.md) method is not defined in the .NET data provider specification, but an application can call it directly.

The drawback to using .NET data provider objects directly by name is that it is more difficult to write an application that can use multiple providers with a common set of code. One solution to this is to program directly to the interfaces themselves.

The following is a simple example of this idea. It has only one section that is specific to a given client. The connection object is assigned as either an Advantage .NET Data Provider AdsConnection object or a SQL Server .NET Data Provider SqlConnection object.

// generic object definitions

IDbConnection Conn = null;

IDataReader Reader = null;

IDbCommand Cmd = null;

 

try

{

// get the specific connection object

if ( bUseAdvantage )

Conn = new AdsConnection( @"data source = c:\data" );

else

Conn = new SqlConnection( "user id=sa;password=" +

";initial catalog=northwind;data source=server" );

 

Conn.Open();

 

// create a command object

Cmd = Conn.CreateCommand();

Cmd.CommandText = "Select \* from customers";

 

// execute the statement

Reader = Cmd.ExecuteReader();

 

// read some results

while ( Reader.Read() )

if ( !Reader.IsDBNull( 1 ))

Console.WriteLine( Reader.GetString(1) + "." );

 

Conn.Close();

}

catch ( Exception e )

{

Console.WriteLine( e.Message );

}

.NET Framework v2.x

In version 2.x of the .NET Framework, the specification for ADO.NET has improved the ability to write portable code. Each of the .NET data provider object types now descend from abstract base classes. For example, AdsConnection is a subclass of the .NET Framework class DbConnection. The following table shows the Advantage classes and the base class that they descend from in the 2.x .NET Framework.

| Advantage Class | Base Class |
| AdsFactory | DbProviderFactory |
| AdsConnection | DbConnection |
| AdsCommand | DbCommand |
| AdsDataReader | DbDataReader |
| AdsTransaction | DbTransaction |
| AdsParameter | DbParameter |
| AdsParameterCollection | DbParameterCollection |
| AdsDataAdapter | DbDataAdapter |
| AdsCommandBuilder | DbCommandBuilder |
| AdsConnectionStringBuilder | DbConnectionStringBuilder |

If you use methods and properties that are defined only in the base classes, then it is possible to write more portable code. When using the interfaces available in the 1.0 .NET Framework, it is sometimes necessary to refer to a specific object type (e.g., AdsConnection). When using the new object types in conjunction with the DbFactories class, it is possible to write code that does not have any references to a specific providers classes.

The following code example shows a simple example using these classes.

try

{

 

// Extract connection information from app.config file

string strConn = ConfigurationManager.

ConnectionStrings["MyConnectionString"].ConnectionString;

string strProvider = ConfigurationManager.

ConnectionStrings["MyConnectionString"].ProviderName;

 

// Get the DbFactory object for the provider and create a connection from it

DbProviderFactory dbFact = DbProviderFactories.GetFactory( strProvider );

DbConnection dbConn = dbFact.CreateConnection();

dbConn.ConnectionString = strConn;

dbConn.Open();

 

// Set up a data adapter and use a command builder to

// create the SQL update statements.

DbDataAdapter dbAdapter = dbFact.CreateDataAdapter();

dbAdapter.SelectCommand = dbConn.CreateCommand();

DbCommandBuilder dbCmdBuilder = dbFact.CreateCommandBuilder();

dbAdapter.SelectCommand.CommandText = "select \* from items";

dbCmdBuilder.DataAdapter = dbAdapter;

 

// Fill a data set, update it, and send the update back to the database

DataSet ds = new DataSet();

dbAdapter.Fill( ds, "items" );

ds.Tables["items"].Rows[0]["quantity"] = 3;

dbAdapter.Update( ds, "items" );

 

dbConn.Close();

}

catch ( Exception e )

{

Console.WriteLine( e.ToString() );

}
