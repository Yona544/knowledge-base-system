---
title: Devguide Declaring Variables
slug: devguide_declaring_variables
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_declaring_variables.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: e85c4be0398a3d74c2732391444155c7327fadd9
---

# Devguide Declaring Variables

Declaring Variables

     Declaring Variables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Declaring Variables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Any variables that you want to use in an Advantage SQL script must be declared at the top of the script. Variables are declared using the DECLARE keyword, which is then followed by a list of one or more variable declarations. Each variable in the list consists of a variable name followed by at least one space and then the variable type. Variable names cannot contain spaces, and cannot be quoted. When two or more variables are declared in a single DECLARE statement, they are separated by commas.

The variable type can be any of the valid data types for ADT tables, with the exception of AUTOINC. The following is the list of supported types:

•        Blob

| • | Char |

| • | CIChar |

| • | CurDouble |

| • | Date |

| • | Double |

| • | Integer |

| • | Logical |

| • | Memo |

| • | Money |

| • | Numeric |

| • | Raw |

| • | Short |

| • | Time |

| • | TimeStamp |

There are two additional valid data types. These are String and Cursor. String is similar to Char, with the exception that Char and CIChar variables have a fixed length (and are padded with spaces if they hold text smaller than their declared size), while a String is dynamically allocated and can grow to almost any size (and dynamically shrink, as well).

Variables that are of type Cursor are used to refer to a SQL SELECT result set. The use of cursors is discussed later in this section.

An Advantage SQL script may include more than one DECLARE statement. However, all DECLARE statements must be in the first lines of the script.

The following is an example of an Advantage SQL script segment with four declared variables:

DECLARE Name String;  
DECLARE Height Short, Description Memo;  
DECLARE Password Char(20);  
// script statements follow

Variables can be used as expressions in SQL statements within your Advantage SQL scripts. However, since variable names cannot be quoted (or enclosed in square braces), the Advantage team recommends that you precede variable names that you will use as expressions in SQL statements with the @ character. This avoids the possibility of a variable name conflicting with the name of a field in your table.

The following is an example of a simple Advantage SQL script that uses a variable as an expression:

DECLARE @empid Integer;  
@empid = 89;  
SELECT \* FROM EMPLOYEE   
  WHERE [Employee Number] = @empid;

   
NOTE: In the SQL scripts that we write for our Advantage applications, we have found it useful to precede all variables by the @ characternot just those intended for use in queries. We find this approach reduces ambiguity and improves script readability.
