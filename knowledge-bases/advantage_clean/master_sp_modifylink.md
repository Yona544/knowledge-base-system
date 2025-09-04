---
title: Master Sp Modifylink
slug: master_sp_modifylink
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_modifylink.htm
source: Advantage CHM
tags:
  - master
checksum: 8e1f89ce0c72d42819f19658a1eea356e5a82799
---

# Master Sp Modifylink

sp\_ModifyLink

sp\_ModifyLink

Advantage SQL Engine

| sp\_ModifyLink  Advantage SQL Engine |  |  |  |  |

Modifies an existing global data dictionary link.

Syntax

sp\_ModifyLink(

Name,CHARACTER,200,

Dictionary,CHARACTER,515,

StaticPath,LOGICAL,

AuthenticateActiveUser,LOGICAL,

UserName,CHARACTER,50,

Password,CHARACTER,20 )

Parameters

| Name (I) | Name of the existing global link to modify. |
| Dictionary (I) | Path to the data dictionary that will be linked to the active connection. The path can be either a full UNC path or a relative path based on the connection path of current connection. |
| StaticPath (I) | Specifies whether the relative or full path of the linked data dictionary is stored in the current database. If True the full path of the linked data dictionary is stored in the data dictionary. It is suggested that the UNC path should be supplied in the data dictionary parameter when this option is specified. |
| AuthenticateActiveUser (I) | Specifies that the user name and password of the current connection be used for authenticating to the linked data dictionary as well. When False the UserName and Password parameters will be used for authentication into the linked data dictionary regardless of the current connections user name and password. |
| UserName (I) | User name to use for authentication with the data dictionary being linked to. This parameter is ignored if the AuthenticateActiveUser is True. |
| Password (I) | Password to use for authentication with the data dictionary being linked to. This parameter is ignored if the AuthenticateActiveUser is True. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error will be returned if the global link with the given alias cannot be found. |

Remarks

sp\_ModifyLink modifies an existing global link to another data dictionary on the current connection. The primary benefit to using this procedure over deleting and re-creating the link is that it maintains existing permissions on the link object. This procedure can only be used to modify global links; local link objects cannot be modified.

See Also

[sp\_CreateLink](master_sp_createlink.md)

[sp\_DropLink](master_sp_droplink.md)
