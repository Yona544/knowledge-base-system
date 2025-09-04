---
title: Devguide Creating And Modifying Objects
slug: devguide_creating_and_modifying_objects
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_creating_and_modifying_objects.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 8a0ba456ead18efffe08960ef6653519208b63ed
---

# Devguide Creating And Modifying Objects

Creating and Modifying Objects

 

     Creating and Modifying Objects

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Creating and Modifying Objects  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Which came first, the table or the data? The data, of course, which is why you need the table in the first place. But seriously, you can't have a database without one or more tables. Furthermore, tables are not much use if you do not have indexes for them. After that, views, stored procedures, triggers, and the like prove quite valuable.

This section covers three essential SQL statements: CREATE, ALTER, and DROP. You use CREATE to create tables and data dictionary objects, ALTER to modify the structure of an existing table, and DROP to destroy objects. Each of these statements is covered in the following sections.
