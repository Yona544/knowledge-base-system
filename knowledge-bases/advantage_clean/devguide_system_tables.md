---
title: Devguide System Tables
slug: devguide_system_tables
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_system_tables.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: b803eeceed0899d6fd73684f21f861054feafc1d
---

# Devguide System Tables

System Tables

 

     System Tables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| System Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Both ADS and ALS provide 25 system tables that you can query to retrieve metadata about your data dictionaries and the objects they contain. These tables are available whenever you are connected to a data dictionary.

•        system.articles

| • | system.columns |

| • | system.dictionary |

| • | system.effectivepermissions |

| • | system.functions |

| • | system.fts |

| • | system.indexes |

| • | system.indexfiles |

| • | system.iota |

| • | system.links |

| • | system.objects |

| • | system.packages |

| • | system.permissions |

| • | system.publicationarticles |

| • | system.publications |

| • | system.relations |

| • | system.storedprocedures |

| • | system.subscriptions |

| • | system.systemprocedures |

| • | system.tables |

| • | system.triggers |

| • | system.usergroupmembers |

| • | system.usergroups |

| • | system.users |

| • | system.views |

You use system tables to discover the properties of the data dictionary you are connected to, the names of tables bound to that data dictionary, individual table structures, index filenames, index order names, constraints, views, permissions, subscriptions and publications, packages and user defined functions, and stored procedures. If you are connected to a data dictionary using the administrative account (ADSSYS) or a user account with appropriate ALTER privileges, you can also get information about referential integrity constraints, users, groups, and access permissions.

In order to ensure that system table names are unique and identifiable, all system tables are qualified using dot notation with the "system" namespace. For example, you use the system.columns table to obtain information about the individual columns available in your database tables, and the system.users table to retrieve information about the data dictionary's users.

You access system tables by querying them. For example, the following query returns information about the user defined functions associated with the data dictionary to which you are connected:

SELECT \* FROM system.functions

System tables are often used to automate the management of your data dictionaries from your client applications. For example, if your client application creates a new table that must be available to all users, you can use information in the system.users and system.usergroupmembers system tables to determine which groups and users need to have access rights granted to them.

The actual granting of the rights is something that your client application can do using the SQL GRANT statement (described later in this chapter). Note, however, that creating automated operations like these requires that the client application connect to the data dictionary using an account that has ALTER permissions for groups and/or users and the appropriate WITH GRANT permissions for the associated objects.

   
NOTE: User and group permissions have three possible states: the permission, the permission WITH GRANT (can grant the permission to other users or groups), or no permission. Assigning permissions is discussed in Chapter 4.  
 

In order to protect confidential information, the information that is returned in a system table query is sensitive to the rights of the user whose connection is used for the query. When queried using the data dictionary administrative connection, all information contained in the data dictionary is available. By comparison, user connections are limited as to what information can be retrieved, based on their access rights. The system table may not be accessible, or the system table may contain less information than when queried by ADSSYS or a user with the appropriate ALTER privileges.

The following sections are divided into related topics, where one or more system tables are discussed in each section. Each discussion includes the primary purpose of the table or tables. In many cases, individual fields in the returned result sets are introduced, and some example queries are given. However, no attempt is made to list the complete structures of the tables being examined. That information is available in the Advantage help. Also, additional fields will likely be added to these tables in future versions of Advantage. You can easily discover the column names of each of these tables by executing a simple SELECT \* FROM query against the desired system table using the SQL Utility while connected on the ADSSYS account.

   
NOTE: In most cases, character-based fields in these system tables are of the type cicharacter, meaning that queries against these fields are case-insensitive. The exceptions are fields of type memo, which are case-sensitive.
