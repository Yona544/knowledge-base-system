---
title: Devguide Data Dictionary Overview
slug: devguide_data_dictionary_overview
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_data_dictionary_overview.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 74219ee7503e4dcc7b497c887c9adbd732306fab
---

# Devguide Data Dictionary Overview

Data Dictionary Overview

 

     Data Dictionary Overview

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Data Dictionary Overview  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A data dictionary is a special file that contains a wide range of definitions that are used by Advantage to access your data. Some of these definitions apply to individual tables of your database. For example, a data dictionary can be used to associate one or more nonstructural indexes with a table. This permits Advantage to auto-open these indexes any time the associated table is opened. With free tables, you are responsible for opening these nonstructural indexes yourself, and risk index corruption if you fail to do so.

Other definitions in a data dictionary apply to two or more tables. For example, a data dictionary permits you to create referential integrity definitions. Referential integrity definitions specify how data in related tables is maintained.

When your client applications connect to Advantage in order to use free tables, you connect to a directory in which your free tables are stored. By comparison, when your data is stored in database tablesthose bound to a data dictionaryyou make your connection to the data dictionary itself. Using this connection, Advantage enforces the definitions found in the data dictionary, assuring that the tables associated with that data dictionary are maintained correctly.

When you are using ADT tables (the recommended table type for Advantage), the use of a data dictionary is an all or none proposition. Specifically, an ADT table is either a free table or a database table. Once an ADT table is associated with a data dictionary, it cannot be accessed as a free table anymore (unless you subsequently free it from the data dictionary).

Data dictionaries provide a great wealth of features, making them an indispensable part of almost all Advantage applications. The following is a list of many of the capabilities that data dictionaries provide you and your applications:

•        You can configure database tables and/or index files to be auto-created. The table structures of auto-created tables are stored in the data dictionary. At runtime, if an auto-created table is not found, the data dictionary will create it and its indexes the first time a client attempts to open that table. This feature simplifies database deployment for those developers who normally distribute some of their database tables empty.

| • | Data dictionaries permit you to define default values for fields for newly inserted records. If a value is not assigned to the field when the record is being inserted into the table, that field will be assigned the specified default value automatically. |

| • | When using a data dictionary with encrypted tables, your client applications do not have to supply each table with a password. The data dictionary does this automatically (since the client application will have already authenticated to the data dictionary). |

| • | Data dictionaries provide your client applications with access to stored procedures. Stored procedures are subroutines that run on the server and which are ideal for data intensive operations. Stored procedures are described in Chapter 7. |

| • | Data dictionaries permit you to define views. A view is a SQL SELECT statement that resides on the server, and that can be treated like a table from your client applications. Views are described in Chapter 6. |

| • | Data dictionaries permit you to implement sophisticated security. Every user can have a different user name and password that they use to access the data dictionary. Furthermore, you can customize the access rights of each user to the objects of the data dictionary. |

| • | Data dictionaries enable you to use triggers. Triggers are server-side subroutines similar to stored procedures. Unlike stored procedures, which are invoked by the client application, triggers are executed when changes are posted to a database table. Triggers permit you to implement sophisticated actions in response to changes in your data. Triggers are described in Chapter 8. |

| • | Data dictionaries permit you to replicate changes from one data dictionary to another. Replication is only available when you are using ADS, and requires an additional license in addition to the ADS license. Replication is discussed in Chapter 10. |

| • | Up to 14 nonstructural index files (with each containing up to 50 tags) can be associated with each database table in a data dictionary. The data dictionary will automatically open these index files any time you open the table, closing them when the associated table is closed. |

| • | Data dictionaries can be configured to encrypt the indexes of your ADT tables, providing additional security for sensitive data. |

| • | Data dictionaries permit you to associate record-level and field-level constraints with tables. Constraints are rules that prohibit invalid data from being posted. Defining constraints is described in Chapter 5. |

| • | Data dictionaries permit you to enforce referential integrity. Referential integrity is described in Chapter 5. |

| • | Data dictionaries allow you to create user-defined functions (UDFs). User-defined functions are reusable SQL subroutines that you can create and use in your SQL statements. UDFs are described in Chapter 13. |

| • | By default, data dictionary definitions can only be updated through a special data dictionary administrator account, which can be password protected. This allows you to prevent unauthorized changes to your data dictionary definitions. (Since Advantage 7.1, you can grant other users permission to modify some dictionary objects and properties, if you choose.) |

| • | Using a data dictionary, you can permit your client applications to connect to your tables over the Internet directly without having to resort to a Web browser interface. |

| • | You can assign to your data dictionary a major and minor version number. You can use this feature to support two or more versions of your data dictionaries. |

| • | Data dictionaries permit you to use tables from two or more directories without having to include path information in your SQL statements. |

| • | Special system tables are available to data dictionary connections. These tables, which have names like system.tables, system.usergroups, system.indexes, and so on, permit you to use SQL queries to retrieve information about your data dictionary objects. |

| • | You can work with data dictionaries through the Advantage Data Architect. This graphical tool allows you to easily manage all of your data dictionary's definitions. |

   
NOTE: Actually, you can also work with data dictionaries using SQL and the ACE (Advantage Client Engine) API. However, the Advantage Data Architect provides a much more convenient and graphical way to work with data dictionaries.  
 

Data dictionaries can be used with both ADS and ALS. The only data dictionary features that are not also available for ALS are data access over the Internet and replication. These features require ADS.
