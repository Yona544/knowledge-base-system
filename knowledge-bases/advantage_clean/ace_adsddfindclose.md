---
title: Ace Adsddfindclose
slug: ace_adsddfindclose
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddfindclose.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 0c7038605597cbbfbb6ab0488565ddb53b385e68
---

# Ace Adsddfindclose

AdsDDFindClose

AdsDDFindClose

Advantage Client Engine

| AdsDDFindClose  Advantage Client Engine |  |  |  |  |

Terminates an active search in the data dictionary and free the resources that was allocated for the search.

Syntax

UNSIGNED32 AdsDDFindClose( ADSHANDLE hDBConn, ADSHANDLE hFindHandle );

Parameters

| hDBConn (I) | Handle of a database connection). |
| hFindHandle (I) | Find handle that was returned by [AdsDDFindFirstObject](ace_adsddfindfirstobject.md). |

Special Return Codes

None.

Remarks

AdsDDFindClose is used to terminate a search initiated by [AdsDDFindFirstObject](ace_adsddfindfirstobject.md).

Example

Find all index files that are associated with the "Customer Information" table.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usBufferSize = sizeof( aucFileName );

if ( AE\_SUCCESS == AdsDDFindFirstObject( hDD, ADS\_DD\_INDEX\_FILE\_OBJECT,

"Customer Information", aucFileName,

&usBufferSize ))

{

do

{

printf( "%s\n", aucFileName );

usBufferSize = sizeof( aucFileName );

}

while ( AE\_SUCCESS == AdsDDFindNextObject( hDD, aucFileName, &usBufferSize ));

AdsDDFindClose( hDD );

}

See Also

[AdsDDFindFirstObject](ace_adsddfindfirstobject.md)

[AdsDDFindNextObject](ace_adsddfindnextobject.md)

[AdsConnect60](ace_adsconnect60.md)
