---
title: Ace Adsfindnexttable62
slug: ace_adsfindnexttable62
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsfindnexttable62.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: f3076e5cdf77c5ae8504592daf195833e0484a84
---

# Ace Adsfindnexttable62

AdsFindNextTable62

AdsFindNextTable62

Advantage Client Engine

| AdsFindNextTable62  Advantage Client Engine |  |  |  |  |

Finds the next table matching the file mask provided in a previous call to [AdsFindFirstTable62](ace_adsfindfirsttable62.md).

Syntax

UNSIGNED32 ENTRYPOINT AdsFindNextTable62 ( ADSHANDLE hConnect,

SIGNED32 lHandle,

UNSIGNED8 \*pucDDName,

UNSIGNED16 \*pusDDLen,

UNSIGNED8 \*pucFileName,

UNSIGNED16 \*pusFileLen );

Parameters

| hConnect (I) | Handle of connection. |
| lHandle (I) | Find handle from a call to AdsFindFirstTable. |
| pucDDName (O) | If the table found is in a linked dictionary, the name of the link is returned in this buffer. |
| pusDDLen (I/O) | Length of pucDDName on input, length of returned data on output. |
| pucFileName (O) | Next matching tablename is returned in this buffer. |
| pusFileLen (I/O) | Length of pucFileName on input, length of returned data on output. |

Special Return Codes

| AE\_NO\_FILE\_FOUND | No tables were found. |

Remarks

Use AdsFindNextTable62 to continue a search started with the [AdsFindFirstTable62](ace_adsfindfirsttable62.md) API.

Call [AdsFindClose](ace_adsfindclose.md) when your work with the find handle (lHandle) is complete.

Example

usLen = ADS\_MAX\_TABLE\_NAME;

usAliasLen = ADS\_MAX\_OBJECT\_NAME;

ulRetVal = AdsFindFirstTable62( hConn, aucTableMask,

aucDictionaryAlias, &usAliasLen,

aucTable, &usLen, &hFindHandle );

if ( (ulRetVal != AE\_NO\_FILE\_FOUND) && (ulRetVal != AE\_SUCCESS) )

return ulRetVal;

 

while ( ulRetVal != AE\_NO\_FILE\_FOUND )

{

 

// Do your work with aucDictionaryAlias and aucTable here...

 

// now get the next table

usLen = ADS\_MAX\_TABLE\_NAME;

usAliasLen = ADS\_MAX\_OBJECT\_NAME;

ulRetVal = AdsFindNextTable62( hConn, hFindHandle,

aucDictionaryAlias, &usAliasLen, aucTable, &usLen );

if ( (ulRetVal != AE\_NO\_FILE\_FOUND) && (ulRetVal != AE\_SUCCESS) )

return ulRetVal;

}

 

AdsFindClose( hConn, hFindHandle );

See Also

[AdsFindFirstTable](ace_adsfindfirsttable.md)

[AdsFindNextTable](ace_adsfindnexttable.md)

[AdsFindClose](ace_adsfindclose.md)

[AdsFindFirstTable62](ace_adsfindfirsttable62.md)
