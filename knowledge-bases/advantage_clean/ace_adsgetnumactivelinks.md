---
title: Ace Adsgetnumactivelinks
slug: ace_adsgetnumactivelinks
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetnumactivelinks.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 2c361d440ce1415a91db1caef5e7e14a6eecfb8b
---

# Ace Adsgetnumactivelinks

AdsGetNumActiveLinks

AdsGetNumActiveLinks

Advantage Client Engine

| AdsGetNumActiveLinks  Advantage Client Engine |  |  |  |  |

Retrieves the number of links active on the current connection.

Syntax

UNSIGNED32 AdsGetNumActiveLinks( ADSHANDLE hDBConn,

UNSIGNED16 \*pusNumLinks );

Parameters

| hDBConn (I) | Handle of a database connection). |
| pusNumLinks (O) | Returns the number of links that are active on the current connection. |

Remarks

This function is used to retrieve the number of active links on the current connection. A global link that is stored in the data dictionary is not active until it is used in an SQL statement on the current connection.

Example

The execution of the following SQL statement creates an implicit link to the ARCHIVE database so the AdsGetNumActiveLinks should return 1 in the output.

AdsConnect60( "n:\\MyData\\MASTER.ADD", ADS\_REMOTE\_SERVER, "User1",

"password", ADS\_DEFAULT, &hDBConn );

 

AdsCreateSQLStatement( hDBConn, &hStmt );

 

AdsExecuteSQLDirect( hStmt, "SELECT Max(LastDate) FROM \"n:\\MyData\\ARCHIVE\\ARCHIVE.ADD\".Table1",

&hCursor );

 

// usNumLinks should be 1

AdsGetNumActiveLinks( hDBConn, &usNumLinks );

See Also

[AdsDDCreateLink](ace_adsddcreatelink.md)

[AdsDDDropLink](ace_adsdddroplink.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.md)

[AdsDDFindNextObject](ace_adsddfindnextobject.md)

[AdsDDGetLinkProperty](ace_adsddgetlinkproperty.md)

[AdsDDModifyLink](ace_adsddmodifylink.md)

[AdsGetActiveLinkInfo](ace_adsgetactivelinkinfo.md)
