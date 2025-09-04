---
title: Ace Adsfindnexttable
slug: ace_adsfindnexttable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsfindnexttable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 82bc4adf54af21ad95f951dc9bd9807a0b6faaf2
---

# Ace Adsfindnexttable

AdsFindNextTable

AdsFindNextTable

Advantage Client Engine

| AdsFindNextTable  Advantage Client Engine |  |  |  |  |

Finds the next table matching the file mask provided in a previous call to [AdsFindFirstTable](ace_adsfindfirsttable.md).

Syntax

UNSIGNED32 ENTRYPOINT AdsFindNextTable( ADSHANDLE hConnect,

SIGNED32 lHandle,

UNSIGNED8 \*pucFileName,

UNSIGNED16 \*pusFileLen );

Parameters

| hConnect (I) | Handle of connection. |
| lHandle (I) | Find handle from a call to AdsFindFirstTable. |
| pucFileName (O) | Next matching tablename is returned in this buffer. |
| pusFileLen (I/O) | Length of pucFileName on input, length of returned data on output. |

Special Return Codes

| AE\_NO\_FILE\_FOUND | No tables were found. |

Remarks

Use AdsFindNextTable to continue a search started with the [AdsFindFirstTable](ace_adsfindfirsttable.md) API.

Call [AdsFindClose](ace_adsfindclose.md) when your work with the find handle (lHandle) is complete.

Example

usLen = ADS\_MAX\_TABLE\_NAME;

strcpy( (char\*)aucTableMask, "x:\\data\\\*.adt" );

ulRetVal = AdsFindFirstTable( hConn, aucTableMask, aucTable,

&usLen, &hFindHandle );

if ( (ulRetVal != AE\_NO\_FILE\_FOUND) && (ulRetVal != AE\_SUCCESS) )

return ulRetVal;

 

while ( ulRetVal != AE\_NO\_FILE\_FOUND )

{

 

// Do your work with the tablename, which is now in the aucTable buffer.

 

// now get the next table

usLen = ADS\_MAX\_TABLE\_NAME;

ulRetVal = AdsFindNextTable( hConn, hFindHandle,

aucTable, &usLen );

if ( (ulRetVal != AE\_NO\_FILE\_FOUND) && (ulRetVal != AE\_SUCCESS) )

return ulRetVal;

}

 

AdsFindClose( hConn, hFindHandle );

See Also

[AdsFindFirstTable](ace_adsfindfirsttable.md)

[AdsFindClose](ace_adsfindclose.md)

[AdsFindFirstTable62](ace_adsfindfirsttable62.md)

[AdsFindNextTable62](ace_adsfindnexttable62.md)
