ADS Is High Performance




Advantage Database Server 12  

     ADS Is High Performance

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

|  |
| --- |
|  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| ADS Is High Performance  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  | Feedback on: Advantage Database Server 12 -      ADS Is High Performance Advantage Database Server v8.1: A Developers Guide by Cary Jensen and Loy Anderson     2007 Cary Jensen and Loy Anderson. All rights reserved. devguide\_ADS\_Is\_High\_Performance Advantage Developer's Guide > Part I - Advantage and Advantage Data Architect > Chapter 1 - Introduction > ADS Is High Performance / Dear Support Staff, |  |
| ADS Is High Performance  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

First of all, ADS is a high-performance server. It permits you to manage very large quantities of data, and to access that data in a multiuser environment with unbelievable speed. For example, so long as you have designed your tables and indexes correctly, you can usually locate a particular record or subset of records in your database in a fraction of a second.

ADS's performance derives from its underlying architecture. Unlike many of the more complicated and expensive database servers, such as Microsoft's SQL Server and Oracle, ADS is not a traditional set-based relational database server based on SQL (the structured query language, pronounced "sequel"). Instead, ADS is an ISAM (indexed sequential access method) relational database server. ISAM databases use indexes extensively, permitting them to perform high-speed table searches, filtering, and table joins.

Even though it is an ISAM server, ADS provides extensive support for the SQL language. Indeed, with ADS you can use the industry standard SQL language to perform almost any task related to the management of your data. When it comes to data access, these SQL statements are translated by Advantage into optimized, index-based operations, providing you with an unbeatable combination of speed and accessibility.

The ISAM architecture has a long history. It is the same architecture that is used by venerable databases such as dBase, FoxPro, and Clipper. However, those databases are file-server databases, while ADS is a client/server database server. In other words, ADS provides the unbeatable combination of proven performance and client/server reliability.

Unlike traditional ISAM databases, however, ADS supports many of the features that you find in high-end, set-based SQL database servers. For example, ADS supports views, stored procedures, triggers, referential integrity, online backup, replication, and domain integrity constraints.

Another performance-related ISAM feature distinguishes ADS from set-based SQL databases. ISAM databases support a navigational model of data access, whereas set-based SQL databases do not.

In the set-based database model, in theory at least, there is no record order. As a result, the SQL language does not support the concept of navigating a database. While some set-based SQL databases know that record B follows record A, the only way to move to a record that is 100 records after record A is to retrieve the record that follows A, then retrieve the record that follows that one, and again, and again, until this task is performed 100 times.

Consider the Delphi language, which natively supports a navigational model of data access, a legacy of the BDE (Borland Database Engine). (It also supports set-based access, but that's not the point here.) Imagine that a Delphi DBGrid (a grid-like component used for displaying the rows and columns) displays data from a SELECT \* FROM CUSTOMER query against a set-based SQL server where the CUSTOMER table contains a million records. If the end user presses Ctrl-End while the DBGrid displaying this result set is active, the DBGrid will navigate to the last recordbut in order to do so, it must fetch every single record. Anyone who has seen this knows that it will take a very, very long time before the last record is reached. Furthermore, both the server and the network will be kept busy by this operation.

By comparison, records in an ISAM database have a record order, based on the current index (or natural record order, if no index is currently selected). If you point a Delphi DBGrid to an Advantage table with a million records, and press Ctrl-End, you will move immediately to the last record. This is because Advantage can use the current index or the table's natural order to go to the last record, and then return only those last records needed to fill the display of the DBGrid.

This is an important point, especially if you are coming to Advantage from a file-server database, such as MS Access, dBase, or Paradox. File-server databases permit a navigational approach. If you want to migrate one of these databases to a set-based SQL database server, unless your database is very small, you will likely have to reprogram your user interface to remove navigational features. Otherwise, users' attempts to navigate can have serious consequences for your application's performance.

Changing your user interface isn't just time-consuming; end users love the navigational interface. Having a grid that displays some records from a table, and having the impression that they can easily jump to somewhere in the middle of that table (or anywhere in the table they want to) is very appealing to end users. With Advantage, you can provide this feature, but with set-based SQL servers, you should not.

Here is another way to look at it. With Advantage you have a choice. You can write your applications using the portable and more or less standardized SQL language, or you can use a navigational modelor you can use both. With traditional SQL-based remote database servers, you are limited to the set-based model.

A number of the Advantage data access mechanisms permit you to build client applications that use the navigation model. These include the Advantage TDataSet Descendant, which can be used by Delphi, Kylix, and C++Builder, as well as languages that can make direct calls to the Advantage Client Engine, which include the aforementioned products as well as Visual Basic and Visual C++. Even the Advantage .NET Data Provider and the Advantage Visual Objects client support the navigational model of data access.

   
NOTE: Development environments that can use ADO (ActiveX data objects) can leverage most of the navigational model through the Advantage OLE DB Provider. ADO, however, does not support setting ranges (also referred to as scopes).