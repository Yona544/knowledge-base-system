---
title: Ace Adscheckexistence
slug: ace_adscheckexistence
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adscheckexistence.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 553810a5b24cc1f0306f704c72dea10125a4a198
---

# Ace Adscheckexistence

AdsCheckExistence

AdsCheckExistence

Advantage Client Engine

| AdsCheckExistence  Advantage Client Engine |  |  |  |  |

Checks for existence of a file.

Syntax

| UNSIGNED32 | AdsCheckExistence (ADSHANDLE hConnect,  UNSIGNED8 \*pucFilename,  UNSIGNED16 \*pusOnDisk); |

Parameters

| hConnect (I) | Handle of an Advantage Client Engine connection, or zero to let the Advantage Client Engine handle the connection. |
| pucFilename (I) | Filename to check for existence. |
| pusOnDisk (O) | True if the file exists, else False. |

Remarks

AdsCheckExistence checks for existence of a file (any file, not just a table) named pucFilename. How the existence check is done by Advantage depends on many factors. These factors include whether or not you are using a database connection) or free connection), whether you are checking for a table that is already open, or checking for a table or some other file. It also depends upon the Advantage server type to which you are connected. Those server type variations are discussed below:

Advantage Internet Server connections:

If a table name is specified, and that table exists in the data dictionary (when using a database connection), or if that table is already open on the current connection, this function will return True in the pusOnDisk parameter. Otherwise, it is assumed the specified file does not exist, and False is returned in the pusOnDisk parameter.

Advantage Database Server and Advantage Local Server connections:

If a table name is specified, and that table exists in the data dictionary (when using a database connection), or if that table is already open on the current connection, this function will return True in the pusOnDisk parameter. Otherwise, a non-Advantage, low-level file access function is called from the client to check for existence of the specified file. If checking for file existence of a file on a server, this function cannot override normal access rights imposed by that server. If the client has access rights to the specified file, and it exists, True will be returned in the pusOnDisk parameter. If the specified file does not exist, or if the client does not have access rights to the specified file that does exist, this function will return False in the pusOnDisk parameter.

Example

None.

See Also

[AdsOpenTable](ace_adsopentable.md)

[AdsConnect](ace_adsconnect.md)
