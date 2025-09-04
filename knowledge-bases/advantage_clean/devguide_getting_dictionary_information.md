---
title: Devguide Getting Dictionary Information
slug: devguide_getting_dictionary_information
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_getting_dictionary_information.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: ea61e3efbbc6a58ff188241c279b7aaebde6273c
---

# Devguide Getting Dictionary Information

Getting Dictionary Information

     Getting Dictionary Information

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Getting Dictionary Information  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

You retrieve the properties of your data dictionary using the system.dictionary table. This table has one record, which contains one field for each property of the data dictionary to which you are connected. The following is how a query of this system table looks:

SELECT \* FROM system.dictionary

If you are connected to the data dictionary using the administrator's account (or a user with ALTER database privileges), every column in this record is populated with the associated property value. If you are connected on any other account, only the Version\_major and Version\_minor columns of this table are populated--all other columns contain NULL values.

Full text search defaults are also a data dictionary property. To list the full text search defaults for your data dictionary, query system.fts. This table returns one record.
