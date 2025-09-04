---
title: Master Sp Createlink
slug: master_sp_createlink
product: Advantage Database Server
component: Advantage
version: "12"
category: Reference
original_path_html: master_sp_createlink.htm
source: Advantage CHM
tags:
  - master
checksum: be6ff47e8a4e9ba922a13521c57274ea87a3aece
---

# Master Sp Createlink

sp\_CreateLink

sp\_CreateLink

Advantage SQL Engine

| sp\_CreateLink  Advantage SQL Engine |  |  |  |  |

Creates a link to another data dictionary from the current database connection, optionally making the link a global link that is available to all users connected to the database.

Syntax

sp\_CreateLink(

Name,CHARACTER,200,

Dictionary,CHARACTER,515,

Global,LOGICAL,

StaticPath,LOGICAL,

AuthenticateActiveUser,LOGICAL,

UserName,CHARACTER,50,

Password,CHARACTER,20 )

Parameters

| Name (I) | Name of the link to create. This name is used in SQL statements to reference the tables associated with the linked data dictionary. |
| Dictionary (I) | Path to the data dictionary that will be linked to the active connection. The path can be either a full UNC path or a relative path based on the connection path of current connection. |
| Global (I) | Specifies the link alias as available to all users connecting to this data dictionary. All information needed to re-create this link is stored in the data dictionary. This option is only valid if the current connection has administrative permissions. By default, this option is turned off, and the link created is local to the current connection. |
| StaticPath (I) | This option can be only True when the Global parameter is also True. It determines whether the relative or full path of the linked data dictionary is stored in the current database. If True the full path of the linked data dictionary is stored in the data dictionary. It is suggested that the UNC path should be supplied in the Dictionary parameter when this option is specified. |
| AuthenticateActiveUser (I) | Specifies that the user name and password of the current connection be used for authenticating to the linked data dictionary as well. When False the UserName and Password parameters will be used for authentication into the linked data dictionary regardless of the current connections user name and password. |
| UserName (I) | User name to use for authentication with the data dictionary being linked to. This parameter is ignored if the AuthenticateActiveUser is True. |
| Password (I) | Password to use for authentication with the data dictionary being linked to. This parameter is ignored if the AuthenticateActiveUser is True. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error will be returned if a local or global link with an identical alias already exists on the current connection. If creating a global link, this error will be returned if the link name is already used for other objects, such as tables, views or stored procedures, in the database. |

Remarks

This function creates a named link to another data dictionary on the current connection. The name can then be used in SQL statements to reference tables in the linked data dictionary. The permissions to the tables in the linked data dictionary are determined by the user name that is used to authenticate into the linked data dictionary.

If the link alias is made global, the link alias is available to all authorized users of the database. Granting or revoking user or group permissions to the link alias can control access to the link.

Example

Make a connection to the database MASTER.ADD, create a link to the ARCHIVE.ADD, and update a table in the MASTER database with values from a table in ARCHIVE database.

EXECUTE PROCEDURE sp\_CreateLink(

LinkA,

ARCHIVE.ADD ,

FALSE,

FALSE,

TRUE,

NULL,

NULL );

 

UPDATE Table1 SET LastDate = ( SELECT Max(LastDate) FROM LinkA.Table1 );

See Also

[sp\_DropLink](master_sp_droplink.md)

[sp\_ModifyLink](master_sp_modifylink.md)
