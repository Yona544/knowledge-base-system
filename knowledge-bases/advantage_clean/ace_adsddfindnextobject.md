---
title: Ace Adsddfindnextobject
slug: ace_adsddfindnextobject
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsddfindnextobject.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 5a0d9c9734778be55a61708893830e2a1a0c1d12
---

# Ace Adsddfindnextobject

AdsDDFindNextObject

AdsDDFindNextObject

Advantage Client Engine

| AdsDDFindNextObject  Advantage Client Engine |  |  |  |  |

Continues the search initiated by [AdsDDFindFirstObject](ace_adsddfindfirstobject.md) and retrieves the name of the next object passing the search condition from the data dictionary.

Syntax

UNSIGNED32 AdsDDFindNextObject( ADSHANDLE hDBConn,

ADSHANDLE hFindHandle,

UNSIGNED8 \*pucObjectName,

UNSIGNED16 \*pusObjectNameLen );

Parameters

| hDBConn (I) | Handle of a database connection). |
| hFindHandle (I) | Find handle that was returned by [AdsDDFindFirstObject](ace_adsddfindfirstobject.md). |
| pucObjectName (O) | Returns the name of next object in the data dictionary. The length of the object name has a maximum length of ADS\_MAX\_OBJECT\_NAME\_LEN. |
| pusObjectNameLen (I/O) | On input, specifies the size of the buffer pointed to by the pucObjectName. On output, returns the length of the object name returned in pucObjectName. |

Special Return Codes

| AE\_NO\_OBJECT\_FOUND | No additional object matching the specified condition was found in the data dictionary. |

Remarks

AdsDDFindNextObject is used in conjunction with [AdsDDFindFirstObject](ace_adsddfindfirstobject.md) to retrieve the names of the objects matching the search condition from the data dictionary. When names of all objects matching the searching condition have been retrieved, the function returns AE\_NO\_OBJECT\_FOUND.

See [AdsDDFindFirstObject](ace_adsddfindfirstobject.md) for information on types of objects that can be searched.

Example

Find all index files that are associated with the "Customer Information" table.

AdsConnect60( "n:\\MyData\\myData.ADD", ADS\_REMOTE\_SERVER, "ADSSYS", NULL, ADS\_DEFAULT, &hDD );

usBufferSize = (UNSIGNED16)sizeof( aucFileName );

if ( AE\_SUCCESS == AdsDDFindFirstObject( hDD, ADS\_DD\_INDEX\_FILE\_OBJECT,

"Customer Information", aucFileName,

&usBufferSize, &hFindHandle ))

{

do

{

printf( "%s\n", aucFileName );

usBufferSize = (UNSIGNED16)sizeof( aucFileName );

}

while ( AE\_SUCCESS == AdsDDFindNextObject( hDD, hFindHandle, aucFileName, &usBufferSize ));

}

 

/\* No need to call AdsDDFindClose since we are closing the DD. \*/

AdsDisconnect( hDD );

See Also

[AdsDDFindFirstObject](ace_adsddfindfirstobject.md)

[AdsDDFindClose](ace_adsddfindclose.md)

[AdsConnect60](ace_adsconnect60.md)
