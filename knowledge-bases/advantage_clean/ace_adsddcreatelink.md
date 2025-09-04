---
title: Ace Adsddcreatelink
slug: ace_adsddcreatelink
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddcreatelink.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 4602c89918b3b475904834c1925fd8238ed1fad5
---

# Ace Adsddcreatelink

AdsDDCreateLink

AdsDDCreateLink

Advantage Client Engine

| AdsDDCreateLink  Advantage Client Engine |  |  |  |  |

Creates a link to another data dictionary from the current database connection), optionally making the link a global link that is available to all users connected to the database.

Syntax

UNSIGNED32 AdsDDCreateLink( ADSHANDLE hDBConn,

UNSIGNED8 \*pucLinkAlias,

UNSIGNED8 \*pucLinkedDDPath,

UNSIGNED8 \*pucUserName,

UNSIGNED8 \*pucPassword,

UNSIGNED32 ulOptions );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucLinkAlias (I) | Name of the link to create. This name is used in SQL statements to reference the tables associated with the linked data dictionary. |
| pucLinkedDDPath (I) | Path to the data dictionary that will be linked to the connection passed in the hDBConn parameter. The path can be either a full UNC path or a relative path based on the connection path of hDBConn. |
| pucUserName (I) | User name to use for authentication with the data dictionary being linked to. This parameter is ignored if the ADS\_LINK\_AUTH\_ACTIVE\_USER option is specified in the ulOptions parameter. |
| pucPassword (I) | Password to use for authentication with the data dictionary being linked to. This parameter is ignored if the ADS\_LINK\_AUTH\_ACTIVE\_USER option is specified in the ulOptions parameter. |
| ulOptions (I) | Bit field for defining options for this link. The options can be ORed together. For example, ADS\_LINK\_GLOBAL | ADS\_LINK\_AUTH\_ACTIVE\_USER. The options are:  ADS\_DEFAULT: If no options are needed, this value (0) can be used.  ADS\_LINK\_GLOBAL: Specifies the link alias as available to all users connecting to this data dictionary. All information needed to re-create this link is stored in the data dictionary. By default, this option is turned off, and the link created is local to the current connection.  ADS\_LINK\_AUTH\_ACTIVE\_USER: Specifies that the user name and password of the current connection be used for authenticating to the linked data dictionary as well. This option is off by default so the pucUserName and pucPassword parameters would be used for authentication into the linked data dictionary regardless of the current connections user name and password.  ADS\_LINK\_PATH\_IS\_STATIC: This option can be specified in conjunction with the ADS\_LINK\_GLOBAL option. It determines whether the relative or full path of the linked data dictionary is stored in the current database. If the ADS\_LINK\_PATH\_IS\_STATIC option is specified, the full path of the linked data dictionary is stored in the data dictionary. It is suggested that the UNC path should be supplied in the pucLinkedDDPath parameter when this option is specified. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error will be returned if a local or global link with an identical alias already exists on the current connection. If creating a global link, this error will be returned if the link name is already used for other objects, such as tables, views or stored procedures, in the database. |

Remarks

This function creates a named link to another data dictionary on the current connection. The name can then be used in SQL statements to reference tables in the linked data dictionary. The permissions to the tables in the linked data dictionary are determined by the user name that is used to authenticate into the linked data dictionary.

If the link alias is made global, the link alias is available to all authorized users of the database. Access to the link can be controlled by granting or revoking user or group permissions to the link alias.

CREATE LINK permissions are required to create a new global link in the data dictionary. Non-global (local) links require no permissions to be created. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

Make a connection to the database MASTER.ADD, create a link to the ARCHIVE.ADD, and update a table in the MASTER database with values from a table in ARCHIVE database.

AdsConnect60( "n:\\MyData\\MASTER.ADD", ADS\_REMOTE\_SERVER, "User1",

"password", ADS\_DEFAULT, &hDBConn );

 

AdsDDCreateLink( hDBConn, "LinkA", "ARCHIVE.ADD", NULL, NULL,

ADS\_LINK\_AUTH\_ACTIVE\_USER );

 

AdsCreateSQLStatement( hDBConn, &hStmt );

 

AdsExecuteSQLDirect( hStmt,

"UPDATE Table1 SET LastDate = ( SELECT Max(LastDate) FROM LinkA.Table1 )",

NULL );

See Also

[AdsDDDropLink](ace_adsdddroplink.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.md)

[AdsDDFindNextObject](ace_adsddfindnextobject.md)

[AdsDDGetLinkProperty](ace_adsddgetlinkproperty.md)

[AdsDDModifyLink](ace_adsddmodifylink.md)

[AdsGetNumActiveLinks](ace_adsgetnumactivelinks.md)

[AdsGetActiveLinkInfo](ace_adsgetactivelinkinfo.md)

[sp\_CreateLink](master_sp_createlink.md)
