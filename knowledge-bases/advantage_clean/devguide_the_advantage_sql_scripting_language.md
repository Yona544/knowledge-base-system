---
title: Devguide The Advantage Sql Scripting Language
slug: devguide_the_advantage_sql_scripting_language
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_the_advantage_sql_scripting_language.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 5cc521e3214c53cb9a67dc83faf5547503dc8da1
---

# Devguide The Advantage Sql Scripting Language

The Advantage SQL Scripting Language

     The Advantage SQL Scripting Language

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| The Advantage SQL Scripting Language  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Since Advantage 7, Advantage SQL has supported SQL scripts, which are two or more SQL statements separated by semicolons. In Advantage, this feature is referred to generically as Advantage SQL scripts.

Several powerful new features have been added to Advantage SQL scripts in Advantage 8. As discussed in Chapter 11, now Advantage SQL scripts return a result set if the last statement in the script is a SELECT statement. Similarly, Advantage SQL scripts process parameters much more intelligently than in previous versions.

The most powerful new feature, however, is Advantage SQL script support for ANSI (American National Standards Institute) standard SQL persistent stored modules (PSMs). ANSI SQL PSM 2003 specifies the syntax and semantics of statements that add a procedural capability to the SQL language. With PSM support, Advantage SQL scripts now can include variable declaration and assignment, branching and looping control structures, cursors, dynamic SQL execution, exception handling, and more.

With these new capabilities, Advantage SQL scripts are now more useful than ever for creating stored procedures and triggers. Here's a case in point. In our last book on Advantage (Advantage Database Server: The Official Guide, Cary Jensen and Loy Anderson; 2003, McGraw-Hill/Osborne), Advantage 7 could not create the Get10Percent stored procedure via SQL. Our only option for creating it was to rely on a third-party compiler, such as Delphi, C#, or VB for .NET.

If you recall from Chapter 7 of this book, you did create this stored procedure using SQL in Advantage 8. The support for PSMs in Advantage SQL scripts made this possible. What this means for you is that there are many different types of SQL stored procedures and triggers that you can create in Advantage 8 that were impossible in previous versions.

For those of you developing your applications in an environment that does not support the creation of DLLs (32-bit Windows), shared object libraries (Linux), or .NET managed assemblies, you now have a powerful and flexible solution for creating stored procedures and triggers without resorting to a third-party compiler.

Even if you are using a language that can compile external stored procedures and triggers, Advantage SQL scripts offer a solution for creating triggers and stored procedures that are operating system independent and require no additional files to be deployed to your servers.

There is another new benefit of Advantage SQL scripts. You can use Advantage SQL scripts to write user defined functions (UDFs). User defined functions are reusable subroutines that you create, after which you can use just as if they were SQL scalar functions. Creating and using UDFs is discussed later in this chapter.
