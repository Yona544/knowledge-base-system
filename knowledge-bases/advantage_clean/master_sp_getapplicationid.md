---
title: Master Sp Getapplicationid
slug: master_sp_getapplicationid
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_getapplicationid.htm
source: Advantage CHM
tags:
  - master
checksum: 23c3bb17423d6e5e4451e39eeb81737308592d5a
---

# Master Sp Getapplicationid

sp\_GetApplicationID

sp\_GetApplicationID

Advantage SQL Engine

| sp\_GetApplicationID  Advantage SQL Engine |  |  |  |  |

Retrieve the current connection's Application ID.

Syntax

sp\_GetApplicationID( )

Parameters

None

Output

The sp\_GetApplicationID procedure returns a result set of one column and one row containing the Application ID in a memo field.

Remarks

The sp\_GetApplicationID system procedure returns the Application ID of the connection that executed it. The Application ID is initialized to be the file name of the application (executable) that created the connection.

Note Only ACE based clients initialize the Application ID.

See Also

[sp\_SetApplicationID](master_sp_setapplicationid.md)
