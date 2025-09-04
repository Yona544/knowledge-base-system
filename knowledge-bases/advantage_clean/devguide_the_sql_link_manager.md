---
title: Devguide The Sql Link Manager
slug: devguide_the_sql_link_manager
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_the_sql_link_manager.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 1d44acb3b19615ba84606b55bdcaf1ace9fdb83f
---

# Devguide The Sql Link Manager

The SQL Link Manager

     The SQL Link Manager

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| The SQL Link Manager  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Links are objects that you add to a data dictionary in order to query tables from two or more data dictionaries. However, what if you occasionally want to query tables from two or more data dictionaries from within Advantage Data Architect, but do not need to do this from your client applications? The answer is the Link Manager of the SQL Utility, shown in Figure 4-14.

The Link Manager is a feature of the SQL Utility when you are querying on a data dictionary connection. You use it to create temporary links to other data dictionaries. These links will remain available so long as you remain connected to the data dictionary for which you define these links. Once you close the connection, these temporary links are removed.

To create a temporary data dictionary link, use the following steps:

Open the SQL Utility on a connected data dictionary connection (select Tools | SQL Utility). Right-click in the top of the SQL Utility to display a context menu and select Link Manager. The Active Links dialog box in Figure 4-14 is displayed.

In the Create Link section, enter a name for the temporary link in the Link Alias field. Although a link alias is not required, it is recommended since it simplifies the SQL statements that use the link, permitting you to qualify the linked table using the link alias.

Figure 4-14: The Active Links dialog box of the SQL Utilitys Link Manager allows you to create and work with active links

Enter the path and data dictionary name to which the link should refer. If you do not define a link alias, this full path and name must be used to qualify linked tables.

Enable Authenticate Active User if the user name and password for your current connection is also a valid user name and password (with the needed privileges to objects you want to link to) for the dictionary to which you are linking. If you do not enable Authenticate Active User, you will be prompted for a user name and password when you try to create the link.

When done defining the temporary link, click Create Link. Enter a valid user name and password, if prompted. Once created, your temporary link will be added to the Active Links list at the top of the SQL Link Manager.
