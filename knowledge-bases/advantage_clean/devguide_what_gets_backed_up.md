---
title: Devguide What Gets Backed Up
slug: devguide_what_gets_backed_up
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_what_gets_backed_up.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 269f60ba7a40c5972de7bdbd4af91b165ba93990
---

# Devguide What Gets Backed Up

What Gets Backed Up

 

     What Gets Backed Up

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| What Gets Backed Up  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Before going any further, it is important to consider what Advantage's online backup actually backs up. In short, Advantage's online backup makes a backup of your data--your tables, memo files, and in the case of free tables, your indexes. If you are backing up a data dictionary, the data dictionary gets backed up as well. Since a data dictionary describes the indexes of your database, Advantage does not need to create index backups when backing up a data dictionary.

There are many aspects of your applications that do not get backed up. Online backup does not back up your external libraries used as stored procedures or triggers. Online backup also does not make backups of your client applications. Similarly, online backup does not back up other external files that your applications may require, such as INI files, bitmaps stored on disk, files written by your application, or any other files that your client applications or external libraries read or write.

In other words, online backup is designed to back up the Advantage-specific data files that reside on your server. Since the server is rarely the same machine as the one on which you develop your external stored procedures, external triggers, and client applications, there is an implicit assumption that you already have backups of those files. With respect to your source code files, presumably this code is also maintained through a version control system.

If your client applications use or create other external files that are not part of your Advantage database, and these files must also be backed up, it is up to you to provide some mechanism for backing up these files. This may be to simply zip these files up from time to time, placing the zipped file in a backup location.

Alternatively, you might consider reading these external files into memo files of a special Advantage table that you create as part of your database. If you store copies of your external files in an Advantage table, and this table is part of your data dictionary or is stored in the same free table directory as the rest of your data, this information will then be backed up as part of your Advantage backup procedure.

   
NOTE: If you read your external files into an Advantage table for the purpose of backing them up, you must not only write the code and create the operational procedures for loading these files into the table from time to time, you must also write the code that will restore these files to disk from the table following a restore operation on the database.
