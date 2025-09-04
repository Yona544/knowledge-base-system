---
title: Devguide Views That Use Other Database Tables
slug: devguide_views_that_use_other_database_tables
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_views_that_use_other_database_tables.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: eb9a8459bc9a8bb202dfa7b3e27f512a0ed853fc
---

# Devguide Views That Use Other Database Tables

Views That Use Other Database Tables

 

     Views That Use Other Database Tables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Views That Use Other Database Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Most client applications need to work with data in a single data dictionary. But what do you do if you want to work with data in two different data dictionaries? Actually, this is not hard if you are willing to use more than one connection. For example, you can establish one connection to one data dictionary, and another connection to the other data dictionary. Because the licensing of the Advantage Database Server permits a single workstation to make any number of connections, there is no monetary cost associated with this approach.

As you learned in Chapter 2, ADT tables that are bound to a data dictionary cannot be accessed directly. They must be accessed through the data dictionary to which they are bound. As a result, references to database tables in a view must include a reference to the data dictionaries to which they are bound.

There are two ways to qualify a table name with the data dictionary to which it is bound, and both of these use dot notation. The first way is to qualify the table from the other data dictionary by including the name of the data dictionary in which the table resides, separating this path from the table name using a dot, or period.

The second way to qualify a data dictionarybound table name is to precede the table name with a data dictionary link. As is the case when you use a data dictionary path, this data dictionary link is separated from the table name by a period.

Before continuing, it is worth noting that the issue of referring to tables in other data dictionaries is not actually a view issue, but a SQL issue. Specifically, the linking that is discussed in this section can be used in views and in SQL statements that you send directly to Advantage.
