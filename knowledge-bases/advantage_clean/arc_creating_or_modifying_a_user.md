---
title: Arc Creating Or Modifying A User
slug: arc_creating_or_modifying_a_user
product: Advantage Database Server
component: Advantage Data Architect
version: "12"
category: API
original_path_html: arc_creating_or_modifying_a_user.htm
source: Advantage CHM
tags:
  - arc
  - advantage-data-architect
checksum: 33c29502e9a46ac23d17c4cc7c6ad14280244311
---

# Arc Creating Or Modifying A User

Creating or Modifying a User

Creating or Modifying a User

Advantage Data Architect

| Creating or Modifying a User  Advantage Data Architect |  |  |  |  |

To create or modify a database user, open a database. See [Opening a Database](arc_opening_a_database2.md) for details. You must login to the database as a user with CREATE USER or ALTER permissions on the specific user in order to add or modify users in a database.

To add a new user, right-click the USERS icon and select Create.

To modify user properties, from the tree view within the Connection Repository, right-click the User's name icon and select Properties.

User Property Field Descriptions

Name (required)

Name of the user.

Password (optional)

Password for the user.

Confirm Password (optional, unless password specified, then required)

Confirmation of user password.

Disable User (optional)

Enables or disables the user's login rights.

Enable Internet Access (optional)

Enables or disables Internet access for the user.

Group Membership (optional)

Click this option to [add or update user membership in a group](arc_adding_removing_users_to_from_a_group.md). Select which groups the user should be a member of. All rights in the group will be given to the user.

Replicate (optional)

Configure this new users properties based on an existing users properties.

Permissions (optional)

Click this option to modify the users permissions

Description (optional)

A description for the user.

Create

Creates the new user. Resets the dialog so another user can be entered.

Cancel/Close

Cancels any input or changes and exits the screen.
