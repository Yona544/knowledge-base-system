---
title: Devguide Understanding Groups
slug: devguide_understanding_groups
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_understanding_groups.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 5f4f5c455834f0c847a4fadbc32861024d37fa09
---

# Devguide Understanding Groups

Understanding Groups

     Understanding Groups

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Understanding Groups  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

A group is like a user template for access rights. You begin by creating a group. You then grant to that group all rights required by the group's members. You then assign individual users to the group. By default, a user inherits all rights associated with the groups to which they belong.

Groups are especially valuable when you have multiple users and want to easily administer their rights. Imagine, for example, that you have created a group and granted all of its members read and write (update, insert, and delete) access to all objects in a data dictionary. Later, we add a new objecta view, for exampleto the data dictionary. By granting rights for the view to the group, all that group's members immediately gain rights to the view also. Without the group, you would have to modify the rights of each individual user needing access to the view.

The benefits of using groups increase even further when you have two or more types of users of your database. For example, some applications have three levels of users: those who can only view data, those who can view and add data, and those who have full access (including create, grant alter, and drop privileges, where create is a dictionary-level privilege).

To accommodate this scenario, you begin by creating three groups, with each group being granted the rights associated with the type of users who will be members. Then, for each user you add to the data dictionary, you assign them to whichever group they belong.

Actually, you can get pretty fancy about how you use groups. For example, a given user can belong to two or more groups. A user's rights are equal to the sum of the rights conveyed to the groups to which they belong.
