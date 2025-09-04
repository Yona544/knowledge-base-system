---
title: Devguide Renaming And Moving Dictionary Objects
slug: devguide_renaming_and_moving_dictionary_objects
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_renaming_and_moving_dictionary_objects.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: ba20e94623d80465c27c08885213a1a15595f807
---

# Devguide Renaming And Moving Dictionary Objects

Renaming and Moving Dictionary Objects

     Renaming and Moving Dictionary Objects

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Renaming and Moving Dictionary Objects  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Any object listed in a data dictionary connection can be easily renamed. Right-click the object you want to rename and select Rename. Provide the new name for your object in the Rename Object dialog box.

When the object is also an external file, such as a table or stored procedure, the option to move the object is also available from the object's context menu. Using the move feature, the file and its associated files (such as the index and memo files for a table) are physically moved to the new location that you specify. Furthermore, the relative path within the data dictionary is updated to reflect the new location.

Moving objects is not a permissible (or reasonable) operation on a free table connection. Specifically, all tables on a free table connection must reside in the same directory. As a result, moving a table in this situation doesnt make sense. Similarly, free table connections do not support non-table external files. For example, free table connections do not have stored procedures or triggers.
