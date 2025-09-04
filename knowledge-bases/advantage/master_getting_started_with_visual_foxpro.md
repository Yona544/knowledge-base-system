Getting Started with Visual FoxPro




Advantage Database Server 12  

Getting Started with Visual FoxPro

Advantage and Visual FoxPro

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Getting Started with Visual FoxPro  Advantage and Visual FoxPro |  |  | Feedback on: Advantage Database Server 12 - Getting Started with Visual FoxPro Advantage and Visual FoxPro master\_Getting\_started\_with\_visual\_foxpro Visual FoxPro > Getting Started with Visual FoxPro / Dear Support Staff, |  |
| Getting Started with Visual FoxPro  Advantage and Visual FoxPro |  |  |  |  |

Introduction

Advantage has a long history of supporting FoxPro tables and indexes. In the early days, one Advantage client was a 16-bit CA-Clipper RDD (replaceable data driver) that supported an early FoxPro file format. Over the years, Advantage has matured into a feature-rich product with support for many different development environments. With the release of Advantage 9.0, much of the focus has been to add features that will benefit Visual FoxPro developers. The 9.0 release added support for more DBF field types such as DateTime, Varbinary, Varchar, Autoinc, and Currency. It also includes support for NULL field values, candidate keys, and international [collation support](master_collation_support.htm) compatible with Visual FoxPro. With this and other new functionality added to Advantage Database Server, it creates a powerful client/server solution for native DBF file support with transactions, full text search, referential integrity, replication, encryption, support for DBFs over 4GB, and other great features.

All of this comes with a major benefit: It is not necessary to convert your DBF data to another format in order to use Advantage. In fact, it is possible to continue using existing Visual FoxPro applications to access the data while concurrently accessing the same data with Advantage-enabled applications.

The numerous Advantage client options open up many opportunities. In addition to being able to add client/server data access to your Visual FoxPro application and access the same tables concurrently with Visual FoxPro, you can use other Advantage clients to access your data in completely new ways. The Advantage ODBC driver gives the ability to access your Visual FoxPro 9 tables from many different applications. You can create a web application using the Advantage .NET Data Provider using your existing data. Or use the Advantage JDBC driver to extend your application onto new platforms. Available clients include an OLE DB provider, an ODBC driver, a JDBC driver, a PHP driver, a DBD driver for Perl, a TDataSet descendant for Delphi, a Visual Objects RDD, the Advantage Client Engine API for powerful low level data access, and the general purpose Advantage Data Architect for table and database management.

In addition, Advantage provides a natural migration path for Visual FoxPro developers writing new applications using Visual Studio. Advantage provides direct table access previously not available to ADO.NET developers. Advantage Database Server allows developers the flexibility to combine powerful SQL statements and relational data access methods with the performance and control of navigational operations, such as direct table and index access and direct table movement (seeks, skips, etc.). Combining these two powerful data access methods allows the result set returned from an SQL query or from a table opened directly to be navigated via the highly optimized Advantage ISAM database engine. The result is an easy-to-use interface that supports SQL commands and direct-result-set navigation.

Integrating Advantage with Visual FoxPro

Visual FoxPro provides several different data access mechanisms that can be utilized to integrate Advantage into your existing application. Aside from Visual FoxPros native data access, some common methods to access external data are [Remote Views](master_remote_views.htm), [Cursor Adapters](master_cursor_adapters.htm), and [SQL Pass Through](master_sql_pass_through.htm).

Because Advantage can share your DBF tables with existing Visual FoxPro applications, it is possible to change applications in piecemeal fashion rather than needing to accomplish a full conversion in a single step. You can also add new Advantage-enabled applications on top of existing applications.

DBC Conversion Utility

Advantage does not support direct access to the database container (DBC) file. Therefore, if you are using a DBC it may be desirable to run DBCConvert.prg against the DBC. This utility is installed with the Advantage OLE DB provider and the Advantage ODBC driver. This utility will create an Advantage Data Dictionary based on the contents of a DBC. It does not modify the DBC or any data. The utility will create an ADD that references all of the tables referenced in the DBC, create long field names, convert table and field validation rules, default field values, and convert referential integrity rules.

Data Access Mechanisms

One of the great features of Visual FoxPro is the way that it integrates the data access mechanisms into a similar programming paradigm. Once the data has been retrieved (e.g., through a remote view or a cursor adapter), the subsequent usage of the data is the same as if it had been retrieved through a USE statement. This reduces the amount of code that you need to change in order to use Advantage to handle your data.

The following sections give a brief introduction to some of the possible data access options that Visual FoxPro provides.

[Remote Views](master_remote_views.htm)

[Cursor Adapters](master_cursor_adapters.htm)

[SQL Pass Through](master_sql_pass_through.htm)