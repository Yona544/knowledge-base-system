---
title: Ace Adssetsearchpath
slug: ace_adssetsearchpath
product: Advantage Database Server
component: Advantage Client Engine
version: "12"
category: API
original_path_html: ace_adssetsearchpath.htm
source: Advantage CHM
tags:
  - ace
  - advantage-client-engine
checksum: 480e444985582576f66e5336fad94b2d8371fb2d
---

# Ace Adssetsearchpath

AdsSetSearchPath

AdsSetSearchPath

Advantage Client Engine

| AdsSetSearchPath  Advantage Client Engine |  |  |  |  |

Sets the search path for opening tables and indexes

Syntax

| UNSIGNED32 | AdsSetSearchPath (UNSIGNED8 \*pucPath); |

Parameters

| pucPath (I) | Search directory. This can be in the form of drive letter and path (f:\path) or UNC (\\server\vol\path). Multiple entries can be supplied if separated by semicolons (";"). |

Remarks

If the AdsOpenTable function is not given a fully qualified path, and the table is not found in the default path (see [AdsSetDefault](ace_adssetdefault.md)), then each directory in the search path is searched for the table. For AdsCreateTable, the default path is used if supplied, otherwise the first search path will be used. For example, if there is no default path and the search path is "f:\data; g:\data", then AdsCreateTable will create tables in f:\data.

When using a search path, the existence check for the file is done on the client so that it does not have to attempt to open the table on each server in the search path. If there is no search path, then no existence check is made on the client and the table is assumed to exist in the default path.

When using the Advantage Internet Server, the use of a search path can cause the Advantage Client Engine to connect to each server in the search path because a connection is required before the existence check can be made. For example, if the search path is "\\server1\vol1\data; \\server2\vol1\data", then the Advantage Client Engine will connect to both server1and server2 if a table exists on server2 and not on server1. If this is not desired, then an application should avoid using search paths and either use [AdsSetDefault](ace_adssetdefault.md) or supply a full path with each open or create request.

AdsSetSearchPath is a global setting that affects the behavior of the entire application.

The search path set by AdsSetSearchPath is only used when [rights checking](master_check_rights.md) is enabled by [AdsSetRightsChecking](ace_adssetrightschecking.md) and the ADS\_RESPECTRIGHTS flag is passed to [AdsOpenTable](ace_adsopentable.md).

Example

[Click Here](ace_examples.md#adssetsearchpathexample)

See Also

[AdsGetSearchPath](ace_adsgetsearchpath.md)

[AdsSetDefault](ace_adssetdefault.md)

[AdsOpenTable](ace_adsopentable.md)

[AdsCreateTable](ace_adscreatetable.md)

[AdsGetTableHandle](ace_adsgettablehandle.md)
