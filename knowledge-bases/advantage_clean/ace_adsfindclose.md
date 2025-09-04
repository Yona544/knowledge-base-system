---
title: Ace Adsfindclose
slug: ace_adsfindclose
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsfindclose.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: f58565779c570a5bbcf85f7a50d32da6e1b2449a
---

# Ace Adsfindclose

AdsFindClose

AdsFindClose

Advantage Client Engine

| AdsFindClose  Advantage Client Engine |  |  |  |  |

Close a find handle and free all resources associated with it

Syntax

UNSIGNED32 ENTRYPOINT AdsFindClose( ADSHANDLE hConnect, SIGNED32 lHandle );

Parameters

| hConnect (I) | Handle of connection. |
| lHandle (I) | Find handle to close. |

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

[AdsFindNextTable](ace_adsfindnexttable.md)

[AdsFindFirstTable62](ace_adsfindfirsttable62.md)

[AdsFindNextTable62](ace_adsfindnexttable62.md)
