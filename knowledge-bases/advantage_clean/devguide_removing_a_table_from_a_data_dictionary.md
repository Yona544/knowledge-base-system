---
title: Devguide Removing A Table From A Data Dictionary
slug: devguide_removing_a_table_from_a_data_dictionary
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_removing_a_table_from_a_data_dictionary.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: ce84a8db9cf294879d74580fe10d4a3476eb30c1
---

# Devguide Removing A Table From A Data Dictionary

Removing a Table from a Data Dictionary

     Removing a Table from a Data Dictionary

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Removing a Table from a Data Dictionary  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You remove a table from a data dictionary by selecting the table you want to remove from the TABLES node of the corresponding data dictionary connection and pressing the Delete key. Removing a table from a data dictionary frees the table, but does not delete it. If you want to erase a table that you have removed from the data dictionary in this way, you can do so by manually deleting the table's files from the directory (using Windows Explorer, for example).

You can also use the SQL DROP TABLE statement to remove a table from a data dictionary. This approach both removes the table from the dictionary and deletes it permanently.

   
CAUTION: There is a utility called FREEADT.EXE that can be used to free tables from a data dictionary. (This utility is located in the same directory as the Advantage Data Architect executable.) This utility should normally only be used when a data dictionary has been deleted, but the associated tables are still marked as bound to a database.
