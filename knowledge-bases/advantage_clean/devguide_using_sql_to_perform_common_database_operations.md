---
title: Devguide Using Sql To Perform Common Database Operations
slug: devguide_using_sql_to_perform_common_database_operations
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_using_sql_to_perform_common_database_operations.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 92ee808a57a9ebd1157065d0b2916e880b56e1ef
---

# Devguide Using Sql To Perform Common Database Operations

Using SQL to Perform Common Database Operations

     Using SQL to Perform Common Database Operations

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Using SQL to Perform Common Database Operations  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

As pointed out in the preceding chapter, SQL (structured query language) is the common denominator among most of the Advantage data access mechanisms. With the exception of the Clipper RDD (replaceable database driver), all data access mechanisms can access your data and data dictionaries using SQL.

This chapter is designed to provide you with a large collection of examples of Advantage SQL statements. In selecting the examples presented here, we are driven by two concerns. First, we have chosen SQL statements that we feel are essential for common database-related tasks. Second, we want to provide you with a wide variety of examples that convey the breadth and power of Advantage SQL, given the limited space of a single chapter.

What we do not attempt to do with this chapter is provide the detailed syntax of the SQL statements that we cover. If we tried to do that, this chapter would be one big syntax statement. For a detailed description of the syntax of Advantage SQL, see the Advantage help.

The topics discussed in this chapter are primarily focused on tables, indexes, and data. Specifically, we do not discuss the larger issue of creating and managing data dictionaries, users, and groups within this chapter. Those topics are covered in Chapter 14, where you will also learn how to access and use metadata in your applications.

If you are already a seasoned SQL programmer, you can scan this chapter for anything that looks new or interesting. If you are new to SQL programming, we recommend that you try using each of these statements against the sample database that you can download for this book using the SQL Utility (discussed in Chapter 11).

However, before you begin working with these queries, we suggest that you make a duplicate of the data tables and your data dictionary, and create a separate, ADSSYS connection to the copy. You can then use this copy of the data dictionary and the tables without worrying about accidentally deleting or modifying data. Then, you can be creative with the copy of the database, modifying the presented queries to better understand what options you have when writing your own SQL.

   
CODE DOWNLOAD: If you'd rather not manually type in the queries in this chapter, you can find all of them listed in this chapter in the file named ch12queries.sql on this book's code download (see Appendix A). Each of the queries in this file has been commented out. To use a query in this file, copy the query text to the clipboard and insert it into in the SQL Utility or a querying tool of your choice. Then, simply highlight the desired SQL statements that you want to execute and execute the query.
