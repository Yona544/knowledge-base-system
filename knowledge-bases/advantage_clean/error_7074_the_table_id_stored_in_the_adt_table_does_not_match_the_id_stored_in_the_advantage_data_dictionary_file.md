---
title: Error 7074 The Table Id Stored In The Adt Table Does Not Match The Id Stored In The Advantage Data Dictionary File
slug: error_7074_the_table_id_stored_in_the_adt_table_does_not_match_the_id_stored_in_the_advantage_data_dictionary_file
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7074_the_table_id_stored_in_the_adt_table_does_not_match_the_id_stored_in_the_advantage_data_dictionary_file.htm
source: Advantage CHM
tags:
  - error
checksum: 7dca8965514dbc88404e0514dda8e169b50434ef
---

# Error 7074 The Table Id Stored In The Adt Table Does Not Match The Id Stored In The Advantage Data Dictionary File

7074 The table ID stored in the ADT table does not match the ID stored in the Advantage Data Dictionary file

7074 The table ID stored in the Advantage Data Dictionary file does not match the table being opened

Advantage Error Guide

| 7074 The table ID stored in the Advantage Data Dictionary file does not match the table being opened  Advantage Error Guide |  |  |  |  |

Problem: When opening a database table, the table ID stored in the .ADT table header does not match the corresponding table ID stored in the Advantage Data Dictionary. The cause of this error is likely the result of overwriting an existing .ADT table or overwriting an existing data dictionary file.

Solution: Avoid using the file system to overwrite an existing database table) file or data dictionary file. Use the Advantage Client Engine API or the Advantage Data Dictionary Management Utility to copy a table and modify the data dictionary file. If a table file is inadvertently deleted without it being removed from the Advantage Data Dictionary first, it can be restored by using the table's [auto-creation](master_advantage_data_dictionary.md) property. The Advantage Data Architect also has this functionality built into it and can be accessed in the table's properties.

Problem: When opening a database table, the table ID stored in the data dictionary of a DBF table does not match the table ID of the previously opened instance of the same DBF table. This error is the result of having same DBF table in two different data dictionaries.

Solution: Do not add same DBF table to two different data dictionaries.
