---
title: Devguide Free Tables Versus Database Tables
slug: devguide_free_tables_versus_database_tables
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_free_tables_versus_database_tables.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 0635c80de330a105926d8f2e0769cee8ed77488a
---

# Devguide Free Tables Versus Database Tables

Free Tables Versus Database Tables

     Free Tables Versus Database Tables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Free Tables Versus Database Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There is a second major distinction between the various Advantage table types, but this is not related to table format. Instead, it is associated with how Advantage interacts with the tables. There are two data access mechanisms. Tables can either be accessed directly, or they can be accessed through a data dictionary. When tables are accessed directly, they are referred to as free tables. Tables accessed using a data dictionary are referred to as database tables.

Free tables provide far fewer features than database tables. Because Advantage accesses free tables directly, the only features available with free tables are those associated with the tables, indexes, and memo files. Security is provided by the free table's encryption (if encrypted), and validation is provided for by the table's structure, that is, the data types of the columns of the table. If any other security or validation features are desired, you must program those manually into your client applications.

Database tables are those Advantage tables that are bound to a data dictionary. By binding a table to a data dictionary, the properties defined in the data dictionary are used by Advantage when you access the table, which is how some of Advantage's more advanced features are implemented. For example, a data dictionary permits you to define constraints, which further define what data can be posted to a record. For example, you can use a constraint to prevent a negative number from being posted to an integer field. With a free table, by comparison, if you want to prevent a negative number from being posted to an integer field, that becomes the responsibility of your client applications.

When an ADT table is bound to a data dictionary, additional information is written into its header, and that information prevents the ADT from being accessed directly. This restriction ensures that the table can be accessed only through that data dictionary. Furthermore, it guarantees that the features you define for that data dictionary to which the table is bound (constraints, triggers, replication, additional index files, and so on) are respected.

Unlike an ADT database table, which can only be accessed through the data dictionary to which it is bound, DBF tables that are bound to a data dictionary can still be accessed as free tables. (These table formats do not support the ADT table header information that limits access to the bound dictionary.) As a result, even though a DBF table may be bound to one or more data dictionaries, Advantage as well as legacy applications can continue to access that table directly. Consequently, data dictionary definitions for DBF tables will not necessarily be enforced. Here is yet another argument in favor of using ADT tables over DBF format tables.

The remainder of this chapter discusses how to create ADT tables. These operations apply to both free tables and database tables, unless noted. Creating a data dictionary, and binding Advantage tables to it, is discussed in detail in Chapter 4.
