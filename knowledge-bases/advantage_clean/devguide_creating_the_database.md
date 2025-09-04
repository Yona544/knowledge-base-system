---
title: Devguide Creating The Database
slug: devguide_creating_the_database
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_the_database.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 20d770659d47797d75d8614a97d5582afbb2a3f3
---

# Devguide Creating The Database

Creating the Database

     Creating the Database

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating the Database  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A database, as the term is used here, is a collection of files used by Advantage. These files include tables, memo files, indexes, and in most cases, a data dictionary.

   
NOTE: If you are unfamiliar with what the parts of a database are, you might want to take a quick look at Chapter 2 (creating tables), Chapter 3 (defining indexes), and Chapter 4 (using data dictionaries). The introductions to each of these chapters define what these various files are, and what roles they play in a database.  
 

In most cases, you use the Advantage Data Architect to create your database. Specifically, you either import existing data into one or more tables, or you design the tables from scratch. You then consider how your data will be accessed by the client applications, and design the indexes that will make that access fast.

In many cases, you also design a data dictionary. A data dictionary, as far as Advantage is concerned, is a special file that is used to access all of the tables within a given application. Data dictionaries provide your client applications with a number of powerful features, such as security, constraints, views, triggers, and referential integrity, to name just a few. Here again, you will probably use the Advantage Data Architect to create your data dictionary.

Instead of using the Advantage Data Architect to create your database, you can also create your database at runtime from one or more of your client applications. To do this, your client applications would need to include code that defines new tables, indexes, and data dictionaries, as needed, on-the-fly. Your client applications would not explicitly create memo files. Memo files are created automatically when data is inserted into large, variable-length table fields, such as memo, binary, or image fields.

Creating databases on-the-fly from within a client application requires quite a lot of code, compared with creating databases with the Advantage Data Architect, which is an interactive operation. Fortunately, creating a database at runtime is normally only necessary in special situations. For example, some applications need to store separate data in separate databases. If these applications need to be able to create a new database at any time, you will probably need to make the extra effort to create the new database at runtime.

   
NOTE: The Advantage Data Architect can generate the code necessary to define a database. Consequently, if you need to create a database on-the-fly, you can still use the Advantage Data Architect to create the database, and then have the Advantage Data Architect generate the code that you can add to your application. In addition, a data dictionary can be configured to automatically create the tables, indexes, and memo files it requires without code.  
 

Before a client application can access the tables, indexes, and data dictionary of an application, the client workstation must be able to send IP or IPX packets to the server upon which Advantage Database Server is running. Client applications don't even need the rights to access the individual files. The server does this. The exception is when the client is using ALS, in which case the client application must have rights to the database files.

The server on which you install your database and the Advantage Database Server can be running one of the following operating systems: Windows NT 4.0 (Service Pack 6 or later), Windows 2000, Windows 2003, or Linux.

Actually, there are three versions of the ADS server. The most popular version is designed for Windows NT 4.0 or later, which includes 2000 and 2003. The Linux version of ADS requires glibc 2.1.2-11 or newer and kernel version 2.2 or newer.

   
NOTE: Windows XP and Windows Vista (which was in beta at the time of this writing) are not listed as supported operating systems since these operating systems are marketed by Microsoft as client operating systems only, not as server operating systems. ADS for Windows NT/2000/2003 runs on XP and Vista.  
 

Some final comments about creating a database are in order before continuing on to the discussion about building client applications. First, while creating tables, indexes, and data dictionaries is not hard, the design of the tables, indexes, and data dictionaries is often the result of research and thoughtful consideration.

For example, you need to take into account what kind of data you need to store and how it will be used. This will lead you to consider how many tables you will need to create, and what indexes you will add to them. Likewise, how you set up a data dictionary, including what groups and users to add, what views to define, and whether to use referential integrity, can have a big impact on the success of your database application.

A second consideration is that the design of your database is something that will likely change over time. In short, database design is often an iterative process.

As your design begins to take shape, you will typically discover that a particular table is missing one or more fields, or that additional indexes need to be created, or that entirely new tables must be added.

These changes, when they happen, will often affect both the server and the client parts of the application. For instance, if you find that you have to add a new field to a table, you might use the Advantage Data Architect to update the table file. In most cases you will then also need to change your client applications so that they can use the newly added field.
