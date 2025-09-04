---
title: Devguide Encrypting Database Tables
slug: devguide_encrypting_database_tables
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_encrypting_database_tables.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: df4b5b4badb65581d4472b9e8ca989870bd00836
---

# Devguide Encrypting Database Tables

Encrypting Database Tables

     Encrypting Database Tables

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Encrypting Database Tables  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Once you have enabled encryption for the data dictionary, you can selectively encrypt tables in the data dictionary. Once encrypted, a table's contents are scrambled on disk, which prevents someone from examining your data with a low-level file viewer.

Use the following steps to encrypt the two tables of this data dictionary:

1.        If the TABLES node of the DemoDictionary connection is not expanded, click the + next to this node to display the nodes for the CUSTOMER and EMPLOYEE tables.

| 2. | Right-click the CUSTOMER node and select Encrypt. After a brief moment, the glyph that appears to the left of the CUSTOMER table node will change. The new glyph depicts an encrypted table. |

| 3. | Now right-click the EMPLOYEE node and select Encrypt. The glyph for this node will soon reflect that this table is also encrypted. |
