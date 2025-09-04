---
title: Devguide Data Dictionary Management
slug: devguide_data_dictionary_management
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_data_dictionary_management.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: a730a45bac43ee64963c0696c543e4a271603c05
---

# Devguide Data Dictionary Management

Data Dictionary Management

     Data Dictionary Management

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Data Dictionary Management  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

The system stored procedures in the data dictionary management category permit you to configure a data dictionary and its various objects. These procedures can be called from the ADSSYS account or any user account with sufficient permissions.

A few of these procedures are designed to affect the data dictionary as a whole. For example, you use sp\_ModifyDatabase to change the properties of your current data dictionary. Likewise, you use sp\_DisableTriggers and sp\_EnableTriggers to disable or enable all triggers in the data dictionary, respectively.

Most all of the remaining procedures in this category are designed to add objects to the data dictionary, create new objects, modify existing objects, or remove (drop) objects from the data dictionary. For example, you use sp\_AddTableToDatabase to bind a free table to the data dictionary. On the other hand, sp\_CreateUser and sp\_DropUser, allow you to create and remove users, respectively.

The list of system stored procedures that you use to manage your data dictionaries are listed in Table 14-13.
