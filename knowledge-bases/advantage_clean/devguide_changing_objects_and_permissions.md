---
title: Devguide Changing Objects And Permissions
slug: devguide_changing_objects_and_permissions
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_changing_objects_and_permissions.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 49ff077d8a42bb1cef2db4938b04401e234a3301
---

# Devguide Changing Objects And Permissions

Changing Objects and Permissions

     Changing Objects and Permissions

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Changing Objects and Permissions  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

Creating users and groups, and enabling user rights checking, are often the final steps that you will take in the testing and deployment of a database application. The creation of users and groups, and the enabling of rights checking were performed in this chapter since these issues are closely related to the creation and security of a data dictionary.

There is a problem, however. You have not completed the construction of this data dictionary. You will add new objects to this data dictionary in later chapters of this book, including stored procedures and views.

Each time you add a new object to this data dictionary, you also need to update group rights and/or user access rights in order to provide access to the added object. By comparison, if you wait until after all of the data dictionary's objects are created before enabling user rights checking, you only have to configure access rights once.

Here is another way to put it. By enabling check user rights at this stage in the data dictionary's development, we have increased your work. On the other hand, this approach also allows us to stress the importance of granting rights as new objects are created in later chapters. In the end, we felt that this lesson was worth the inconvenience.

In your own data dictionaries, save yourself time and configure object rights as a last step towards security testing and deployment.
