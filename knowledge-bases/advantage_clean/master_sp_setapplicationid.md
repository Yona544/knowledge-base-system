---
title: Master Sp Setapplicationid
slug: master_sp_setapplicationid
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_setapplicationid.htm
source: Advantage CHM
tags:
  - master
checksum: ffffd28b46d2ea08210ac7941ce57c6b0062a212
---

# Master Sp Setapplicationid

sp\_SetApplicationID

sp\_SetApplicationID

Advantage SQL Engine

| sp\_SetApplicationID  Advantage SQL Engine |  |  |  |  |

Set the current connection's Application ID.

Syntax

sp\_SetApplicationID( ApplicationID, MEMO )

Parameters

| ApplicationID (I) | New Application ID to be used for the current connection. |

Output

None

Remarks

The sp\_SetApplicationID system procedure sets the Application ID of the connection that executed it. The Application ID is initialized to be the file name of the application (executable) that created the connection.

Note Only ACE based clients initialize the Application ID.

See Also

[sp\_GetApplicationID](master_sp_getapplicationid.md)
