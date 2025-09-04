---
title: Devguide Accessing Advantage Using The Advantage Odbc Driver
slug: devguide_accessing_advantage_using_the_advantage_odbc_driver
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_accessing_advantage_using_the_advantage_odbc_driver.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: be980fea3d88d9bcee8d8eb0024d58b98a97f3b7
---

# Devguide Accessing Advantage Using The Advantage Odbc Driver

Accessing Advantage Using the Advantage ODBC Driver

     Accessing Advantage Using the Advantage ODBC Driver

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Accessing Advantage Using the Advantage ODBC Driver  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

ODBC (open database connectivity) is based on the Open SQL CLI (call-level interface), a SQL-based standard for accessing data. Advantage supplies ODBC drivers for both Windows and Linux.

ODBC is an API (application programming interface). However, most developers who use ODBC to access their data do not make direct ODBC calls. Instead, they use an IDE that supports ODBC.

A good example of this can be found in the Borland products that use the BDE (Borland Database Engine). The BDE provides three mechanisms for accessing data, including direct local table access to Paradox and dBase file formats, and Borland SQL Links for Windows-native SQL drivers that support a number of remote database servers, such as MS SQL Server and Oracle (Borland SQL Links for Windows has now been officially deprecated).

The third data access mechanism supported by the BDE makes use of the ODBC API, through which you can use any installed ODBC driver. However, developers who use ODBC through the BDE rarely make direct ODBC calls. Instead, they use the TDataSet interface of the VCL (visual component library). The TBDEDataSet classes that implement the TDataSet interface encapsulate calls to ODBC.

While ODBC is an older standard, compared with OLE DB (and the related ActiveX data objects) and ADO.NET, it is easily the most widely supported data access mechanism for Windows and Linux. Nearly every database currently available is supported by at least one, and in some cases several, ODBC drivers. Consequently, every development environment for Windows and Linux that we are aware of provides some support for ODBC. Even Java, with its JDBC-ODBC bridge class 1 driver (Java database connectivity/open database connectivity), and .NET, with its classes in the System.Data.Odbc third-level namespace of the FCL (framework class library), provide support for ODBC.

The Advantage ODBC Driver is compliant with the core API and level 1 API for ODBC 2.0. In addition, it supports most of the level 2 API functions. For a complete list of ODBC functions and information on Advantage's ODBC conformance level, see the Advantage help.
