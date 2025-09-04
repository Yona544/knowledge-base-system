---
title: Master Long Field Names And Long Index Names
slug: master_long_field_names_and_long_index_names
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_long_field_names_and_long_index_names.htm
source: Advantage CHM
tags:
  - master
checksum: d700fd1cad0b8f63eb79f6021d1f7f7f1014422c
---

# Master Long Field Names And Long Index Names

Long Field Names and Long Index Names

Long Field Names and Long Index Names

Advantage Concepts

| Long Field Names and Long Index Names  Advantage Concepts |  |  |  |  |

Field names and index order names in the Xbase file format are limited to 10 characters in length. However, if you are using Visual FoxPro (VFP) tables in a data dictionary, field names can be up to 128 characters in length. Note, though, that the field names stored in the physical table are still only 10 characters so if the table becomes separated from the dictionary without using a standard method for removing tables from dictionaries (e.g., SQL, Advantage Client Engine API, or Advantage Data Architect), then the associated indexes might not be valid. This is because when long field names are used with Visual FoxPro tables, the index key expressions include the long name, so those key expressions would no longer match the table.

Field names and index order names in the Advantage proprietary file format can be up to 128 characters in length. Because the long field names are stored in the table itself, there are fewer potential problems if a table is inadvertently separated from the dictionary. If you have the need for field names or index order names longer than 10 characters, you may want to choose the Advantage proprietary file format.
