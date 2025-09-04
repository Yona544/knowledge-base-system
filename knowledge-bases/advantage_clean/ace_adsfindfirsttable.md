---
title: Ace Adsfindfirsttable
slug: ace_adsfindfirsttable
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adsfindfirsttable.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 261fd0236c54381fc369816e3da169ed24609245
---

# Ace Adsfindfirsttable

AdsFindFirstTable

AdsFindFirstTable

Advantage Client Engine

| AdsFindFirstTable  Advantage Client Engine |  |  |  |  |

Finds the first table matching the file mask

Syntax

UNSIGNED32 ENTRYPOINT AdsFindFirstTable ( ADSHANDLE hConnect,

UNSIGNED8 \*pucFileMask,

UNSIGNED8 \*pucFirstFile,

UNSIGNED16 \*pusFileLen,

SIGNED32 \*plHandle );

Parameters

| hConnect (I) | Connection handle. |
| pucFileMask (I) | File mask to use when searching for tables. |
| pucFirstFile (O) | First matching tablename is returned in this buffer. |
| pusFileLen (I/O) | Length of pucFirstFile on input, length of returned data on output. |
| plHandle (O) | Handle to use in subsequent calls to AdsFindNextTable. |

Special Return Codes

| AE\_NO\_FILE\_FOUND | No tables were found. |

Remarks

Use AdsFindFirstTable, in conjunction with [AdsFindNextTable](ace_adsfindnexttable.md) and [AdsFindClose](ace_adsfindclose.md), to search for either physical file names matching a given file mask (such as "\*.adt"), or to find "logical" table names in an Advantage Data Dictionary, where a "logical" table name is the name given to a table or a view in the data dictionary.

To find logical table names in an Advantage Data Dictionary, the hConnect parameter must be a database connection), and the pucFileMask parameter must be either NULL or an empty string. If you are not using a database connection or the pucFileMask is neither NULL nor an empty string, the API will try to find physical files matching the given file mask.

How the existence check for a file is done by Advantage can depend on many factors, including whether using a database connection) or free connection) and the Advantage server type to which you are connected. Those variations are discussed below:

Advantage Internet Server connections:

If a logical table exists in the data dictionary (when using a database connection)), this function will return AE\_SUCCESS (0). Otherwise, it is assumed no files exist, and AE\_NO\_FILE\_FOUND is returned.

Advantage Database Server and Advantage Local Server connections:

If a logical table exists in the data dictionary (when using a database connection)), this function will return AE\_SUCCESS (0). Otherwise, a non-Advantage, low-level file access function is called from the client to check for existence of a file matching the pucFileMask. If attempting to find a file on a server, this function cannot override normal access rights imposed by that server. If the client has access rights to a file matching the pucFileMask, and it exists, AE\_SUCCESS (0) will be returned. If no file matching the pucFileMask exists, or if the client does not have access rights to an existing file matching the pucFileMask, this function will return AE\_NO\_FILE\_FOUND.

If the function returns AE\_SUCCESS, the first file name will be returned in pucFirstFile and pusFileLen will contain the length of that file name. [AdsFindNextTable](ace_adsfindnexttable.md) can be used to retrieve the next file name. Call [AdsFindClose](ace_adsfindclose.md) when your work with the find handle (plHandle) is complete.

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

[AdsFindNextTable](ace_adsfindnexttable.md)

[AdsFindClose](ace_adsfindclose.md)

[AdsFindFirstTable62](ace_adsfindfirsttable62.md)

[AdsFindNextTable62](ace_adsfindnexttable62.md)
