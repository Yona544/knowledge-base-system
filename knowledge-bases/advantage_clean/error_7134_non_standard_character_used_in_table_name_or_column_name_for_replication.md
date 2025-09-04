---
title: Error 7134 Non Standard Character Used In Table Name Or Column Name For Replication
slug: error_7134_non_standard_character_used_in_table_name_or_column_name_for_replication
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7134_non_standard_character_used_in_table_name_or_column_name_for_replication.htm
source: Advantage CHM
tags:
  - error
checksum: 0e69a3d602d179afae95886e048812091ecf810d
---

# Error 7134 Non Standard Character Used In Table Name Or Column Name For Replication

7134 Non-standard character used in table name or column name for replication

7134 Non-standard character used in table name or column name for replication

Advantage Error Guide

| 7134 Non-standard character used in table name or column name for replication  Advantage Error Guide |  |  |  |  |

Problem: Replication cannot be performed because the name of the table to be replicated or the name of one of the columns in the table to be replicated contains both the double quote (") character and closing bracket (]) character.

Solution: Avoid using non-standard characters in table names and column names. Restructure the table to remove non-standard characters in column names.
