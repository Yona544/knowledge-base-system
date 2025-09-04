---
title: Devguide Getting User And Group Information
slug: devguide_getting_user_and_group_information
product: Advantage Database Server
component: Developer’s Guide
version: "12"
category: Reference
original_path_html: devguide_getting_user_and_group_information.htm
source: Advantage CHM
tags:
  - devguide
  - developers-guide
checksum: 30812ba7a2f0a96e22e14dbcd01fc62552638630
---

# Devguide Getting User And Group Information

Getting User and Group Information

     Getting User and Group Information

Advantage Database Server v8.1: A Developers Guide

by Cary Jensen and Loy Anderson

  © 2007 Cary Jensen and Loy Anderson. All rights reserved.

| Getting User and Group Information  Advantage Database Server v8.1: A Developers Guide  by Cary Jensen and Loy Anderson    © 2007 Cary Jensen and Loy Anderson. All rights reserved. |  |  |  |  |

There are five tables that contain information about users, groups, and permissions: system.users, system.usergroups, system.usergroupmembers, system.permissions, and system.effectivepermissions. With the exception of the system.permissions and system.effectivepermissions tables, you must be connected to the data dictionary using the ADSSYS account or a user account with ALTER or DROP (or WITH GRANT) user or group permissions to access this information.

You use the system.users table to retrieve one record for each user defined in the data dictionary. The columns in this table provide you with the user's name, description, and whether or not the user is enabled for Internet access. (ADSSYS is not included in this table.) The following query returns the names of the users defined for the connected dictionary:

SELECT Name FROM system.users

The system.usergroups table contains one record for each group defined for your data dictionary. Columns returned in this result set include the group name and description. The following query demonstrates how to retrieve the names of your data dictionary's groups:

SELECT Name FROM system.usergroups

To discover which groups your data dictionary's users are assigned to, you query the system.usergroupmembers table. This table has one record for each group to which each user belongs. (Recall that a given user may be a member of zero or more groups.) There are only two fields in this group: Name and Group\_Name.

You use the system.permissions table to discover the names of objects, object type, name of user or group with access rights, object parent (when applicable), and rights conveyed. This table does not include inherited permissions. If you want to retrieve all permissions, including inherited permissions, use system.effectivepermissions. The values for the object type field in this table are codes. These codes are shown in Table 14-7.
