---
title: Error 7087 Permission Not Granted For The Requested Operation
slug: error_7087_permission_not_granted_for_the_requested_operation
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: error_7087_permission_not_granted_for_the_requested_operation.htm
source: Advantage CHM
tags:
  - error
checksum: c0fd23ddd4c3c5caae8a5da509b0b6f5421e562c
---

# Error 7087 Permission Not Granted For The Requested Operation

7087 Permission not granted for the requested operation

7087 Permission not granted for the requested operation

Advantage Error Guide

| 7087 Permission not granted for the requested operation  Advantage Error Guide |  |  |  |  |

Problem: An operation on a database table failed because it requires permission not granted to the user performing the operation. Some of the possible causes are:

- Attempting to update an existing row in the table but the UPDATE permission was not granted on the table or not granted on some columns to be modified,

- Attempting to insert a new row in the table but the INSERT permission was not granted on the table

- Attempting to delete a row in a table but the DELETE permission was not granted on the table

- Attempting to set a filter or scope on a table but the filter expression or the scope index contains columns that the user has no READ permission

Solution: If the requested operation is necessary, the database administrator must grant the user the appropriate permission.

Problem: An attempt to open a free table) failed because access to free table) is restricted on this database connection).

Solution: If the requested operation is necessary, the application must not set the CheckFreeTableAccess option to true when connecting to the data dictionary.
