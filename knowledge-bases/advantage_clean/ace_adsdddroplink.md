---
title: Ace Adsdddroplink
slug: ace_adsdddroplink
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsdddroplink.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 10a945cf6dfdc4a6fb480ea525e2096b6a96ebd8
---

# Ace Adsdddroplink

AdsDDDropLink

AdsDDDropLink

Advantage Client Engine

| AdsDDDropLink  Advantage Client Engine |  |  |  |  |

Removes either a local link or a global link from current connection.

Syntax

UNSIGNED32 AdsDDDropLink( ADSHANDLE hDBConn,

UNSIGNED8 \*pucLinkedDD,

UNSIGNED16 usDropGlobal );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pucLinkedDD (I) | The name or path of the link to drop. If the path is given, the first link matching the given path will be dropped. |
| usDropGlobal (I) | True to remove the global link alias from the data dictionary. If this parameter is True, the pucLinkedDD parameter must specify the link alias in the data dictionary. |

Special Return Codes

| AE\_INVALID\_OBJECT\_NAME | This error may be returned if the usDropGlobal parameter is True and the specified link cannot be found in the data dictionary. |

Remarks

This function can be used to either drop an active link from the current connection or remove a global link from the data dictionary. Since the database server maintains information on the active links, dropping active links from the current connection will free some resources consumed by the server.

DROP permissions on the link are required to drop a link from the data dictionary. See [Advantage Data Dictionary User Permissions](master_advantage_data_dictionary_user_permissions.md) for more information.

Note This function can be called inside a transaction, but will not be part of the transaction. Any changes it makes cannot be rolled back.

Example

The execution of the following SQL statement creates an implicit link to the ARCHIVE database. The implicit link is then dropped.

AdsConnect60( "n:\\MyData\\MASTER.ADD", ADS\_REMOTE\_SERVER, "User1",

"password", ADS\_DEFAULT, &hDBConn );

 

AdsCreateSQLStatement( hDBConn, &hStmt );

 

AdsExecuteSQLDirect( hStmt, "SELECT Max(LastDate) FROM \"n:\\MyData\\ARCHIVE\\ARCHIVE.ADD\".Table1",

&hCursor );

 

AdsDDDropLink( hDBConn, "n:\\MyData\\ARCHIVE\\ARCHIVE.ADD", FALSE );

See Also

[AdsDDCreateLink](ace_adsddcreatelink.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.md)

[AdsDDFindNextObject](ace_adsddfindnextobject.md)

[AdsDDGetLinkProperty](ace_adsddgetlinkproperty.md)

[AdsDDModifyLink](ace_adsddmodifylink.md)

[AdsGetNumActiveLinks](ace_adsgetnumactivelinks.md)

[AdsGetActiveLinkInfo](ace_adsgetactivelinkinfo.md)

[sp\_DropLink](master_sp_droplink.md)
