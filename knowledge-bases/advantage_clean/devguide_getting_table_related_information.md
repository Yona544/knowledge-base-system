---
title: Devguide Getting Table Related Information
slug: devguide_getting_table_related_information
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_getting_table_related_information.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 78da02b948a67cd3ff8c1f8fed49517fb5c02217
---

# Devguide Getting Table Related Information

Getting Table-Related Information

     Getting Table-Related Information

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Getting Table-Related Information  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are five system tables that provide you with information about your dictionary-bound tables: system.tables, system.columns, system.indexes, system.indexfiles, and system.triggers. The table system.tables contains one record for each table in your data dictionary. (Views are not listed in this table. You can get view information from the system.views table.) Columns in this table contain information about a table's name, physical location on disk, encryption, permissions level, primary key, and record-level constraint, to name a few.

The following query retrieves information about all nonsystem tables in the data dictionary:

SELECT \* FROM system.tables

The next query returns one record with information about the PRODUCTS table:

SELECT \* FROM system.tables  
  WHERE NAME = 'PRODUCTS'

The system.columns table contains one record for every field in every table in your data dictionary. Fields in this table include the name of the field, the name of the table to which the field belongs, the ordinal position of the field in its table structure, column type, constraints, and so forth.

The values in the Field\_type column are integer codes. Table 14-1 contains the values for these codes.

 

| Type | Value |
| ADS\_UNKNOWN | 0 |
| ADS\_LOGICAL | 1 |
| ADS\_NUMERIC | 2 |
| ADS\_DATE | 3 |
| ADS\_STRING | 4 |
| ADS\_MEMO | 5 |
| ADS\_BINARY | 6 |
| ADS\_IMAGE | 7 |
| ADS\_VARCHAR | 8 |
| ADS\_COMPACTDATE | 9 |
| ADS\_DOUBLE | 10 |
| ADS\_INTEGER | 11 |
| ADS\_SHORTINT | 12 |
| ADS\_TIME | 13 |
| ADS\_TIMESTAMP | 14 |
| ADS\_AUTOINC | 15 |
| ADS\_RAW | 16 |
| ADS\_CURDOUBLE | 17 |
| ADS\_MONEY | 18 |
| ADS\_LONGLONG | 19 |
| ADS\_CISTRING | 20 |
| ADS\_ROWVERSION | 21 |
| ADS\_MODTIME | 22 |
| ADS\_NUMBER | 23 |

Table 14-1: Field Type Codes
