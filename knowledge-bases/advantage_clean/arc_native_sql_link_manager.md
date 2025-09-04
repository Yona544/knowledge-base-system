---
title: Arc Native Sql Link Manager
slug: arc_native_sql_link_manager
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_native_sql_link_manager.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 27d4d49f423ead49fea3c6775021e3dbfffb8d54
---

# Arc Native Sql Link Manager

SQL Link Manager

SQL Link Manager

Advantage Data Architect

| SQL Link Manager  Advantage Data Architect |  |  |  |  |

The SQL Link Manger is used to create temporary data dictionary links for testing. This feature is only available when using Advantage Data Dictionaries. The links are not added to the data dictionary and will be destroyed when the SQL Utility disconnects.

Active Links

This list box displays all current links active for the SQL Utility. Each link includes an alias if one has been set, the path to the linked data dictionary, and the user name for the link if it is not the current user.

Drop Link

This button closes a link.

Link Alias (optional)

This property specifies an optional alias that can be assigned to a new data dictionary link when it is created. This alias can be used directly in an SQL statement instead of the path to the data dictionary.

SELECT \* FROM myalias.mytable;

Data Dictionary (required)

This property specifies the data dictionary to create a link to. If an alias is not specified then the path will be required in the SQL statement using dot notation.

SELECT \* FROM "\\server\share\data\data.add".mytable

Browse

This button allows the user to browse for the data dictionary to link to.

Authenticate Active User

When enabled this property specifies that the current user name and password should be used for authenticating into the linked data dictionary.

Create Link

Creates the link.

Close

This button closes the Native SQL Link Manager.
