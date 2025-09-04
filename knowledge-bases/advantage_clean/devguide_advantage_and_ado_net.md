---
title: Devguide Advantage And Ado Net
slug: devguide_advantage_and_ado_net
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_advantage_and_ado_net.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: aabfa44db47b4ff29872413e53bf65a38e0f5e8b
---

# Devguide Advantage And Ado Net

Advantage and ADO.NET

     Advantage and ADO.NET

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Advantage and ADO.NET  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

ADO.NET is the common name for the classes and interfaces of the System.Data second-level namespace of the FCL. Conceptually, ADO.NET can be divided into two distinct parts: the data access layer and the data storage system.

The classes associated with the data storage system are stand-alone classes that you can employ in any ADO.NET application. These classes include DataColumn, DataRelation, DataRow, DataSet, DataTable, and DataView. Of these, the most central class is DataSet.

Unlike the storage mechanism, which is defined around classes, the data access layer is formally defined using interfaces (abstract application programming interface definitions), and in ADO.NET 2.0, abstract base classes. Concrete classesthat is, classes that can be instantiatedimplement these interfaces. It is these concrete implementations that you use to access your data. Such classes are referred to generically as .NET data providers.

There are five .NET data providers native to version 1.1 and version 2.0 of ADO.NET, which is also to say that Microsoft provides them. These are associated with the System.Data.SqlClient, System.Data.OleDb, System.Data.Odbc, System.Data.SqlServerCE, and System.Data.OracleClient third-level namespaces.

As is the case with ADO and OLE DB providers, database vendors are permitted and encouraged to create their own data access classes that implement these same interfaces (and in ADO.NET 2.0, extend the abstract base classes). Advantage calls their implementation the Advantage .NET Data Provider, and it can be found in the Advantage.Data.Provider namespace.

The primary responsibility of the Advantage .NET Data Provider classes is the same as that of the native implementations--supply data to the data storage system, and in particular, provide access to data through SQL queries.

The second, and obviously crucial, role of .NET data providers is to permit direct manipulation of data through SQL. This, too, is deftly handled by the Advantage .NET Data Provider.

As is the case with all data access mechanisms described in this part of this book, the following discussion of Advantage programming with ADO.NET touches on just a few of the available techniques, particularly those that apply to Advantage. Unlike some of the other data access mechanisms covered in this part of this book, the native .NET classes provide a significant amount of standard database functionality, such as filtering, sorting, and seeking. Consequently, these topics are not Advantage specific, and are not covered in this chapter. For a comprehensive discussion of ADO.NET programming, you may want to pick up a book on the subject.

Another important point about the examples provided in this chapter is that they are provided through a Windows form application. This might seem a bit odd, considering that the vast majority of applications written using the .NET framework are Web forms (or Web service) applications, those used to create applications for the World Wide Web.

There is a good reason for the use of a Windows form application in these examples. Windows forms applications are more demanding, database-wise, than ASP.NET applications, such as Web forms applications. In most Web forms applications, a DataReader is used to read data, which is then bound to one or more controls on a Web form. In most cases, DataSets and DataTables are not used. These are, however, essential parts of ADO.NET.

There is also a second reason. Creating an ASP.NET Web forms application is more involved than creating a Windows forms application. You need a Web server and you need to configure it to run .NET.

In the end, we opted for focusing on how to access Advantage using .NET, rather than complicate the process with ASP.NET-related issues. Consequently, the Windows forms application described here is designed to be similar to the Delphi, Java, and Visual Basic applications described in the preceding chapters.
