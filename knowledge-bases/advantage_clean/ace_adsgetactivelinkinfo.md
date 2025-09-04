---
title: Ace Adsgetactivelinkinfo
slug: ace_adsgetactivelinkinfo
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsgetactivelinkinfo.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 77b2b2e2f8e941a2e2451e14ec6caf201e015894
---

# Ace Adsgetactivelinkinfo

AdsGetActiveLinkInfo

AdsGetActiveLinkInfo

Advantage Client Engine

| AdsGetActiveLinkInfo  Advantage Client Engine |  |  |  |  |

Retrieves the detail information about an active link on the current connection.

Syntax

UNSIGNED32 AdsGetActiveLinkInfo( ADSHANDLE hDBConn,

UNSIGNED16 usLinkNum,

UNSIGNED8 \*pucLinkInfo,

UNSIGNED16 \*pusBufferLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| usLinkNum (I) | The ordinal number of the link to retrieve detail information about. The number is one-based. |
| pucLinkInfo (O) | Returns the detail information about the link in this buffer. |
| pusBufferLen (I/O) | On input, specifies the length of the buffer pointed to by pucLinkInfo. On output, returns the length of the detail information copied into the buffer. |

Remarks

This function is used to retrieve the detail information about an active link on the current connection. The information returned is the link alias, if there is one, the user name used to authenticate into the linked data dictionary, and the path of the linked data dictionary. The information is delimited using semi-colons. Following is some sample link detail information:

"Link1;User1;\\Server1\Share1\Data\MyData.ADD"

";;n:\ShareData\MyData.ADD"

Example

This code segment will drop all active links on the current connection.

UNSIGNED8 aucLinkInfo[500];

UNSIGNED16 usBuffLen = sizeof( aucLinkInfo );

 

while ( AE\_SUCCESS == AdsGetActiveLinkInfo( hDBConn, 1, aucLinkInfo, &usBuffLen ))

{

 

/\* Find the link alias or path \*/

if ( aucLinkInfo[0] != ';' )

{

SIGNED8 \*pcLinkEnd = strchr( (SIGNED8 \*)aucLinkInfo, ';' );

 

\*pcLinkEnd = 0;

 

ulRetVal = AdsDDDropLink( hDBConn, aucLinkInfo, FALSE );

}

else

{

/\* Link is not named, use path. \*/

SIGNED8 \*pcLinkPath = strchr( (SIGNED8 \*)aucLinkInfo + 1, ';' );

 

ulRetVal = AdsDDDropLink( hDBConn, pcLinkPath + 1, FALSE );

}

 

if ( ulRetVal != AE\_SUCCESS )

break;

 

usBuffLen = sizeof( aucLinkInfo );

}

See Also

[AdsDDCreateLink](ace_adsddcreatelink.md)

[AdsDDDropLink](ace_adsdddroplink.md)

[AdsDDGrantPermission](ace_adsddgrantpermission.md)

[AdsDDRevokePermission](ace_adsddrevokepermission.md)

[AdsDDFindFirstObject](ace_adsddfindfirstobject.md)

[AdsDDFindNextObject](ace_adsddfindnextobject.md)

[AdsDDGetLinkProperty](ace_adsddgetlinkproperty.md)

[AdsDDModifyLink](ace_adsddmodifylink.md)

[AdsGetNumActiveLinks](ace_adsgetnumactivelinks.md)
