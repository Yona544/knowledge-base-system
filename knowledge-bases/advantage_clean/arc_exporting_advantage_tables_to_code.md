---
title: Arc Exporting Advantage Tables To Code
slug: arc_exporting_advantage_tables_to_code
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_exporting_advantage_tables_to_code.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 5c06124b142add63bed1099363355c5d72ddc5da
---

# Arc Exporting Advantage Tables To Code

Exporting Advantage Tables to Code

Exporting Advantage Tables to Code

Advantage Data Architect

| Exporting Advantage Tables to Code  Advantage Data Architect |  |  |  |  |

The Advantage Tables to Code Generator provides a convenient way to reverse engineer existing tables into functions or SQL scripts. The output code contains all of the necessary calls to re-create a table and associated indexes in a specified directory. There are three possible types of output code: Delphi (Pascal), C++Builder (C++), or SQL.

Delphi

The structure of the Delphi output code from the generator is as follows: A unit named CreateTables is generated that contains procedures to create every table that was reverse engineered. Each procedure takes the directory of where to create an individual table as input. The name of each procedure is CreateXXXX where XXXX is the base name of the table. Because Delphi does not support numeric or varchars fields, these field types cannot be created using Delphi code; instead, use SQL. Delphi 3 also has a known problem of being able to maintain, but not create, indexes with ixExpression as an attribute.

C++Builder

The structure of the C++Builder output code from the generator is as follows: A class named CreateTables is generated that contains functions to create every table that was reverse engineered. The input for each function is the directory in which the table is to be created. The name of each function is CreateXXXX where XXXX is the base name of the table. Because C++Builder does not support numeric or varchars fields, these field types cannot be created using the C++Builder code; instead, use SQL.

SQL

The SQL output of the generator consists of a series of semicolon delimited SQL-92 statements. The statements first create a table then create the indexes associated with that table. Creating tables using SQL provides an exact copy of the table it was generated from.

To reverse engineer tables:

| 1. | Start the Advantage Tables To Code Generator from Tools | Export Table Structures as Code. |

| 2. | Select the tables along with any non-auto-open indexes associated with them. |

| 3. | Select the output code type. |

| 4. | Generate the output code. |

| 5. | Save the code to disk. |

Note The Delphi and C++Builder functionality cannot create a table that has case insensitive fields. To correctly create these tables, use the SQL Tables-to-Code functionality.
